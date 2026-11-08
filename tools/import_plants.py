#!/usr/bin/env python3
"""Plants with recorded human uses or poisons, and natural-product drugs with the organisms that
produce them. Pointer cards only: Rose shows what the sources record, it never says that something
is safe to eat or to take.

  taxa    USDA GRIN taxonomy download (taxonomy_data.cab: taxonomy_use, species, genus, family,
          common names) - species with a recorded use as human food, food additive, medicine,
          social use (stimulant, hallucinogen ...), pesticide or poison. Infraspecific taxa and
          synonyms are merged into the species. Accepted name, synonyms and POWO link from WCVP
          (Kew, CC BY 3.0). Cards bio:taxon.<name>; status 'caution' when food or poison is recorded.
  drugs   Wikidata (CC0): compounds with an ATC code (P267) that are found in an organism (P703,
          mostly from LOTUS) - plants, fungi, bacteria. Cards bio:drug.<name>. A found-in claim
          without a reference is listed as such.
          Plus synthetic and semi-synthetic drugs known before ivermectin (1981): active ingredients of
          the FDA Orange Book (public domain) approved in the US before 1 January 1982, salts merged
          into the active moiety, ATC code by name from Wikidata. Natural products that are also in
          that list get the approval note.

Inputs: data/plants/grin_dl/*.txt (7z e taxonomy_data.cab), data/plants/wcvp_dl/wcvp_dwca.zip,
        data/pharma/ob_dl/products.txt (unzip of https://www.fda.gov/media/76860/download).
Usage: import_plants.py taxa|drugs [--dry-run]
"""
import argparse
import collections
import csv
import io
import os
import re
import sys
import time
import zipfile

import requests

import rose_db as R

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "plants")
GRIN = os.path.join(BASE, "grin_dl")
WCVP = os.path.join(BASE, "wcvp_dl", "wcvp_dwca.zip")
GRIN_URL = "https://npgsweb.ars-grin.gov/gringlobal/taxon/taxonomydetail?id={}"
USES = {"FOOD": "human food", "ADDITIVE": "food additive", "MEDICINE": "medicine", "SOCIAL": "social use",
        "PESTICIDE": "pesticide", "POISON": "poison"}
CAUTION = ("[CAUTION: whether a plant is safe to eat depends on the plant part, ripeness, preparation and "
           "amount, and above all on correct identification (poisonous look-alikes) - Rose only shows what the "
           "sources record and does not confirm that anything is safe to eat]")
csv.field_size_limit(10 ** 9)
ORANGE_BOOK = os.path.join(BASE, "..", "pharma", "ob_dl", "products.txt")
# salt, ester and hydrate words after the active moiety (Orange Book ingredient strings)
SALT = set("""HYDROCHLORIDE HCL SULFATE SODIUM POTASSIUM CALCIUM MAGNESIUM ZINC ALUMINUM LITHIUM CITRATE
ACETATE PHOSPHATE MALEATE TARTRATE BITARTRATE SUCCINATE FUMARATE MESYLATE BESYLATE TOSYLATE BROMIDE
HYDROBROMIDE IODIDE CHLORIDE NITRATE LACTATE GLUCONATE STEARATE PALMITATE DIPROPIONATE PROPIONATE
VALERATE BUTYRATE CYPIONATE ENANTHATE DECANOATE UNDECYLENATE BENZOATE SALICYLATE PAMOATE NAPSYLATE
HYCLATE MONOHYDRATE DIHYDRATE TRIHYDRATE HYDRATE ANHYDROUS BENZATHINE PROCAINE MEGLUMINE TROMETHAMINE
DISODIUM DIPOTASSIUM METHYLBROMIDE METHYLSULFATE SACCHARATE ASPARTATE ESTOLATE ETHYLSUCCINATE
LACTOBIONATE GLUCEPTATE PHOSPHATE, SODIUM, SUCCINATE, ACETONIDE""".replace(",", "").split())


def orange_book_before_1982():
    """active moiety -> ingredient strings approved in the US before 1982 (Orange Book wording:
    'Approved Prior to Jan 1, 1982'). Combination products count for each of their ingredients."""
    out = collections.defaultdict(set)
    with open(ORANGE_BOOK, encoding="latin-1") as fh:
        head = fh.readline().rstrip("\n").split("~")
        for line in fh:
            r = dict(zip(head, line.rstrip("\n").split("~")))
            if "Prior" not in r.get("Approval_Date", ""):
                continue
            for ing in re.split(r"[;/]", r["Ingredient"]):
                ing = re.sub(r",\s*(MICROCRYSTALLINE|ULTRAMICROCRYSTALLINE|DIBASIC|MONOBASIC)$", "", ing.strip().rstrip(")").strip())
                w = ing.split()
                while len(w) > 1 and w[-1] in SALT:
                    w.pop()
                if w:
                    out[" ".join(w)].add(ing)
    return out


def grin(name):
    with open(os.path.join(GRIN, name), encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE):
            yield {k: (None if v == "\\N" else v) for k, v in row.items()}


def plain(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def species_key(name):
    """'Solanum tuberosum subsp. tuberosum' -> 'Solanum tuberosum'; hybrids keep the x."""
    w = name.split()
    if len(w) >= 3 and w[1] in ("x", "×"):
        return " ".join(w[:3])
    return " ".join(w[:2])


def wcvp_index(keys):
    """accepted WCVP record and species synonyms for the wanted names."""
    by_id, accepted, syn = {}, {}, collections.defaultdict(list)
    with zipfile.ZipFile(WCVP) as z, z.open("wcvp_taxon.csv") as fh:
        rows = csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8"), delimiter="|", quoting=csv.QUOTE_NONE)
        for r in rows:
            by_id[r["taxonid"]] = (r["scientfiicname"], r["taxonomicstatus"], r["acceptednameusageid"], r["family"],
                                   r["references"], r["taxonrank"])
    name_to_acc = {}
    for tid, (name, status, acc, fam, ref, rank) in by_id.items():
        if name in keys:
            target = tid if status == "Accepted" else acc
            if target in by_id and (name not in name_to_acc or status == "Accepted"):
                name_to_acc[name] = target
        if status == "Synonym" and rank == "Species" and acc:
            syn[acc].append(name)
    for name, tid in name_to_acc.items():
        n, _, _, fam, ref, _ = by_id[tid]
        accepted[name] = {"accepted": n, "family": fam, "powo": ref, "synonyms": sorted(set(syn.get(tid, [])) - {name})[:8]}
    return accepted


def taxa(a):
    fam = {r["taxonomy_family_id"]: r["family_name"] for r in grin("taxonomy_family.txt")}
    gen = {r["taxonomy_genus_id"]: fam.get(r["taxonomy_family_id"]) for r in grin("taxonomy_genus.txt")}
    sp = {}
    for r in grin("taxonomy_species.txt"):
        sp[r["taxonomy_species_id"]] = (r["current_taxonomy_species_id"], plain(r["name"]), gen.get(r["taxonomy_genus_id"]))
    def key_of(sid):
        cur = sp.get(sid)
        if not cur:
            return None, None
        cur = sp.get(cur[0], cur)
        return species_key(cur[1]), cur[2]
    uses, fams, grin_id = collections.defaultdict(list), {}, {}
    for r in grin("taxonomy_use.txt"):
        code = r["economic_usage_code"]
        if code not in USES:
            continue
        k, family = key_of(r["taxonomy_species_id"])
        if not k:
            continue
        uses[k].append((code, r["usage_type"] or "", (r["plant_part_code"] or "").lower(), plain(r["note"])))
        fams[k] = family
    for sid, (cur, name, _) in sp.items():               # the GRIN page of the species itself, else of an accepted infraspecific taxon
        k = species_key(name)
        if k in uses and cur == sid and (name == k or k not in grin_id):
            grin_id[k] = sid
    common = collections.defaultdict(list)
    for r in grin("taxonomy_common_name.txt"):
        if r["language_description"] == "English" and r["taxonomy_species_id"]:
            k, _ = key_of(r["taxonomy_species_id"])
            if k in uses and r["name"] not in common[k]:
                common[k].append(r["name"])
    print(f"GRIN: {len(uses)} species with a recorded use", flush=True)
    wc = wcvp_index(set(uses))
    print(f"WCVP: {len(wc)} matched", flush=True)
    # GRIN species that WCVP treats as one accepted species are merged under the accepted name
    merged = collections.defaultdict(list)
    for k in uses:
        merged[wc.get(k, {}).get("accepted") or k].append(k)
    for acc, ks in merged.items():
        if len(ks) > 1 or ks[0] != acc:
            main_k = acc if acc in ks else ks[0]
            for k in ks:
                if k != main_k:
                    uses[main_k] += uses.pop(k)
                    common[main_k] += [x for x in common.pop(k, []) if x not in common[main_k]]
                    grin_id.setdefault(main_k, grin_id.get(k))
                    fams.setdefault(main_k, fams.get(k))
                    if k in wc and main_k not in wc:
                        wc[main_k] = wc[k]
    print(f"after merging WCVP synonyms: {len(uses)} species", flush=True)

    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "grin", "https://npgsweb.ars-grin.gov/gringlobal/taxon/abouttaxonomy", "LicenseRef-USGov-PD",
                          False, "USDA ARS GRIN taxonomy, economic uses (World Economic Plants); US federal work, "
                          "cite as USDA ARS NPGS; names and synonyms from WCVP (Kew, CC BY 3.0)")
    st = collections.Counter()
    for k in sorted(uses):
        u = uses[k]
        w = wc.get(k, {})
        name = w.get("accepted") or k
        by = collections.defaultdict(list)
        for code, typ, part, note in u:
            t = typ.replace("\\N", "") or code.lower()
            if part:
                t += f" ({part})"
            if t not in by[code]:
                by[code].append(t)
        codes = set(by)
        cn = common.get(k, [])[:5]
        title = name + (f" ({cn[0]})" if cn else "")
        parts = [f"{name} - plant species, family {w.get('family') or fams.get(k) or '?'}"]
        if cn:
            parts[0] += " [common names: " + "; ".join(cn) + "]"
        rec = "; ".join(f"{USES[c]}: {', '.join(by[c][:8])}" for c in USES if c in by)
        parts.append(f"recorded uses (USDA GRIN): {rec}")
        if "FOOD" in codes and "POISON" in codes:
            parts.append("[recorded BOTH as human food and as poisonous]")
        if codes & {"FOOD", "POISON"}:
            parts.append(CAUTION)
        if w.get("synonyms"):
            parts.append("[synonyms: " + "; ".join(w["synonyms"]) + "]")
        intent = " ".join(parts)
        status = "caution" if codes & {"FOOD", "POISON"} else "defined"
        st[status] += 1
        st["food"] += "FOOD" in codes
        st["poison"] += "POISON" in codes
        st["both"] += {"FOOD", "POISON"} <= codes
        payload = {"domain": "botany", "status": status, "uses": {USES[c]: by[c] for c in by},
                   "grin": GRIN_URL.format(grin_id[k]) if grin_id.get(k) else None, "powo": w.get("powo"),
                   "family": w.get("family") or fams.get(k), "common_names": cn, "synonyms": w.get("synonyms", [])}
        if a.dry_run:
            if k in ("Solanum tuberosum", "Sambucus nigra", "Catha edulis", "Allium ursinum"):
                print(intent[:900])
            continue
        ref = R.free_ref(cur, f"bio:taxon.{R.slug(name)}", None) if not R.unit_by_alias(cur, "taxon", name) \
            else R.unit_by_alias(cur, "taxon", name)[1]
        uid = R.upsert_unit(cur, ref=ref, kind="bio", name=title, intent=intent, source_id=sid,
                            source_url=payload["grin"] or payload["powo"] or "https://npgsweb.ars-grin.gov", payload=payload)
        R.set_alias(cur, uid, "taxon", name)
    if not a.dry_run:
        R.mark_imported(cur, sid)
        con.commit()
    print("taxa", dict(st), flush=True)


def drugs(a):
    s = requests.Session()
    s.headers["User-Agent"] = R.USER_AGENT
    # scholarly articles are no longer in the main query graph (WDQS graph split): only their ids come
    # from SPARQL, titles and dates from the API
    q = """SELECT ?c ?cl ?atc ?t ?tl (COUNT(?ref) AS ?nref) (SAMPLE(?r) AS ?rid) WHERE {
      ?c wdt:P267 ?atc ; p:P703 ?st . ?st ps:P703 ?t .
      OPTIONAL { ?st prov:wasDerivedFrom ?ref . OPTIONAL { ?ref pr:P248 ?r } }
      ?c rdfs:label ?cl FILTER(lang(?cl)='en') ?t rdfs:label ?tl FILTER(lang(?tl)='en') }
      GROUP BY ?c ?cl ?atc ?t ?tl"""
    for attempt in range(4):
        r = s.get("https://query.wikidata.org/sparql", params={"query": q, "format": "json"}, timeout=300)
        if r.status_code == 200:
            break
        time.sleep(30)
    r.raise_for_status()
    comp = collections.defaultdict(lambda: {"atc": set(), "taxa": {}, "refs": {}})
    for b in r.json()["results"]["bindings"]:
        c = comp[b["c"]["value"].rsplit("/", 1)[1]]
        c["label"] = b["cl"]["value"]
        c["atc"].add(b["atc"]["value"])
        c["taxa"][b["tl"]["value"]] = max(c["taxa"].get(b["tl"]["value"], 0), int(b["nref"]["value"]))
        if "rid" in b:                                  # one reference per organism is enough to point to
            c["refs"][b["tl"]["value"]] = b["rid"]["value"].rsplit("/", 1)[1]
    print(f"compounds with ATC code and a producing organism: {len(comp)}", flush=True)
    want = sorted({r for c in comp.values() for t, r in c["refs"].items() if len(c["taxa"]) <= 3})
    title = {}
    for k in range(0, len(want), 50):
        e = s.get("https://www.wikidata.org/w/api.php", params={"action": "wbgetentities", "ids": "|".join(want[k:k + 50]),
                  "props": "labels|claims", "languages": "en", "format": "json"}, timeout=60).json()["entities"]
        for qid, v in e.items():
            lab = (v.get("labels", {}).get("en") or {}).get("value")
            yr = next((x["mainsnak"]["datavalue"]["value"]["time"][1:5] for x in v.get("claims", {}).get("P577", [])
                       if x["mainsnak"].get("snaktype") == "value"), None)
            doi = next((x["mainsnak"]["datavalue"]["value"] for x in v.get("claims", {}).get("P356", [])
                        if x["mainsnak"].get("snaktype") == "value"), None)
            if lab:
                title[qid] = lab + (f" ({yr})" if yr else "") + (f", doi:{doi}" if doi else "")
        time.sleep(0.3)
    for c in comp.values():
        c["refs"] = {t: title[r] for t, r in c["refs"].items() if r in title}

    # ATC group names: Wikidata's own labels (CC0) of the group codes - not the WHO index, whose terms
    # forbid commercial distribution and changes; groups without a usable label keep only the code
    q3 = """SELECT ?code ?l WHERE { ?g wdt:P267 ?code FILTER(STRLEN(?code) < 7) ?g rdfs:label ?l FILTER(lang(?l)='en') }"""
    r3 = s.get("https://query.wikidata.org/sparql", params={"query": q3, "format": "json"}, timeout=300)
    r3.raise_for_status()
    group = {b["code"]["value"]: b["l"]["value"] for b in r3.json()["results"]["bindings"]
             if not b["l"]["value"].lower().startswith("atc code")}
    print(f"ATC group labels from Wikidata: {len(group)}", flush=True)

    def atc_groups(codes):
        out = []
        for code in sorted(codes):
            for n in (5, 4, 3, 1):
                g = code[:n]
                if g in group and f"{g} {group[g]}" not in out:
                    out.append(f"{g} {group[g]}")
        return out

    # drugs approved in the US before 1982: match the active moiety to a Wikidata item with an ATC code
    ob = orange_book_before_1982()
    q2 = """SELECT ?c ?l (GROUP_CONCAT(DISTINCT ?atc; separator=' ') AS ?atcs) WHERE { ?c wdt:P267 ?atc .
      { ?c rdfs:label ?l } UNION { ?c skos:altLabel ?l } FILTER(lang(?l)='en') } GROUP BY ?c ?l"""
    r2 = s.get("https://query.wikidata.org/sparql", params={"query": q2, "format": "json"}, timeout=300)
    r2.raise_for_status()
    by_name, atc_of, label_of = collections.defaultdict(set), {}, {}
    for b in r2.json()["results"]["bindings"]:
        qid = b["c"]["value"].rsplit("/", 1)[1]
        by_name[b["l"]["value"].upper()].add(qid)
        atc_of[qid] = set(b["atcs"]["value"].split())
    approved, unmatched = {}, {}
    for moiety, forms in ob.items():
        cands = by_name.get(moiety) or set().union(*(by_name.get(f, set()) for f in forms))
        if len(cands) == 1:
            approved.setdefault(next(iter(cands)), set()).update(forms)
        else:
            unmatched[moiety] = forms
    print(f"Orange Book before 1982: {len(ob)} active moieties, {len(approved)} matched to Wikidata (ATC), "
          f"{len(unmatched)} not matched", flush=True)
    missing = [qid for qid in approved if qid not in comp]
    for k in range(0, len(missing), 50):                 # English labels of the synthetic ones
        e = s.get("https://www.wikidata.org/w/api.php", params={"action": "wbgetentities", "ids": "|".join(missing[k:k + 50]),
                  "props": "labels", "languages": "en", "format": "json"}, timeout=60).json()["entities"]
        label_of.update({qid: (v.get("labels", {}).get("en") or {}).get("value") for qid, v in e.items()})
        time.sleep(0.3)
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "wikidata", "https://www.wikidata.org", "CC0-1.0", False,
                          "defining formulas, theorems, conjectures, physical laws, unsolved problems")
    st = collections.Counter()
    for q_, c in sorted(comp.items()):
        sourced = sorted(t for t, n in c["taxa"].items() if n)
        bare = sorted(t for t, n in c["taxa"].items() if not n)
        # LOTUS also records trace detections (diazepam in wheat): 'recorded as found in', not 'made by'
        parts = [f"{c['label']} - drug (ATC {', '.join(sorted(c['atc']))}), recorded in Wikidata as found in organisms"]
        if sourced and len(sourced) <= 3:                # few producers: name the publication behind each claim
            parts.append(f"- {len(sourced)} organism(s): " + "; ".join(
                t + (f" (source: {c['refs'][t]})" if t in c["refs"] else "") for t in sourced))
        elif sourced:
            parts.append(f"- {len(sourced)} organism(s): " + "; ".join(sourced[:15]) + (" ..." if len(sourced) > 15 else ""))
        if bare:
            parts.append("[found-in claim WITHOUT a source in Wikidata - unconfirmed: " + "; ".join(bare[:10]) + "]")
        grp = atc_groups(c["atc"])
        if grp:
            parts.append("[ATC groups: " + "; ".join(grp) + "]")
        if q_ in approved:
            parts.append("[a found-in record can be a trace detection; the drug itself may be made synthetically]")
            parts.append(f"[US approval before 1982 (FDA Orange Book): {'; '.join(sorted(approved[q_])[:6]).lower()}]")
        parts.append("[pointer only: dose, preparation and safety are not covered - see the drug's own documentation]")
        intent = " ".join(parts)
        st["approved_before_1982"] += q_ in approved
        st["with_atc_group_name"] += bool(grp)
        st["with_source"] += bool(sourced)
        st["only_unsourced"] += not sourced
        payload = {"domain": "pharmacology", "status": "defined" if sourced else "disputed", "wikidata": q_,
                   "atc": sorted(c["atc"]), "found_in": sourced, "found_in_unsourced": bare,
                   "found_in_refs": {t: c["refs"][t] for t in sourced if t in c["refs"]},
                   "approved_us_before_1982": sorted(approved.get(q_, [])) or None, "atc_groups": grp or None}
        if a.dry_run:
            if c["label"] in ("ephedrine", "methamphetamine", "cathine", "avermectin", "morphine", "artemisinin"):
                print(intent[:700])
            continue
        hit = R.unit_by_alias(cur, "wikidata", q_)
        ref = hit[1] if hit and hit[1].startswith("bio:drug.") else R.free_ref(cur, f"bio:drug.{R.slug(c['label'])}", hit[0] if hit else None)
        if hit and hit[1] != ref:                    # an existing Wikidata card of this compound becomes the drug card
            cur.execute("UPDATE rose_unit SET ref=%s, kind='bio' WHERE unit_id=%s", (ref, hit[0]))
        uid = R.upsert_unit(cur, ref=ref, kind="bio", name=c["label"], intent=intent, source_id=sid,
                            source_url=f"https://www.wikidata.org/wiki/{q_}", payload=payload)
        R.set_alias(cur, uid, "wikidata", q_)
    # synthetic / semi-synthetic: approved before 1982, no producing organism recorded
    osid = R.ensure_source(cur, "fda-orange-book", "https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files",
                           "LicenseRef-USGov-PD", False, "FDA Orange Book data files: active ingredients approved in the "
                           "US before 1982; US federal work; ATC codes from Wikidata (CC0)")
    rows = [(qid, label_of.get(qid) or min(forms).lower(), sorted(atc_of[qid]), forms) for qid, forms in approved.items() if qid not in comp]
    rows += [(None, m.lower(), [], forms) for m, forms in unmatched.items()]
    for qid, label, atc, forms in sorted(rows, key=lambda x: x[1]):
        grp = atc_groups(atc)
        intent = (f"{label} - drug" + (f" (ATC {', '.join(atc)})" if atc else "")
                  + (" [ATC groups: " + "; ".join(grp) + "]" if grp else "") + ", known before ivermectin: US approval "
                  f"before 1982 (FDA Orange Book: {'; '.join(sorted(forms)[:6]).lower()}); no producing organism recorded "
                  "(synthetic or semi-synthetic) [pointer only: dose, preparation and safety are not covered - see the drug's "
                  "own documentation]")
        payload = {"domain": "pharmacology", "status": "defined", "wikidata": qid, "atc": atc,
                   "approved_us_before_1982": sorted(forms), "atc_groups": grp or None}
        st["synthetic_before_1982"] += 1
        st["with_atc_group_name"] += bool(grp)
        st["synthetic_without_wikidata"] += qid is None
        if a.dry_run:
            if label in ("diazepam", "ibuprofen", "aspirin", "acetaminophen", "paracetamol", "metamfetamine", "methamphetamine"):
                print(intent[:500])
            continue
        hit = R.unit_by_alias(cur, "wikidata", qid) if qid else R.unit_by_alias(cur, "orangebook", label)
        ref = hit[1] if hit and hit[1].startswith("bio:drug.") else R.free_ref(cur, f"bio:drug.{R.slug(label)}", hit[0] if hit else None)
        if hit and hit[1] != ref:
            cur.execute("UPDATE rose_unit SET ref=%s, kind='bio' WHERE unit_id=%s", (ref, hit[0]))
        uid = R.upsert_unit(cur, ref=ref, kind="bio", name=label, intent=intent, source_id=osid,
                            source_url=f"https://www.wikidata.org/wiki/{qid}" if qid else
                            "https://www.accessdata.fda.gov/scripts/cder/ob/", payload=payload)
        R.set_alias(cur, uid, "wikidata" if qid else "orangebook", qid or label)
    if not a.dry_run:
        R.mark_imported(cur, osid)
        con.commit()
    print("drugs", dict(st), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=["taxa", "drugs"])
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    taxa(a) if a.step == "taxa" else drugs(a)


if __name__ == "__main__":
    sys.exit(main())
