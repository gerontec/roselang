# TODO – contributing to Rose

Rose is an experiment with a built-in exit: if the language does not beat a plain Python
module on the same corpus (benchmark variant **B2**, see [`docs/KONZEPT.md`](docs/KONZEPT.md) §11),
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
5. **English** for identifiers, comments, API fields, DB columns and commit messages.
   The concept document is German; translations are welcome as separate files.
6. **Licences are data.** Keep the SPDX id of every imported source. Do not import
   Project Euler solutions (publication not allowed) or Stack Overflow code. Rosetta Code
   is GFDL (share-alike) – keep it separable (`--license permissive`).
7. **Bio tasks use the local DIAMOND nr** (see [gerontec/blastDiamond](https://github.com/gerontec/blastDiamond)),
   never NCBI online BLAST, and never call `diamond` directly – go through the job queue.

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
| Corpus: OEIS | imported, 401 561 sequences (CC BY-SA 4.0) |
| Embeddings (bge-m3) | `tools/embed.py`; Wikidata + CODATA first, OEIS in background |
| Compiler v1 | `fn`, `const`, `use`, `law` + `solve` (sympy), `table` with exhaustive check, `test`; target Python |
| Diagnostics | E101 E201 E202 E203 E204 E205 E206 E207 E208 E301 E305 E306 E511 E512 R199 R205 |
| `rosec plan` | hybrid search (HNSW vector + FULLTEXT, RRF), category vote, negative-knowledge warnings |

## Open tasks

Pick one, open an issue saying you work on it, keep the PR small.

### Corpus (M1, M4)
- [ ] **Rosetta Code importer** (MediaWiki API): task text → `intent`, solutions per language
      → `rose_impl`, outputs of several languages as test oracle. *Biggest missing piece* –
      the A/B/B2/C benchmark depends on it.
- [ ] **TeX → Rose `eq` converter** for Wikidata formulas using the symbol table (`rose_law_var`),
      then a verify pass: dimensionally consistent → level `tested`. Today Wikidata laws are
      level `imported` and `use law:...` reports `E306 no machine-readable equation`.
- [ ] QUDT import (units, quantity kinds) to replace the built-in unit table in `rose/units.py`.
- [ ] Modelica Standard Library: extract equations of Thermal/Electrical/Fluid models as `law`/`model`.
- [ ] Lean mathlib: index theorem statements as `math` units with level `proven`.
- [ ] Core units (`ctrl:pid…`, `machine:hysteresis_min_runtime`, `model:fopdt`, `bio:*`) as real Rose sources.
- [ ] Public read-only access to the corpus (dump on releases or a public MCP endpoint).

### Compiler
- [ ] `machine` with exhaustive checks (deterministic, reachable, no deadlock) – M5.
- [ ] `ctrl` with mandatory `sample` and bounded outputs (E410/E411), simulation against `model` – M6.
- [ ] Targets C, IEC 61131-3 ST, ESPHome C++.
- [ ] `R201 known-solution`: detect hand-written bodies that resemble a corpus unit.
- [ ] `rose fmt` (canonical form) and AST hash (`rose_unit.ast_hash`).
- [ ] `--self-contained` mode for Rosetta Code submissions (E304), see M8.
- [ ] Quantity literal ambiguity: `9 kW/m` when `m` is also a variable – define and test the rule.

### MCP server (M2)
- [ ] `rose` MCP server exposing `search`, `plan`, `get`, `check`, `compile`, `law_solve`
      (spec: [`spec/mcp-tools.md`](spec/mcp-tools.md)).

### Benchmark (M7) – the decision
- [ ] Task set: Rosetta leave-one-out + 30 house-automation tasks + 10 bio tasks.
- [ ] Variants A (LLM alone), B (LLM + MCP, plain Python), **B2 (LLM + MCP + Python module `rose`)**, C (LLM + MCP + Rose).
- [ ] Python module `rose` for B2: `use()`, `solve()`, quantities, `rose.lock` – same corpus, runtime checks.
- [ ] Report pass@1, tokens, check rounds, unit and table errors; decide language vs. module.

### Later (M8)
- [ ] Register Rose at Rosetta Code ([Add a Language](https://rosettacode.org/wiki/Rosetta_Code:Add_a_Language))
      – only if M7 is positive, with self-contained solutions.
