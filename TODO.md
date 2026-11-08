# TODO – contributing to Rose

Rose is an experiment with a built-in exit: if the language does not beat a plain Python
module on the same corpus (benchmark variant **B2**, see [`docs/CONCEPT.md`](docs/CONCEPT.md) §11),
the language is dropped and Rose lives on as a library. Contributions that help answer that
question honestly are the most valuable ones.

Humans and LLM agents are both welcome. The rules below apply to both.

## Ground rules

1. **Search before you write.** Before implementing an algorithm, formula, controller or
   state machine, look it up (`./rosec plan "<task>"`, `./rosec search "<query>"`). If it
   exists, reference it; if you write it anyway, say why.
2. **Never present an open problem as solved.** Units of kind `open` are *negative
   knowledge*: they tell you that no general solution is known (Riemann hypothesis,
   P vs NP, ...). Do not generate "proofs" or "solutions" for them; work on bounded or
   numerical sub-questions and label them as such.
3. **No invented results.** Numbers in docs, tests and commit messages must come from a
   run you can reproduce (command + output). If something was not tested, write that.
4. **One change per commit, with a test.** Every new diagnostic gets a negative test in
   `tests/neg/<code>[_suffix].rose`; every feature gets a positive test in `tests/*.rose`.
   `python3 tests/run_tests.py` must stay green.
5. **English only**: code, identifiers, comments, docs, corpus texts, commit messages.
6. **No project-specific content** in the compiler or the corpus: no private installations,
   plant configurations or personal scripts. Rose is a general tool.
7. **Licences are data.** Keep the SPDX id of every imported source. Do not import
   Project Euler solutions (publication not allowed) or Stack Overflow code. Rosetta Code
   is GFDL (share-alike) – keep it separable (`--license permissive`).
8. **Bio tasks use a local DIAMOND nr backend** (reference implementation:
   [gerontec/blastDiamond](https://github.com/gerontec/blastDiamond)), never NCBI online BLAST, and
   never call `diamond` directly – go through the backend's job queue.

## Getting started

```sh
git clone https://github.com/gerontec/roselang && cd roselang
python3 tests/run_tests.py                 # offline self-test, needs only python3 + sympy
ROSE_OFFLINE=1 ./rosec test tests/units_demo.rose
```

The corpus (`rose_*` tables, ~412 000 units) lives in a private MariaDB instance; without it
`use` statements report `E301 corpus offline`. Making the corpus publicly reachable is on the
list below.

## Status (2026-11-08)

| Area | State |
|---|---|
| Corpus: Wikidata (formulas, theorems, laws, conjectures, open problems) | importer done (`tools/import_wikidata.py`) |
| Corpus: CODATA 2022 constants | imported, 355 constants |
| Corpus: OEIS | imported, 401 561 sequences (CC BY-SA 4.0) – database only, not shipped |
| Corpus: Rosalind (bio, titles + links) and Wikidata biology methods | imported |
| Corpus: Gene Ontology (38 092 terms, CC BY 4.0) | imported (`tools/import_go.py`) |
| Built-in knowledge | `std/` + `std/catalog.jsonl` (47 967 cards); `rosec` needs no database or server (`rose/knowledge.py`) |
| Embeddings (bge-m3) | `tools/embed.py`; Wikidata + CODATA first, OEIS in background |
| Knowledge → language | `rose/tex.py` converts imported TeX formulas to Rose `law`s, `tools/verify_laws.py` checks them with the compiler, `tools/export_std.py` generates `std/` (CC0/PD only) |
| Negative knowledge | `open name intent "..." end` in the language, `use` of an open problem → `E305` |
| Compiler v1 | `fn`, `const`, `use`, `law` + `solve` (sympy), `table` with exhaustive check, `test`; target Python |
| Diagnostics | E101 E201 E202 E203 E204 E205 E206 E207 E208 E301 E305 E306 E511 E512 R199 R205 (each with a test in `tests/neg/` where listed there) |
| `rosec plan` | built-in catalog, BM25 (+ optional vectors); category = best evidence per category; negative-knowledge warnings; acceptance 7/12 (`tests/run_plan.py`) |

## Open tasks

Pick one, open an issue saying you work on it, keep the PR small.

### Corpus (M1, M4)
- [ ] **Rosetta Code importer** (MediaWiki API): task text → `intent`, solutions per language
      → `rose_impl`, outputs of several languages as test oracle. *Biggest missing piece* –
      the A/B/B2/C benchmark depends on it.
- [x] TeX → Rose `law` converter driven by the symbol table, verify pass with the compiler.
- [ ] Extend the converter: derivatives (`\mathrm{d}`, `\partial`) as `der()`, sums, vectors, systems of equations.
- [ ] **EDAM ontology** (bioinformatics operations, CC BY-SA 4.0 – corpus only, not `std/`).
- [ ] Rosalind: the full problem list (only the first public page is reachable without `?page=`, which robots.txt forbids).
- [ ] QUDT import (units, quantity kinds) to replace the built-in unit table in `rose/units.py`.
- [ ] Modelica Standard Library: extract equations of Thermal/Electrical/Fluid models as `law`/`model`.
- [ ] Lean mathlib: index theorem statements as `math` units with level `proven`.
- [ ] Core units (`ctrl:pid…`, `machine:hysteresis_min_runtime`, `model:fopdt`, `bio:*`) as real Rose sources.
- [ ] Share-alike packs (OEIS, later Rosetta Code) as optional downloads next to `std/`.
- [ ] Wikidata aliases for every card; Wikidata subclasses of GO terms that GO lacks (6 562 items, e.g. illegitimate recombination).

### Compiler
- [ ] `machine` with exhaustive checks (deterministic, reachable, no deadlock) – M5.
- [ ] `ctrl` with mandatory `sample` and bounded outputs (E410/E411), simulation against `model` – M6.
- [ ] Targets C, IEC 61131-3 ST, ESPHome C++.
- [ ] `R201 known-solution`: detect hand-written bodies that resemble a corpus unit.
- [ ] `rose fmt` (canonical form) and AST hash (`rose_unit.ast_hash`).
- [ ] `--self-contained` mode for Rosetta Code submissions (E304), see M8.
- [ ] Quantity literal ambiguity: `9 kW/m` when `m` is also a variable – define and test the rule.

### Packaging
- [x] `pyproject.toml`: distribution `roselang` (the name `rose` is taken on PyPI), import `rose`, command `rosec`;
      wheel carries `rose/std/` (3.7 MB compressed).
- [ ] Publish to PyPI (needs the maintainer's account and token).

### Built-in knowledge (M2)
- [ ] `rosec plan` to ≥ 10/12: synonyms/aliases in the lexical index, P vs NP warning, no warning for a proved
      conjecture that has an open generalisation.
- [ ] Semantic mode: measure `run_plan.py` with `std/catalog.vec` and an embedding endpoint.
- [ ] MCP adapter only if the benchmark shows a need – a thin wrapper around `rosec ... --json`.

### Benchmark (M7) – the decision
- [ ] Task set: Rosetta leave-one-out + 30 engineering tasks (control, state machines, energy flows) + 10 bio tasks.
- [ ] Variants A (LLM alone), B (LLM + `rosec plan`, plain Python), **B2 (LLM + Python module `rose` on the same catalog)**, C (LLM + Rose).
- [x] Python module `rose` for B2 (`rose/lib.py`): `use()`, `law().solve()`, `Q` quantities, `table()`, `plan()`, `lock()`.
- [x] Check comparison without LLM (`bench/compare_b2.py`): Rose 10/10 before running; module 4 at definition, 4 at call, 2 never.
- [ ] Contracts (`require`/`ensure`) in the module; B2 versions of all examples (`bench/b2/`).
- [ ] Report pass@1, tokens, check rounds, unit and table errors; decide language vs. module.

### Later (M8)
- [ ] Register Rose at Rosetta Code ([Add a Language](https://rosettacode.org/wiki/Rosetta_Code:Add_a_Language))
      – only if M7 is positive, with self-contained solutions.
