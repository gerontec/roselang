# Rose – concept of an LLM-optimised programming language

> **In short:** an LLM given a new task should not re-invent what is already solved. Rose is a
> small composition language in which the LLM **references solved building blocks** –
> algorithms, mathematical results, physical laws, constants, controllers, state machines,
> decision tables, bioinformatics methods – and writes only the **glue**. The compiler `rosec`
> **carries this knowledge itself** (`std/`): it finds the blocks, checks the result and compiles
> it to the target language (Python first; C, IEC 61131-3 ST and ESPHome C++ planned). No server
> is needed at run time; the corpus database is only the factory that builds `std/`.

Status and open work: [`TODO.md`](../TODO.md).

---

## 1. Problem

An LLM that receives a coding task writes almost everything from memory: a prime sieve, a PID
controller, the thermal power of a water flow, a hysteresis with minimum run time. Four
weaknesses follow:

| Weakness | Consequence |
|---|---|
| Re-invention | tokens and time spent on solved problems, slightly different every time |
| Remembered instead of verified solutions | off-by-one errors, wrong units, missing anti-windup, unchecked edge cases |
| No provenance | nobody knows where a formula comes from or where it is valid |
| No checkability | a state machine with an unreachable state is found in production |
| Unknown unknowns | the model may "solve" a problem that is in fact open (Riemann hypothesis, P vs NP) |

The solutions exist – spread over Rosetta Code, OEIS, Wikidata, the Modelica Standard Library,
Lean mathlib, CODATA, Rosalind. What is missing is a bridge through which an LLM can
**find, embed and check** them.

## 2. Goals

1. A **corpus of solved building blocks** with provenance, licence, tests and verification
   level, **shipped with the compiler** as `std/` – plus **negative knowledge**: open problems
   marked as such.
2. A **language (Rose)** in which an LLM composes these blocks compactly and unambiguously.
3. A **checker/compiler** that checks types, physical units, contracts, decision tables and state
   machines automatically and generates code for the target platform.
4. A **measurement** that shows whether LLM + Rose beats LLM alone and LLM + a plain library
   (section 11) – otherwise the language is dropped.

"All solved problems" is not a reachable end state but a direction: the corpus grows through
importers (section 6) and through submissions by the LLMs themselves (`rosec submit`, planned).

## 3. Core idea: search before you write

```
task ──► decompose ──► rosec plan / rosec search per sub-problem ──► hit? ─yes─► use <ref>
                                                                      │
                                                                      no
                                                                      ▼
                                                             write it yourself (fn/law/...)
                                                                      │
          rosec check ◄──────────────── Rose source ◄─────────────────┘
               │ diagnostics (--json) ─► LLM fixes ─► check again
               ▼
          rosec compile ─► target code + .lock.json (provenance, licences)
               ▼
          rosec test ─► sandbox ─► ok ─► rosec submit (planned: new unit, level "tested")
```

The decisive point is **token economy**: the LLM only gets a **signature card** of a unit
(≈ 50 tokens: name, intent, signature, units, level). It never sees the implementation – the
compiler inserts it. The LLM thinks at the level of "sieve up to n", not at the level of loops.

**Who chooses a unit?** Finding and ranking is automatic (`rosec plan/search` over the built-in
catalog). Choosing
is the LLM's job: it writes `use law:...` explicitly, so the decision stays visible and
reviewable. Choosing the implementation for the target is automatic again (compiler, pinned in
the lock file). Afterwards the compiler checks: `R201` when hand-written code duplicates a corpus
unit, `R202` when a better-verified unit with the same signature exists, `E305` when an open
problem is used as a building block.

## 4. Design principles

| # | Principle | In Rose |
|---|---|---|
| P1 | **Reference, not copy** | `use rc:Sieve_of_Eratosthenes` instead of 20 lines; units pinned by hash (the lock file) |
| P2 | **One canonical form** | `rose fmt` is part of the language; no synonyms, no optional syntax. Same meaning → same text → same AST hash |
| P3 | **Explicit over implicit** | types, physical units, effects (`effect io, time`), controller sample time, value ranges |
| P4 | **Intent is code** | every `fn`/`law`/`ctrl`/`machine` carries `intent "..."` – the search key; new code becomes findable |
| P5 | **Locally checkable** | `require`/`ensure` contracts, tests in the same file, finite parts (tables, machines) **enumerated exhaustively** |
| P6 | **Machine-readable diagnostics** | code, location, explanation, fix suggestion as JSON |
| P7 | **No runtime of its own** | Rose compiles to existing platforms |
| P8 | **Blocks without significant indentation** | `do ... end`; LLMs lose indentation levels in long answers |
| P9 | **Vocabulary that tokenises well** | short English keywords, ASCII, no exotic operators |
| P10 | **Re-invention detector** | a hand-written body resembling a corpus unit triggers `R201 known-solution` |
| P11 | **Negative knowledge** | open problems are corpus units of kind `open`: found by search, never usable |

Rose is less a general-purpose language than a **planning and composition language with a
checker**. A deliberately small core covers loops, strings and glue code.

## 5. The language

Grammar draft: [`spec/grammar.ebnf`](../spec/grammar.ebnf). Examples: [`examples/`](../examples),
tested programs: [`tests/`](../tests).

### 5.1 Core

```rose
module demo.primes

use rc:Sieve_of_Eratosthenes as sieve        # Rosetta Code task
use oeis:A000040 as primes                   # the prime numbers

fn primes_below(n: Int{>= 2}) -> List[Int]
  intent "all primes smaller than n"
  ensure sorted(result) and all(result, primes.contains)
  cost   O(n log log n)
do
  return sieve(n - 1)
end

test primes_below(10) == [2, 3, 5, 7]
```

- Types: `Int`, `Real`, `Bool`, `Text`, `List[T]`, `Map[K,V]`, `Opt[T]`, enums `{a, b, c}`.
- Refinements: `Int{>= 2}`, `Real[%]{0 .. 100}` (checked at run time as contracts).
- **Quantities:** `Real[W]`, `Real[kg/s]`, `Real[K]`. Absolute temperatures (`degC`) and
  temperature differences (`K`) are different types: `degC - degC` gives `K`, `degC + degC` is
  an error. Run-time values are SI floats.
- Effects: functions are pure unless they declare `effect io | time | rand | state`.
- Contracts: `require`, `ensure` (`result`), `cost` (documented complexity).

### 5.2 Kinds of units

| Kind | Keyword | Example | Automatic check |
|---|---|---|---|
| Algorithm | `fn` / `use rc:` | sieve, Dijkstra, LZW | tests, cross-check of several implementations |
| Mathematics | `use math:` / `use oeis:` | binomial coefficient, sequences | equality with reference terms, mathlib proof |
| Physical law | `law` | Q̇ = ṁ·c_p·ΔT, Ohm's law | dimensions, validity range, solvable for any variable |
| Constant | `use const:` | CODATA values | unit, source, uncertainty |
| Plant model | `model` | first order + dead time, storage tank | step response against reference |
| Controller | `ctrl` | PID with anti-windup, two-point, ramp | sample time and output range mandatory, simulation |
| State machine | `machine` | pump with hysteresis + minimum run time | deterministic, total, reachable, no deadlock |
| Decision table | `table` | energy source by state of charge (DMN, hit `unique`) | complete and overlap-free by exhaustive enumeration |
| Bioinformatics | `use bio:` | homology search, sequence by accession, alignment | local DIAMOND backend enforced (5.7) |
| Open problem | – (`use open:` is an error) | Riemann hypothesis, P vs NP | `E305`: negative knowledge, hint only |

### 5.3 Physical laws are acausal

A `law` is an **equation, not an assignment** (as in Modelica). The LLM names what it wants and
what is given; the compiler solves:

```rose
law water_heat_flow
  intent "thermal power carried by a water flow"
  var P:    Real[W]
  var mdot: Real[kg/s]
  var cp:   Real[J/(kg*K)] = 4182 J/(kg*K)
  var dT:   Real[K]
  eq  P = mdot * cp * dT
  valid dT in 0.5 K .. 80 K
end

fn flow_for(p: Real[W], spread: Real[K]) -> Real[kg/s]
  intent "mass flow needed to carry power p at temperature spread"
do
  return solve water_heat_flow for mdot given P = p, dT = spread
end
```

`solve` is resolved symbolically at compile time (`mdot = P/(cp*dT)`, sympy), with a dimension
check of the law and a run-time check of the validity range.

### 5.4 Controllers

```rose
ctrl buffer_temp
  intent "keep tank temperature at setpoint via heater demand"
  use    ctrl:pid.parallel.antiwindup as pid
  sample 10 s
  in     y: Real[degC]
  in     w: Real[degC]
  out    u: Real[%]{0 .. 100}
  param  kp = 8 %/K, ti = 600 s, td = 0 s
do
  u = pid(e = w - y, kp = kp, ti = ti, td = td)
end
```

Things an LLM tends to forget are **enforced by syntax**: sample time (`E410`), bounded output
(`E411`), unit of the gain.

### 5.5 State machines and decision tables

Decision and amounts are kept apart; tables stay small and orthogonal; every rule set is
checked automatically.

```rose
table discharge_source
  intent "choose energy source by battery state of charge and grid state"
  hit    unique
  in     soc: Real[%]{0 .. 100}, grid_ok: Bool
  out    src: {battery, grid, none}
  rule   soc >= 20 %,  true  -> battery
  rule   soc <  20 %,  true  -> grid
  rule   soc >= 10 %,  false -> battery
  rule   soc <  10 %,  false -> none
  check  complete, no_overlap
end
```

For real-valued inputs the checker splits each axis at the thresholds into intervals and then
enumerates all cells exhaustively (`E511` incomplete, `E512` overlap, each with a counterexample).
State machines (`machine`) get the same treatment for reachability and deadlocks.

### 5.6 Diagnostics

```json
{"code": "E202", "name": "missing-unit", "severity": "error",
 "at": {"file": "flow.rose", "line": 4, "col": 7},
 "message": "number without unit where Real[W] is expected (operator '>')",
 "fix": [{"with": "<value> W"}]}
```

Classes: `E1xx` syntax, `E2xx` types/units, `E3xx` units of the corpus (unknown, no
implementation for the target, open problem), `E4xx` controllers, `E5xx` machines/tables,
`E6xx` bio, `R2xx` recommendations.

### 5.7 Bio tasks: shortcut through a local DIAMOND database

**Rule:** if a task concerns protein sequences, homology, taxa or accessions, Rose always takes
the **local route** through a DIAMOND copy of NCBI nr. Never NCBI online BLAST
(`blastp -remote`, Biopython `qblast`), never `efetch` for sequences that are available locally,
never a hand-written alignment loop over a database.

| Rose unit | maps to |
|---|---|
| `bio:meta.*` – accession, taxon, lineage, counting, "new since" | **plain SQL** on the metadata, no search |
| `bio:seq.get(acc, range?)` | residues from the local database (offset table) |
| `bio:search.blastp` / `blastx` | a job in the backend's queue, two stages: (1) narrow by taxon, length, creation date in SQL → sub-database, (2) DIAMOND with `--dbsize` of the full nr so that E-values stay comparable |

`bio:search` without any filter is an error (`E602`) unless `scope all_nr` is stated. Generated
code never calls `diamond` itself, so the backend's memory planning stays the only one. Counting
questions are SQL, not searches. Reference implementation of such a backend:
[gerontec/blastDiamond](https://github.com/gerontec/blastDiamond).

Bio knowledge comes from Wikidata (bioinformatics methods, laws of genetics and enzyme kinetics,
linked to 19 biology fields), the Rosalind problem list (titles and links only) and the **Gene
Ontology** (all 38 092 non-obsolete terms: processes, functions, components, with synonyms).
Terms that exist in neither source stay unknown – e.g. "heterologous recombination" is neither a
GO term nor a Wikidata item; Wikidata has homologous (Q22280388) and illegitimate recombination
(Q59567515, alias "nonhomologous recombination").

## 6. The corpus – sources

| Source | Content | Licence | Use |
|---|---|---|---|
| **Wikidata** | defining formulas (P2534) with symbols (P7235) and ISQ dimensions (P4020), theorems, conjectures, physical laws, open problems, "proved by" (P1318), biology methods | CC0 | `law`, `math`, `const`, `open`, `bio` units |
| **CODATA** | fundamental physical constants with uncertainty | public domain (NIST) | `const` units |
| **OEIS** | > 400 000 integer sequences with leading terms | CC BY-SA 4.0 | `math` units, terms as test oracle |
| **Rosalind** | classic bioinformatics problems | reference only | `bio` reference cards |
| **Gene Ontology** | biological processes, molecular functions, cellular components, synonyms | CC BY 4.0 | `bio` cards |
| **Rosetta Code** (planned) | ~1 300 tasks, solutions in > 900 languages | GFDL 1.3 (share-alike) | `algo` units, outputs of several languages as test oracle |
| TheAlgorithms (planned) | algorithms in Python, C, Go, … | MIT | permissive alternative |
| Lean mathlib (planned) | > 200 000 proven theorems | Apache-2.0 | `math` facts, level `proven` |
| QUDT (planned) | quantity kinds, units, dimension vectors | CC BY 4.0 | unit system of the checker |
| Modelica Standard Library (planned) | thermal, electrical, fluid, mechanical models | BSD-3 | `law` and `model` units |
| Rose core | controllers, machines, plant models, bio mapping | MIT | reference cards until M5/M6 |

Not used: Project Euler solutions (publication not allowed), Stack Overflow (unclear code
provenance).

**Licences are part of the data model.** Every implementation carries its SPDX id;
`rosec compile` writes a lock file (`.lock.json`) with provenance and licence of every unit and supports
`--license permissive`, which excludes share-alike sources.

## 7. Verification levels

| Level | Meaning |
|---|---|
| `imported` | taken from the source, not executed |
| `parsed` | parses / compiles |
| `tested` | runs in the sandbox, output matches the reference (laws: dimensionally consistent) |
| `cross_checked` | ≥ 2 independent implementations agree |
| `proven` | contract checked formally (mathlib proof, exhaustive enumeration, CBMC) |

Theorems from Wikidata carry `payload.status = proved` (with the prover, e.g. the Poincaré
conjecture, proved by Grigori Perelman, 2002) but stay level `imported` until a machine-checked
proof is linked. Foreign code runs **only in a sandbox** (no network, memory limit, ≤ 20 s).

## 8. Where the knowledge lives

### 8.1 Review after the MCP route (2026-11-08)

The first design put the corpus behind a server (MCP over MariaDB + vector search) that the
compiler and the LLM query at run time. Building and testing it showed:

| Observation (measured in this repository) | Consequence |
|---|---|
| `use`, `plan` and the tests needed DB credentials, an embedding server and the network; without them every `use` failed with `E301 corpus offline` | contributors of a public repository cannot run the compiler at all |
| a query ordered by a column alias returned **wrong neighbours** without any error (MariaDB 11.8 HNSW); `plan` went from 0/12 to 4/12 only after the fix | a server can be silently wrong; the error was visible only through the acceptance test |
| cosine similarity of right and wrong units overlaps (right 0.50–0.71, noise up to 0.55) | a threshold "known / unknown" on embeddings alone is unreliable |
| embedding 400 000 OEIS sequences runs at ~30/s (hours), competing with other jobs on the same GPU | the data path is a batch job, not something to do per query |
| the result of `rosec compile` depended on the state of a database that changes between runs | a compile is not reproducible from the repository |
| an LLM agent with a shell can call `rosec plan --json` directly | an extra tool protocol adds a layer, not a capability |

### 8.2 Architecture

```
build time (maintainers)                     ship time (git)                run time (anyone)
importers ─► corpus DB (rose_*) ─► verify ─► export_std.py ─► std/*.rose  ─► rosec check/compile/test
 Wikidata, CODATA, OEIS, GO, ...   TeX→law     (CC0/PD/MIT/        std/catalog.jsonl ─► rosec plan/search/get
                                   tests        CC BY only)        (std/catalog.vec, optional)
```

- **Knowledge is a release artefact.** `std/` (Rose source of laws, formulas, constants, open
  problems) and `std/catalog.jsonl` (one card per unit: ref, kind, intent, level, licence, source,
  aliases) are generated, committed and versioned with the compiler: the same compiler version
  always has the same knowledge. Current size: 1 252 units with Rose source, 47 967 cards.
- **The compiler needs nothing else.** `rosec plan/search/get` work from the catalog (BM25 over
  name, intent, aliases); `use` binds Rose source from `std/`. Optional: `std/catalog.vec` (int8
  vectors, not in git) plus an embedding endpoint for semantic search.
- **The database is the factory**, not a dependency: importers, TeX→law conversion, verification
  levels, embeddings, export. `--db` (or `ROSE_DB_NAME`) still lets maintainers query it.
- **Share-alike sources are not shipped in `std/`** (OEIS CC BY-SA, Rosetta Code GFDL): they would
  change the licence of the core. They become separate optional packs; until then `oeis:` refs
  resolve only with the database.
- **The LLM interface is the CLI** with `--json`. An MCP adapter, if ever wanted, is a thin wrapper
  around the same commands without logic of its own ([`spec/mcp-tools.md`](../spec/mcp-tools.md) is
  kept as the description of that interface). Schema of the factory:
  [`schema/rose_schema.sql`](../schema/rose_schema.sql).
- **Division of labour stays:** filtering, ranking and counting happen in the compiler, not in the
  LLM; responses are small (k ≤ 10).

## 9. Example: `rosec plan`

`rosec plan "<task>"` is the first test of the toolchain: a new task comes in and Rose recognises,
from the solved problems it resembles, the **category** and the **best solution paths** – and warns
when the task touches an open problem. Real output (built-in knowledge, lexical mode, no server):

```text
$ rosec plan "prove that every even integer greater than 2 is the sum of two primes" -k 3
category:  open  (margin 0.34 over the next category)
           best similarity per category: open 1.00, math/proved 0.66, math/defined 0.64, math/constant 0.37
WARNING:   NEGATIVE KNOWLEDGE: 'Goldbach's conjecture' is an open problem - no known solution. Do not
           claim or search for a general solution; solve a bounded or numerical sub-question instead.
best solution paths:
 1. math:divergence_of_the_sum_of_the_reciprocals_of_the_primes  [math, imported, CC0-1.0]  sim 0.40
 ...
```

Acceptance test `tests/run_plan.py` (12 tasks, expectations written before the first run):
**7/12** with the built-in knowledge, 4/12 with the database route. Open failures: three tasks
whose words do not occur in any card (water mass flow, tank heater; the knowledge is there as a
law but named differently), a German task (intents are English), a missing warning for P vs NP and
a false warning for the Poincaré conjecture (matched to the *generalized* conjecture, which is open).

## 10. Prior art

| Prior art | Taken | Not taken |
|---|---|---|
| Unison | content-addressed code (AST hash) | own runtime and codebase format |
| Modelica | acausal equations, units | DAE simulator, object hierarchy |
| Dafny / SPARK | `require` / `ensure` | mandatory full proofs |
| Hoogle | search by type signature | – |
| DMN / SCXML / IEC 61131 | tables, machines, ST as target | XML as source format |

## 11. Measuring the benefit

Rose only justifies itself if it is measurably better. Same tasks, same models:

- **A** LLM alone, writes Python/C directly.
- **B** LLM + `rosec plan/search` (same catalog), writes Python/C directly (units as example code).
- **B2** LLM + catalog + **Python module `rose`** (or a Perl module): same knowledge, `solve`,
  units, lock file – as a library in plain Python, checks at run time or through a type-checker
  plugin. Extending Python itself (PEP) is not a realistic option.
- **C** LLM + Rose (`rosec`).

Tasks: (1) Rosetta Code tasks **leave-one-out** (the task is removed from the index, its
sub-problems remain findable); (2) 30 engineering tasks (control, state machines, energy flows)
with fixed checks; (3) 10 bio tasks (homology, "new since", counting by taxon) – including whether
the LLM takes the local route or writes online BLAST.

Metrics: pass@1, tokens in/out, number of check rounds, run time, unit errors, table/machine errors.

**First measurement of the checks (2026-11-08, `bench/compare_b2.py`, no LLM involved):** the same
10 faulty programs written in Rose and with the Python module `rose` (`rose/lib.py`, same units,
knowledge and table check). Rose finds 10/10 before anything runs. The module finds 4 when the
code is defined (inconsistent law, open problem, incomplete or overlapping table), 4 only when
the faulty line executes, and 2 never: an error in a branch the test does not take, and plain
numbers passed where quantities are expected. This answers what static checking buys; whether
it outweighs the cost of an unfamiliar language for the LLM is the M7 benchmark.

**Decision rule:** if C is not clearly better than B2, the language is dropped and Rose lives on
as a Python module plus the generated catalog. The real question is whether **static** checking before the
run (units, complete tables, `E305` for open problems) is measurably better than the same checks
at run time.

## 12. Roadmap

| Milestone | Content | Acceptance |
|---|---|---|
| M0 | concept | review ✔ |
| M1 | corpus import (Wikidata, CODATA, OEIS, Rosalind ✔; **Rosetta Code open**), embeddings | paraphrased task → right unit in top 3 for ≥ 80 % |
| M2 | built-in knowledge: `std/` + `std/catalog.jsonl`, `rosec plan/search/get` offline ✔; bio units on the DIAMOND backend; (MCP adapter only if the benchmark asks for it) | `run_plan.py` ≥ 10/12 (now 7/12) |
| M3 | compiler v1: parser, unit checker, Python target; `fn`, `use`, `law`/`solve`, `table`, `test` ✔ | self-test green ✔ |
| M4 | TeX → `eq` converter for imported laws, QUDT, Modelica | 50 imported laws solvable for every variable |
| M5 | `machine` with exhaustive checks; targets ST and C | reference tables re-built in Rose, differential test green |
| M6 | `ctrl` library (PID with anti-windup, two-point, ramp, PT1, SIMC) + ESPHome target | simulation against `model:fopdt` within tolerance |
| M7 | benchmark A/B/B2/C, decision language vs. module | report with numbers |
| M8 (months later, only if M7 is positive) | register Rose at Rosetta Code ([Add a Language](https://rosettacode.org/wiki/Rosetta_Code:Add_a_Language)) | self-contained solutions (`--self-contained`, E304), runnable with the open compiler |

**M8 details:** a Rose solution on Rosetta Code must not just `use rc:<the same task>` – that would
be circular. Solutions published there are GFDL. Focus on what other languages do not show: units,
laws, controllers, checked state machines.

## 13. Risks and open questions

- **Licences:** GFDL/CC BY-SA in generated code → the lock file and `--license permissive`.
  Language and tools MIT, corpus data under the licence of its source.
- **Quality of sources:** Rosetta solutions are often outdated; Wikidata classes are uneven (a
  wrong class id once turned units of time into "open problems" – class ids are now verified by
  label before use).
- **Search without a server:** lexical search misses synonyms and other languages; vectors need
  an embedding model for the query. Aliases and synonyms (Wikidata, GO) go into the cards first.
- **Size of the catalog:** 30 MB of JSON lines in git today (mostly GO definitions); compress or
  split into packs when it grows.
- **Embeddings for code and formulas:** intents are embedded, code is searched by FULLTEXT and
  signature, formulas by symbols and dimensions.
- **Signatures for Rosetta tasks** do not exist and must be generated at import (LLM proposal +
  check against the sample outputs) – the most expensive part of M1/M3.
- **Scope:** "all" problems is unbounded; bounded by milestones and the decision rule in section 11.
- **Security:** foreign code only in the sandbox; `rosec submit` lands in staging.
