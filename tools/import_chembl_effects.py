#!/usr/bin/env python3
"""Measured effects, mechanisms and indications from a local ChEMBL copy (schema `chembl`, MySQL dump of
ChEMBL 37, CC BY-SA 3.0) into the effect map rose_compound_effect / rose_effect (tools/build_effect_map.py).

LOCAL USE ONLY: ChEMBL is share-alike; these rows stay in the local MariaDB for analysis and are never
exported into the public Rose catalog or a pack (P12) - single facts go through facts/*.tsv as before.
Required attribution: Mendez D et al., ChEMBL: towards direct deposition of bioassay data, Nucleic Acids
Res 2019;47(D1):D930-D940, doi:10.1093/nar/gky1075; ChEMBL IDs are kept, the release is recorded.

Compounds are matched by standard InChIKey (rose_compound.inchikey); drug cards without an InChIKey by
the ChEMBL ID of their Wikidata item is not attempted. Rows, all with source='chembl':
  target      activities with a pChEMBL value on human single-protein or complex targets
              (confidence >= 7, valid data, no potential duplicate), aggregated per compound and target:
              range in micromolar, most frequent measure, number of documents -> evidence
  action      curated mechanism of action (drug_mechanism: action type + target)
  indication  drug indications (drug_indication, MeSH heading, highest clinical phase)
Usage: import_chembl_effects.py [--release 37]
"""
import argparse
import sys

import rose_db as R

STEPS = [
    ("map compounds by InChIKey", """
     CREATE TEMPORARY TABLE tmp_map (compound_id INT NOT NULL, molregno BIGINT NOT NULL, PRIMARY KEY (compound_id, molregno),
                                     KEY (molregno))
     SELECT c.compound_id, cs.molregno FROM rose_compound c
     JOIN chembl.compound_structures cs ON cs.standard_inchi_key = c.inchikey COLLATE utf8mb4_unicode_ci
     WHERE c.inchikey IS NOT NULL"""),
    ("aggregate activities on human protein targets", """
     CREATE TEMPORARY TABLE tmp_act (KEY (tid)) AS
     SELECT m.compound_id, a.tid,
            MIN(POW(10, 6 - act.pchembl_value)) AS um_min, MAX(POW(10, 6 - act.pchembl_value)) AS um_max,
            SUBSTRING_INDEX(GROUP_CONCAT(act.standard_type ORDER BY act.standard_type), ',', 1) AS measure,
            COUNT(DISTINCT act.doc_id) AS n_docs, COUNT(*) AS n_values,
            SUM(d.doc_type = 'PUBLICATION') AS n_pub,
            SUBSTRING_INDEX(GROUP_CONCAT(COALESCE(d.doi, CONCAT('https://www.ebi.ac.uk/chembl/document_report_card/', d.chembl_id))
                                         ORDER BY (d.doc_type = 'PUBLICATION') DESC, d.year DESC SEPARATOR '\\t'), '\\t', 1) AS ref,
            SUBSTRING_INDEX(GROUP_CONCAT(a.assay_type ORDER BY a.assay_type), ',', 1) AS assay_type
     FROM tmp_map m
     JOIN chembl.activities act ON act.molregno = m.molregno
     JOIN chembl.assays a ON a.assay_id = act.assay_id
     JOIN chembl.target_dictionary t ON t.tid = a.tid
     JOIN chembl.docs d ON d.doc_id = act.doc_id
     WHERE act.pchembl_value IS NOT NULL AND act.data_validity_comment IS NULL AND act.potential_duplicate = 0
       AND a.confidence_score >= 7 AND t.tax_id = 9606
       AND t.target_type IN ('SINGLE PROTEIN', 'PROTEIN COMPLEX', 'PROTEIN FAMILY', 'PROTEIN-PROTEIN INTERACTION')
     GROUP BY m.compound_id, a.tid"""),
    ("target effects", """
     INSERT INTO rose_effect (kind, name, code, chembl_target)
     SELECT 'target', LEFT(t.pref_name, 255),
            LEFT(GROUP_CONCAT(DISTINCT cseq.accession ORDER BY cseq.accession), 32), t.chembl_id
     FROM (SELECT DISTINCT tid FROM tmp_act) x
     JOIN chembl.target_dictionary t ON t.tid = x.tid
     LEFT JOIN chembl.target_components tc ON tc.tid = t.tid
     LEFT JOIN chembl.component_sequences cseq ON cseq.component_id = tc.component_id
     GROUP BY t.tid
     ON DUPLICATE KEY UPDATE code = COALESCE(rose_effect.code, VALUES(code)), chembl_target = COALESCE(rose_effect.chembl_target, VALUES(chembl_target))"""),
    ("target links", """
     INSERT IGNORE INTO rose_compound_effect (compound_id, effect_id, relation, measure, value_um_min, value_um_max,
                                              test_system, evidence, reference, source)
     SELECT x.compound_id, e.effect_id, 'activity', x.measure, x.um_min, x.um_max,
            CASE x.assay_type WHEN 'B' THEN 'protein' WHEN 'F' THEN 'cells or tissue' WHEN 'A' THEN 'ADME assay' ELSE x.assay_type END,
            CASE WHEN x.n_pub >= 2 THEN 'several_studies' WHEN x.n_pub = 1 THEN 'single_study' ELSE 'screening' END,
            LEFT(x.ref, 255), 'chembl'
     FROM tmp_act x JOIN chembl.target_dictionary t ON t.tid = x.tid
     JOIN rose_effect e ON e.kind = 'target' AND e.name = LEFT(t.pref_name, 255) COLLATE utf8mb4_unicode_ci"""),
    ("mechanism effects", """
     INSERT IGNORE INTO rose_effect (kind, name, code, chembl_target)
     SELECT DISTINCT 'action', LEFT(dm.mechanism_of_action, 255), NULL, t.chembl_id
     FROM tmp_map m JOIN chembl.drug_mechanism dm ON dm.molregno = m.molregno
     LEFT JOIN chembl.target_dictionary t ON t.tid = dm.tid
     WHERE dm.mechanism_of_action IS NOT NULL"""),
    ("mechanism links", """
     INSERT IGNORE INTO rose_compound_effect (compound_id, effect_id, relation, evidence, reference, source)
     SELECT m.compound_id, e.effect_id, LOWER(COALESCE(dm.action_type, 'mechanism')), 'regulatory',
            CONCAT('https://www.ebi.ac.uk/chembl/compound_report_card/', md.chembl_id), 'chembl'
     FROM tmp_map m JOIN chembl.drug_mechanism dm ON dm.molregno = m.molregno
     JOIN chembl.molecule_dictionary md ON md.molregno = m.molregno
     JOIN rose_effect e ON e.kind = 'action' AND e.name = LEFT(dm.mechanism_of_action, 255) COLLATE utf8mb4_unicode_ci"""),
    ("indication effects", """
     INSERT IGNORE INTO rose_effect (kind, name, code)
     SELECT DISTINCT 'indication', LEFT(di.mesh_heading, 255), di.mesh_id
     FROM tmp_map m JOIN chembl.drug_indication di ON di.molregno = m.molregno WHERE di.mesh_heading IS NOT NULL"""),
    ("indication links", """
     INSERT IGNORE INTO rose_compound_effect (compound_id, effect_id, relation, test_system, evidence, reference, source)
     SELECT m.compound_id, e.effect_id, 'treats', CONCAT('clinical phase ', MAX(di.max_phase_for_ind)),
            IF(MAX(di.max_phase_for_ind) >= 4, 'regulatory', 'single_study'),
            CONCAT('https://www.ebi.ac.uk/chembl/compound_report_card/', MAX(md.chembl_id)), 'chembl'
     FROM tmp_map m JOIN chembl.drug_indication di ON di.molregno = m.molregno
     JOIN chembl.molecule_dictionary md ON md.molregno = m.molregno
     JOIN rose_effect e ON e.kind = 'indication' AND e.name = LEFT(di.mesh_heading, 255) COLLATE utf8mb4_unicode_ci
     GROUP BY m.compound_id, e.effect_id"""),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", default="37")
    a = ap.parse_args()
    con = R.connect()
    cur = con.cursor()
    cur.execute("DELETE FROM rose_compound_effect WHERE source='chembl'")
    for title, sql in STEPS:
        cur.execute(sql)
        print(f"{title}: {cur.rowcount}", flush=True)
    cur.execute("DELETE e FROM rose_effect e LEFT JOIN rose_compound_effect ce USING (effect_id) WHERE ce.effect_id IS NULL")
    con.commit()
    cur.execute("SELECT e.kind, COUNT(DISTINCT e.effect_id), COUNT(*), COUNT(DISTINCT ce.compound_id) FROM rose_compound_effect ce "
                "JOIN rose_effect e USING (effect_id) WHERE ce.source='chembl' GROUP BY e.kind")
    for kind, n_eff, n_links, n_comp in cur.fetchall():
        print(f"chembl {a.release}: {kind}: {n_eff} effects, {n_links} links, {n_comp} compounds")


if __name__ == "__main__":
    sys.exit(main())
