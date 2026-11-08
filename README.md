# Rose

**Search before you write.** Rose is a concept for a small, LLM-optimised programming
language. Instead of re-inventing solved problems, an LLM *references* verified building
blocks – algorithms from [Rosetta Code](https://rosettacode.org), mathematical facts,
physical laws, controllers and state machines – and writes only the glue. The compiler
`rosec` carries this knowledge itself (`std/`, no server needed): it finds the blocks, checks
the result (types, physical units, contracts, exhaustive tables and state machines) and
compiles it to Python (C, IEC 61131-3 ST and ESPHome C++ planned).

> Status: **knowledge module usable, compiler v1 experimental.** `rose.exists()` points to known
> solutions in **<!--stat:total_cards-->278 969<!--/stat--> searchable cards** – mathematics, physics, algorithms, control engineering,
> biology, plants and drugs, radio technology, social psychology, Python packages – and says when a
> problem is open, a concept disputed, or a plant has poison records. It never solves the task
> itself. Counts per topic: [`docs/STATISTICS.md`](https://github.com/gerontec/roselang/blob/main/docs/STATISTICS.md).
> Want to help? See [`TODO.md`](https://github.com/gerontec/roselang/blob/main/TODO.md).

## How to use

```sh
pip install roselang          # import name "rose"; development version: pip install git+https://github.com/gerontec/roselang
```

No server, no network, no API key: the knowledge ships with the package. Size: 75 MB download,
118 MB installed, plus a <!--stat:index_mb-->362<!--/stat--> MB index unpacked on the first query into `~/.cache/roselang`
(`$ROSE_CACHE`). First query after installing ~0.6 s, then **~7 ms per query** (median, measured).

**1. Does a known solution exist?** – one verdict, the pointers, their sources:

```sh
$ rosec exists "plan a tour for a delivery van that visits 30 customers and returns to the depot" -k 1
SOLVED: A known solution exists: travelling salesperson problem (TSP) (NP-hard); ready-made solver: networkx.algorithms.approximation.traveling_salesman.traveling_salesman_problem.
  - travelling salesperson problem (TSP)  [problem:travelling_salesperson]  https://www.wikidata.org/wiki/Q322212
$ rosec exists "ESP32 RS485 Modbus RTU master" -k 1
SOLVED: A known solution exists: ESPHome modbus_controller (Modbus RTU master on ESP32/ESP8266); ready-made solver: pip install esphome; YAML: uart + modbus (flow_control_pin) + one modbus_controller per address; esphome run <config>.yaml.
$ rosec exists "is P equal to NP" -k 1
OPEN: No known solution: P versus NP problem is an open problem.
$ rosec exists "is elderberry edible" -k 1
CAUTION: Sources record uses of Sambucus canadensis (American elderberry), see the card; whether anything is safe to eat or to take depends on the part, preparation, amount and correct identification - Rose does not confirm it.
$ rosec exists "mass formation psychosis" -k 1
DISPUTED: Not established knowledge: mass formation psychosis is a proposed, disputed concept without established empirical support - see the source.
```

| Verdict | Means |
|---|---|
| `solved` | a known solution, definition, theorem or maintained package exists – with source, licence and, where there is one, the exact library call |
| `open` | the best match is an unsolved problem (negative knowledge) – do not claim a general solution |
| `caution` | the best match is a plant with food or poison records – shown with source, never a confirmation of safety |
| `disputed` | the best match is a proposed concept without established empirical support |
| `unknown` | nothing in the knowledge matches |

**2. The same from Python** (for an LLM tool call or a script):

```python
import rose
v = rose.exists("estimate the state of a system from noisy measurements")
v["verdict"], v["answer"]          # 'solved', 'A known solution exists: ...'
for s in v["solutions"]:           # ref, name, url, licence, level, call (ready-made solver), status
    print(s["ref"], s["url"], s.get("call"))
rose.get("bio:drug.ephedrine")     # the full card: intent, source, licence, ATC codes ...
rose.search("free space path loss", k=5)   # ranked cards without a verdict
```

**3. More detail** – `rosec plan "<task>"` shows the recognised category, structure and quantities
with units; `rosec search "<words>" [--kind law|math|algo|bio|lib|...]` lists ranked cards;
`rosec get <ref>` prints one card; every command takes `--json`.

**Rules for using the answers:** Rose only *points*. Check the source behind a card before relying
on it; a `solved` card is a pointer, not a verified result for your input. Drug and plant cards
carry no dose, preparation or safety information.

### The language (experimental)

```sh
rosec plan "speed of light in vacuum"
python3 -c 'import rose; print(rose.use("law:kinetic_energy"))'
```

From a checkout:

```sh
python3 tests/run_tests.py                       # self-test, no network
./rosec test examples/kinetic.rose
./rosec plan "prove that every even integer greater than 2 is the sum of two primes"
```

```rose
use law:kinetic_energy                       # from std/ (Wikidata Q46276): T = 1/2 m v^2

fn speed_for(e: Real[J], m: Real[kg]) -> Real[m/s]
  intent "speed of a body of mass m that carries kinetic energy e"
do
  return solve kinetic_energy for v given T = e, m = m
end

test speed_for(200 kJ, 1000 kg) == 20 m/s within 1 %
```

## Contents

| Path | What |
|---|---|
| [`docs/STATISTICS.md`](https://github.com/gerontec/roselang/blob/main/docs/STATISTICS.md) | what can be found: cards per topic, verdicts, distinct facts (`tools/stats.py`) |
| [`docs/pharma/`](https://github.com/gerontec/roselang/tree/main/docs/pharma), [`docs/pypi/`](https://github.com/gerontec/roselang/tree/main/docs/pypi) | browsable overviews: drugs by ATC group, top PyPI packages by topic |
| [`docs/CONCEPT.md`](https://github.com/gerontec/roselang/blob/main/docs/CONCEPT.md) | full concept: principles, language, corpus sources and licences, verification levels, where the knowledge lives, benchmark and go/no-go rule, roadmap |
| [`spec/grammar.ebnf`](https://github.com/gerontec/roselang/blob/main/spec/grammar.ebnf) | grammar draft v0 |
| [`spec/mcp-tools.md`](https://github.com/gerontec/roselang/blob/main/spec/mcp-tools.md) | tool interface (CLI `--json`; optional MCP adapter) and diagnostic codes |
| [`rose/std/`](https://github.com/gerontec/roselang/tree/main/rose/std) | generated standard library and knowledge catalog (do not edit; `tools/export_std.py`) |
| [`schema/rose_schema.sql`](https://github.com/gerontec/roselang/blob/main/schema/rose_schema.sql) | MariaDB 11.8 corpus schema (`rose_*`, `VECTOR(1024)` + HNSW) |
| [`rose/`](https://github.com/gerontec/roselang/tree/main/rose) | compiler v1 (`rosec`): parser, unit checker, solve, tables, Python codegen, corpus access |
| [`tools/`](https://github.com/gerontec/roselang/tree/main/tools) | corpus importers (Wikidata, CODATA, GO, mathlib, Rosetta Code, Modelica, PyPI, GRIN/WCVP, Orange Book, ...), export and release build |
| [`tests/`](https://github.com/gerontec/roselang/tree/main/tests) | self-test: positive programs and negative programs per diagnostic code |
| [`TODO.md`](https://github.com/gerontec/roselang/blob/main/TODO.md) | open tasks and rules for contributors (humans and LLMs) |
| [`examples/`](https://github.com/gerontec/roselang/tree/main/examples) | `fn`, `law`, `ctrl`, `machine`, `table`, `bio` examples |

## Key ideas

- **Reference, not copy:** `use rc:Sieve_of_Eratosthenes` – the model sees a ~50-token
  signature card, the compiler inserts the tested implementation.
- **Units are types:** `Real[kg/s]`, `degC` vs `K`; laws are acausal equations solved at
  compile time.
- **Finite parts are enumerated:** decision tables and state machines are checked for
  completeness, overlap, reachability and deadlock.
- **Machine-readable diagnostics** with fix suggestions, plus `R201 known-solution` when
  hand-written code re-implements a corpus unit.
- **Provenance and licences** in the lock file; `--license permissive` excludes
  share-alike sources (Rosetta Code is GFDL).
- **Bio tasks take the local shortcut:** sequence, homology and taxon questions compile onto the
  local DIAMOND nr ([gerontec/blastDiamond](https://github.com/gerontec/blastDiamond)): MariaDB
  pre-selection, then DIAMOND through the existing job queue; online BLAST is a compile error.
- **Measured, not assumed:** the language is dropped if LLM + Rose does not beat
  LLM + a plain Python module on the same knowledge.

## Licence

Language, tools and documents: MIT. Corpus data keeps the licence of its source.
