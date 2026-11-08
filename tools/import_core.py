#!/usr/bin/env python3
"""Seed the Rose core units (own source, MIT): controllers, state machines, plant models and
the bio units that map onto the local DIAMOND nr (gerontec/blastDiamond).

These are reference cards (level 'imported') until the compiler supports ctrl/machine (M5/M6);
they make `rosec plan` recognise these categories. Intents carry English and German keywords.
"""
import sys

import rose_db as R

CORE = [
    # ref, kind, name, signature, intent
    ("ctrl:pid.parallel.antiwindup", "ctrl", "PID controller, parallel form, anti-windup",
     "(e: Real, kp, ti: Real[s], td: Real[s], sample: Real[s]) -> Real{bounded}",
     "discrete PID controller with output limits and anti-windup (conditional integration) for "
     "temperature, pressure, flow or speed control - PID-Regler mit Begrenzung und Anti-Windup, "
     "Temperaturregelung, Regelkreis, Stellgröße"),
    ("ctrl:two_point", "ctrl", "two-point controller with hysteresis",
     "(y: Real, w: Real, band: Real) -> Bool",
     "on/off controller with hysteresis band, thermostat - Zweipunktregler, Hysterese, Thermostat, ein/aus schalten"),
    ("ctrl:rate_limiter", "ctrl", "rate limiter / ramp", "(u: Real, rate: Real[1/s]) -> Real",
     "limit the rate of change of a setpoint or actuator signal - Rampe, Steigungsbegrenzung, Sollwertrampe"),
    ("ctrl:pt1_filter", "ctrl", "first-order low-pass filter (PT1)", "(x: Real, tau: Real[s]) -> Real",
     "first-order lag filter to smooth noisy measurements - PT1-Glied, Tiefpass, Messwertglättung"),
    ("ctrl:tuning.simc", "ctrl", "SIMC PI/PID tuning rules (Skogestad)", "(model: fopdt) -> (kp, ti, td)",
     "controller tuning from a first-order-plus-dead-time model, SIMC rules - Reglereinstellung, Reglerparameter berechnen"),
    ("machine:hysteresis_min_runtime", "machine", "on/off state machine with hysteresis and minimum run time",
     "(t: Real, t_on, t_off, min_run: Real[s]) -> Bool",
     "pump or compressor switching with hysteresis, minimum on time and minimum off time, "
     "synchronous deterministic Mealy machine - Pumpe schalten, Mindestlaufzeit, Taktsperre, Zustandsautomat"),
    ("machine:debounce", "machine", "debounce of a digital input", "(x: Bool, t: Real[s]) -> Bool",
     "debounce a contact or digital input over a hold time - Entprellen, Eingang entprellen"),
    ("table:decision_unique", "table", "decision table with hit policy unique (DMN)",
     "(inputs...) -> outputs",
     "rule-based decision with complete and overlap-free rules, checked by exhaustive enumeration - "
     "Entscheidungstabelle, Regelmatrix, DMN"),
    ("model:fopdt", "model", "first order plus dead time plant model", "(k, tau: Real[s], theta: Real[s])",
     "process model for step response, tuning and simulation: gain, time constant, dead time - "
     "Streckenmodell PT1 mit Totzeit, Sprungantwort"),
    ("model:thermal_storage", "model", "mixed thermal storage tank",
     "(volume: Real[m^3], ua: Real[W/K]) -> Real[K/s]",
     "energy balance of a fully mixed hot water buffer tank with losses - Pufferspeicher, Wärmespeicher, Energiebilanz"),
    ("bio:search.blastp", "bio", "protein homology search against NCBI nr (local DIAMOND)",
     "(query: Fasta, taxon?, len?, new_days?, sensitivity) -> List[bio.Hit]",
     "BLASTP protein similarity search, homologous sequences, alignment against nr - two-stage: MariaDB "
     "pre-selection by taxon/length/date, then DIAMOND with --dbsize of the full nr via the job queue; never "
     "NCBI online BLAST - Proteinsuche, Homologie, Sequenzvergleich"),
    ("bio:search.blastx", "bio", "translated nucleotide search against nr (local DIAMOND)",
     "(query: Fasta, ...) -> List[bio.Hit]",
     "BLASTX: DNA query translated in six frames against protein nr, local DIAMOND - Nukleotidsequenz gegen Proteine"),
    ("bio:seq.get", "bio", "protein sequence by accession (local nr)", "(acc: Text, range?) -> Fasta",
     "residues of an accession from the local nr_full.dmnd offset table; may contain X runs (masking) - "
     "Sequenz zu Accession holen, kein efetch"),
    ("bio:meta.count", "bio", "count nr sequences by taxon, length and date (SQL)",
     "(taxon?, len?, new_days?) -> Int",
     "how many sequences in nr for an organism, taxon with sub-taxa, length range or created in the last N "
     "days - pure SQL on blast_*, no search - Anzahl Sequenzen zählen"),
    ("bio:meta.taxon", "bio", "taxon with lineage (local taxdump)", "(name or taxid) -> bio.Taxon",
     "taxonomy lookup, lineage, sub-taxa of an organism - Taxonomie, Abstammung, Organismus"),
    ("bio:amylo", "bio", "amyloid propensity per window (Tesla P4)", "(query: Fasta) -> List[Real]",
     "amyloid aggregation propensity of a protein sequence, AmyloDeep on GPU - Amyloid-Neigung"),
]


def main():
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "rose-core", "https://github.com/gerontec/roselang", "MIT", False,
                          "Rose core units: controllers, state machines, plant models, bio mapping")
    for ref, kind, name, sig, intent in CORE:
        R.upsert_unit(cur, ref=ref, kind=kind, name=name, intent=intent, signature=sig, source_id=sid,
                      source_url="https://github.com/gerontec/roselang",
                      payload={"core": True, "domain": "bio" if kind == "bio" else "control"})
    R.mark_imported(cur, sid)
    con.commit()
    print(f"core units: {len(CORE)}")


if __name__ == "__main__":
    sys.exit(main())
