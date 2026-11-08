# Rose – concept of an LLM-optimised programming language

> **In short:** an LLM given a new task should not re-invent what is already solved – and should
> not "solve" what is still open. Rose **carries the knowledge of solved and open problems itself**
> (Python package `roselang`, about 247 000 cards: proved theorems, physical laws, constants,
> algorithms, Rosetta Code tasks, plant models, controllers, state machines, library solvers,
> bioinformatics terms) and answers one question first: **is there a known solution, and where is
> it?** It **points** to the solution – source, licence, ready-made library call – and **solves
> nothing itself**. On top of that sits a small composition language in which the LLM references
> such building blocks and writes only the glue; the compiler `rosec` checks units, tables and
> machines and compiles to Python (C, IEC 61131-3 ST and ESPHome C++ planned). No server is needed
> at run time; the corpus database is only the factory that builds the knowledge.

Status and open work: [`TODO.md`](../TODO.md).

---

## 0. Scope (decision 2026-11-08)

The module's first job is to **show that a solution exists** – not to solve the problem:

```text
$ rosec exists "plan a tour for a delivery van that visits 30 customers and returns to the depot ..."
SOLVED: A known solution exists: travelling salesperson problem (TSP) (NP-hard).
  - travelling salesperson problem (TSP)  [problem:travelling_salesperson]  https://www.wikidata.org/wiki/Q322212
$ rosec exists "is P equal to NP?"
OPEN: No known solution: P versus NP problem is an open problem.
```

The same from Python, after `pip install roselang`:

```python
import rose
rose.exists("estimate the state of a system from noisy measurements")
# {'verdict': 'solved', 'answer': 'A known solution exists: state estimation from noisy
#   measurements (...); ready-made solver: python-control lqe.', 'solutions': [...]}
```

Three answers: **solved** (with pointers to the known solution and its source), **open** (negative
knowledge) or **unknown** (nothing in the knowledge matches). The language and compiler (sections
5, 11) stay, but are no longer the first goal: composing and checking solutions comes after finding
them.

Two rules follow from this scope (decisions 2026-11-08):

| Rule | Means | Does not mean |
|---|---|---|
| **Point, don't solve** | a card holds name, description, source link, licence, complexity, the call of an existing solver (`networkx…traveling_salesman_problem`, `control.lqe`) | no own solver code, no execution of solutions, no generated signatures for every Rosetta task |
| **Recognition inside Rose** | words (BM25), quantities with dimensions, structure of the task (problem classes, §8.3) | no LLM pre-step that rewrites or classifies the task – that would make the answer depend on the model it is meant to support |

**What the module adds over what a large LLM already knows.** Most pointers (TSP → OR-Tools,
PID → Ziegler-Nichols) are known to a large model. The module adds: a verdict that is looked up in
a fixed, versioned source instead of remembered (in particular *open* – the model may not know that
a problem is still unsolved), provenance and licence of every pointer, the exact call of a
maintained library instead of a hand-written re-implementation, and the same knowledge for small
local models that do not have it. Whether this is measurable is the M7 benchmark (§11).

## 1. Problem

An LLM that receives a coding task writes almost everything from memory: a prime sieve, a PID
controller, the thermal power of a water flow, a hysteresis with minimum run time. Five
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

Cards shipped in release 0.1.0 (counted in the installed package, 2026-11-08):

| Source | Content | Licence | Cards | Shipped as |
|---|---|---|---|---|
| **Lean mathlib4** | statements of proved theorems and definitions (cut at `:=`) | Apache-2.0 | 189 932 | `sets/mathlib.jsonl.gz` |
| **Gene Ontology** | all non-obsolete terms: processes, functions, components, synonyms | CC BY 4.0 | 38 092 | catalog |
| **Wikidata** | defining formulas (P2534) with symbols and ISQ dimensions, theorems, conjectures, physical laws, open problems, "proved by" (P1318), algorithms and computational problems, control and automata concepts, biology methods | CC0 | 12 144 | `std/*.rose` + catalog |
| **Modelica Standard Library** 4.x | class index: path, description, source line – models, blocks, functions, state graphs (no equations) | BSD-3 | 3 484 | catalog |
| **Python libraries** | public solver functions: SciPy 723, networkx 587, python-control 154, transitions 37, Python stdlib 26, dd 17, sympy 15, automata-lib 12, OR-Tools 7 (path, signature, first docstring paragraph) | BSD-3 / MIT / Apache-2.0 / PSF | 1 578 | catalog |
| **PyPI** | top 15 000 packages by downloads: summary, licence, installable on CPython 3.14, cleaned README extract (§6.1) | metadata as published; extracts under each package's licence, share-alike left out | 14 498 | catalog (kind `lib`) |
| **Rosetta Code** | all 1 363 tasks with 2 606 Python 3 solutions (compile-checked) | GFDL 1.3 | 1 363 | `sets/rosetta*.jsonl.gz` |
| **CODATA 2022** | fundamental physical constants with uncertainty | public domain (NIST) | 355 | `std/const/codata.rose` |
| **Rosalind** | classic bioinformatics problems | titles and links only | 104 | catalog |
| **Rose core** | 30 problem classes (§8.3), reference controllers, machines, plant models, bio mapping | MIT | 45 | `std/problems.json` + catalog |
| OEIS | > 400 000 integer sequences | CC BY-SA 4.0 | – | **not shipped**, database only |
| QUDT, TheAlgorithms | units and dimensions; permissive algorithms | CC BY 4.0 / MIT | – | planned |

Library solvers are pointers only: nothing is executed except importing the library on the build
host. Libraries are installed there as user packages (`pip install --user`), never over a
distribution package.

Not used: Project Euler solutions (publication not allowed), Stack Overflow (unclear code
provenance).

**Licences are part of the data model.** Every implementation carries its SPDX id;
`rosec compile` writes a lock file (`.lock.json`) with provenance and licence of every unit and supports
`--license permissive`, which excludes share-alike sources.

### 6.1 Public package overview (PyPI) – plan of 2026-11-08

**Gap.** As far as we could find, there is no public, cleaned overview of what Python packages are
*for* that can be searched by task. What exists: raw dumps (PyPI on BigQuery, metadata dumps on
Hugging Face) with READMEs full of badges and HTML; name and summary search (pypi.org,
libraries.io); documentation services for LLMs for selected libraries, online (Context7) or
written by the projects themselves (llms.txt). PyPI has no counterpart of CPAN's conventions (POD
with NAME/SYNOPSIS/METHODS, MetaCPAN full-text search, CPAN Testers): its metadata carries a
one-line summary, keywords and optional classifiers; everything else is free-text README.

**Size (measured 2026-11-08).**

| | CPAN (Perl) | PyPI (Python) |
|---|---|---|
| total | 42 128 distributions, 262 833 modules | 934 596 projects |
| technical | 2 175 distributions (by namespace: Math, Geo, Algorithm, Device, Bio, …) | 2 168 in the top 15 000 alone (by Topic classifier; only 51 % declare one) |
| catalogue data per module | structured (POD, SYNOPSIS, test reports) | free text; rebuilt here |

**Levels and decisions.**

| Level | Content | Scope | Status |
|---|---|---|---|
| 1 | metadata + cleaned README extract | top 15 000 by downloads (hugovk/top-pypi-packages), **in the core package** as cards `pypi:<name>` (kind `lib`) | done: 14 498 cards |
| 1 | same | **all PyPI projects**, a separate dataset, not shipped in the package | running (~1 day, resumable) |
| 2 | public functions with signatures (install + import in a sandbox) | only 1 000–2 000 technical packages, with a public-API filter | later; a trial showed mostly internal noise without a filter (pandas: 1 168 objects) |
| 3 | test results per release and version (as CPAN Testers) | – | not planned: needs a test network, not one machine |

**One record per project** (level 1): name, version, summary, keywords, Topic classifiers, licence,
share-alike flag, `requires_python`, **installable on CPython 3.14 / Linux x86_64** (`wheel`, `sdist`
or not – decided with `packaging.tags` against the interpreter of the build host), date of the last
release, links (PyPI, docs, homepage, source) and a **README extract** of at most 800 characters:
opening text, feature list, one real code example (not `pip install`), section names; badges,
images, HTML and link targets removed (`tools/readme_clean.py`).

**Rules.**
- *Metadata only.* Nothing is installed or run for level 1; the selection of the core package
  follows downloads, because most of the ~935 000 projects are empty, abandoned or squatted names,
  and some are malicious – a weak model must not be pointed to them.
- *Licences.* Metadata is used as each project published it (`LicenseRef-PyPI-metadata`). A README
  extract is the project's own text under its licence; for share-alike licences (GPL family, CC
  BY-SA, EUPL) it is left out and only the metadata is kept.
- *Ranking.* Package cards are broad pointers: their prior is below specific cards (0.70–0.85 by
  download rank), so a problem class or a concrete solver function still wins.
- *Polite fetching.* PyPI JSON API, 4 connections with a pause, identified user agent, cache with
  resume; the BigQuery dump is the alternative for bulk refreshes.

**Publication.**
- [`docs/pypi/`](pypi/README.md): browsable Markdown by topic for the top 15 000 (180 pages; large
  topics split into parts), generated by `tools/pypi_overview.py`.
- The full dataset (all projects, `pypi-<letter>.jsonl.gz` + `STATS.md`, `tools/pypi_dataset.py`) is
  too large for the git history; it is to be published as a release asset or dataset next to the
  repository – where, is decided before the first upload.
- Refresh: re-run monthly (download ranks change); a daily delta from PyPI's update feed is
  possible but not built.

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
proof is linked. Solver functions of maintained libraries (SciPy, networkx, …) are filed as
`tested` because they are covered by their project's own test suite; Rose itself has not run them.
Rosetta solutions are `parsed` (they compile under Python 3, nothing more). Foreign code runs **only in a sandbox** (no network, memory limit, ≤ 20 s).

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
build time (maintainers, build host)          release (wheel)                       run time (anyone)
importers ─► corpus DB (rose_*) ─► verify ─► std/*.rose, std/catalog.jsonl     pip install roselang
 Wikidata, CODATA, GO, mathlib,     TeX→law   std/problems.json                 first start: unpack index
 Rosetta, Modelica, Python libs     tests     std/sets/*.jsonl.gz (mathlib,       to ~/.cache/roselang
                                              Rosetta)                          rose.exists / rosec exists,
                          tools/build_release.sh ─► std/knowledge.sqlite.gz     plan, search, get, use,
                                              (prebuilt SQLite FTS5 index)      check, compile, test
```

- **Everything in one core package** (like torch): no separate data packs to install, no
  importers at run time. The wheel is 62.5 MB; installed 85 MB plus a 297 MB index in
  `~/.cache/roselang` (or `$ROSE_CACHE`), unpacked on the first start (0.5–0.6 s), later starts
  under 0.1 s. The index key is a hash over the source files, so a new release rebuilds it.
- **Knowledge is a release artefact.** `std/` and the sets are generated by the factory and
  versioned with the compiler: the same version always has the same knowledge.
- **The compiler needs nothing else.** `exists/plan/search/get` run on the SQLite index (FTS5,
  BM25); `use` binds Rose source from `std/` or a set card. Optional: `std/catalog.vec` (int8
  vectors, not shipped) plus an embedding endpoint for semantic search – prepared, not measured.
- **The database is the factory**, not a dependency: importers, TeX→law conversion, verification
  levels, export, release build. `--db` (or `ROSE_DB_NAME`) still lets maintainers query it. All
  builds and tests run on the build host, not on a developer notebook.
- **Licences:** the package is an **aggregation** of independent works (GFDL §7): each set keeps its
  licence ([`rose/std/LICENSES.md`](../rose/std/LICENSES.md)), the Rose code stays MIT. Code that
  embeds a Rosetta solution inherits GFDL; Rose warns with `R205` and records it in the lock file.
  OEIS (CC BY-SA) is not shipped; `oeis:` refs resolve only with the database.
- **The LLM interface is the CLI** with `--json`. An MCP adapter, if ever wanted, is a thin wrapper
  around the same commands without logic of its own ([`spec/mcp-tools.md`](../spec/mcp-tools.md) is
  kept as the description of that interface). Schema of the factory:
  [`schema/rose_schema.sql`](../schema/rose_schema.sql).
- **Division of labour stays:** filtering, ranking and counting happen in the compiler, not in the
  LLM; responses are small (k ≤ 10).

### 8.3 Recognising the problem

The mapping "new task → known problem" is not trivial: a tour-planning request never says
"travelling salesperson". Rose combines three known techniques, all inside the package:

| Stage | Technique | Example |
|---|---|---|
| 1. words | lexical retrieval: BM25 over name (weight 3), description, aliases; accents and German/English variants normalised; score scaled by how much of the query a card covers | "Goldbach" → `open:goldbachs_conjecture` |
| 2. quantities | quantities and units taken from the text (`9 kW`, `5 K`, "how fast"); laws whose variables carry exactly these dimensions, the more specific the better | power + temperature difference → heat-flow law |
| 3. structure | **specification matching** (Zaremski & Wing): 30 curated problem classes in `rose/std/problems.json`, each with required facet groups of input, output, objective and constraints, forbidden facets and tie-breakers; facets are regular expressions (English and German) | "locations + round trip + visit all + minimise, one vehicle" → TSP; "+ fleet or capacity" → vehicle routing; "+ minimum run time" → state machine, not on/off control |

A problem class points to its known solvers (`networkx…traveling_salesman_problem`,
`ortools…RoutingModel`, `control.lqe`, `transitions.Machine`) and to related cards (Wikidata,
Modelica). An open problem is reported only if it scores at least 95 % of the best solved match, so
that "prime" alone does not raise the Goldbach warning. Below a threshold the verdict is
**unknown** – a corpus gap, reported as such. Dense retrieval (embeddings) is prepared but not yet
measured.

The 30 classes cover routing and graphs (TSP, vehicle routing, shortest paths, spanning tree,
maximum flow, assignment, topological sort, colouring, route inspection), optimisation (knapsack,
bin packing, set cover, subset sum, job shop, linear programming), sequences and geometry (sorting,
edit distance, LCS, convex hull, binary search) and logic and control (Boolean minimisation, SAT,
decision table check, state machine, PID tuning, state estimation, system response, on/off control,
physical system model). New classes are data, not code.

## 9. Example: `rosec plan`

`rosec plan "<task>"` is the detailed form of `exists`: a new task comes in and Rose recognises,
from the solved problems it resembles, the **category** and the **best solution paths** – and warns
when the task touches an open problem. Real output of release 0.1.0 (installed wheel, lexical
mode, no server):

```text
$ rosec exists "plan a tour for a delivery van that visits 30 customers and returns to the depot, as short as possible"
SOLVED: A known solution exists: travelling salesperson problem (TSP) (NP-hard); ready-made solver:
        networkx.algorithms.approximation.traveling_salesman.traveling_salesman_problem.
  - travelling salesperson problem (TSP)  [problem:travelling_salesperson]  https://www.wikidata.org/wiki/Q322212
  - Knight's tour  [rc:Knight's_tour]  https://rosettacode.org/wiki/Knight%27s_tour

$ rosec plan "prove that every even integer greater than 2 is the sum of two primes" -k 3
category:  open  (margin 0.32 over the next category)
           best similarity per category: open 1.00, algo 0.69, math/defined 0.56, math/proved 0.50
WARNING:   NEGATIVE KNOWLEDGE: 'Goldbach's conjecture' is an open problem - no known solution. Do not
           claim or search for a general solution; solve a bounded or numerical sub-question instead.
best solution paths:
 1. rc:Primality_by_trial_division  [algo, parsed, GFDL-1.3]  sim 0.86
    -> python: rose.use('rc:Primality_by_trial_division').code  (Rosetta Code solution, GFDL share-alike)
 ...
```

The second hit list also shows the weakness of pure word matching: "Knight's tour" is a tour, but
not this one. The verdict comes from the problem class, the list below it is context.

Measurements on the build host (2026-11-08):

| Test | Result | Note |
|---|---|---|
| `tests/run_plan.py`, 12 tasks, expectations written before the first run | **9/12** | was 7/12 (built-in) and 4/12 (database route); failing: P vs NP (the SAT class wins over the open problem), tank heater (right class, test expects a `ctrl:` card), local alignment (a Rosetta global-alignment task wins) |
| `tests/plan_cases_spec.json`, 17 tasks for the problem classes | 17/17 | optimistic: classes and cases were written in the same step |
| Karp's 21 NP-complete problems by name (`tests/karp21.py`) | top-1 19/21, top-3 20/21 | – |
| "how big must the heater be to warm 0.2 kg/s of water by 5 K" | **wrong**: *global warming potential* | "warm" outweighs the quantities; the heat-flow law is in the knowledge but not found |

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
| M1 | corpus import: Wikidata, CODATA, OEIS, Rosalind, GO, Rosetta Code, Lean mathlib, Modelica class index, Python library solvers ✔; embeddings open | paraphrased task → right unit in top 3 for ≥ 80 % (not yet measured) |
| M2 | built-in knowledge in one package: prebuilt index, `exists/plan/search/get` offline ✔, problem classes ✔, `pip install roselang` ✔ (PyPI upload pending); bio units on the DIAMOND backend; MCP adapter only if the benchmark asks for it | `run_plan.py` ≥ 10/12 (now 9/12) |
| M3 | compiler v1: parser, unit checker, Python target; `fn`, `use`, `law`/`solve`, `table`, `test` ✔; Python module `rose` (B2) ✔ | self-test green ✔ |
| M4 | TeX → `eq` converter for imported laws ✔ (first version), QUDT | 50 imported laws solvable for every variable |
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
- **Hints the LLM already knows:** for a large model most pointers are not news (§0). The value
  is the checked verdict, provenance and the exact library call; if M7 shows no gain for large
  models, the target group is small local models.
- **Recognition is the weak point**, not the amount of knowledge: 247 000 cards do not help when
  a word like "warm" outweighs the quantities (§9). Problem classes are hand-written and their test
  cases were written together with them; independent test tasks are needed.
- **Many proofs, few solvers:** 190 000 of the cards are mathlib statements, 1 578 are library
  solvers. Sparse kinds (controllers 38, state machines 78, decision tables 41) are mostly
  Modelica and Wikidata pointers.
- **The "ready-made solver" shown is the first library entry of a class**, not the best one (PID
  tuning still names `scipy.optimize.minimize` before python-control); the order in
  `problems.json` is the ranking.
- **Search without a server:** lexical search misses synonyms; vectors need an embedding model for
  the query. Aliases and synonyms (Wikidata, GO) go into the cards first.
- **Size:** 62.5 MB wheel, 297 MB index on first start; mathlib dominates.
- **Refs are case-insensitive in the factory database** (MariaDB collation): `control.frd` and
  `control.FRD` collide. Importers must use canonical names and must not rely on case.
- **Signatures for Rosetta tasks** are out of scope since the "point, don't solve" decision; a
  Rosetta card is a reference plus Python code to look at, not a typed building block.
- **Scope:** "all" problems is unbounded; bounded by milestones and the decision rule in section 11.
- **Security:** foreign code only in the sandbox; `rosec submit` lands in staging.
