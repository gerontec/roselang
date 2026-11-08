# Rose

**Search before you write.** Rose is a concept for a small, LLM-optimised programming
language. Instead of re-inventing solved problems, an LLM *references* verified building
blocks – algorithms from [Rosetta Code](https://rosettacode.org), mathematical facts,
physical laws, controllers and state machines – and writes only the glue. The compiler
`rosec` carries this knowledge itself (`std/`, no server needed): it finds the blocks, checks
the result (types, physical units, contracts, exhaustive tables and state machines) and
compiles it to Python (C, IEC 61131-3 ST and ESPHome C++ planned).

> Status: **compiler v1 (experimental)**. Built-in knowledge: 1 252 units with Rose source
> (laws, formulas, CODATA constants, open problems) and 47 967 searchable cards (Wikidata,
> CODATA, Gene Ontology, Rosalind). Compiler handles `fn`, `const`, `use`, `law` + `solve`,
> `table`, `test` and emits Python. `rosec plan` acceptance: 7/12.
> Not yet: Rosetta Code import, `machine`/`ctrl`, C/ST/ESPHome targets.
> Want to help? See [`TODO.md`](TODO.md).

```sh
pip install git+https://github.com/gerontec/roselang     # distribution "roselang", import name "rose"
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
| [`docs/CONCEPT.md`](docs/CONCEPT.md) | full concept: principles, language, corpus sources and licences, verification levels, where the knowledge lives, benchmark and go/no-go rule, roadmap |
| [`spec/grammar.ebnf`](spec/grammar.ebnf) | grammar draft v0 |
| [`spec/mcp-tools.md`](spec/mcp-tools.md) | tool interface (CLI `--json`; optional MCP adapter) and diagnostic codes |
| [`rose/std/`](rose/std) | generated standard library and knowledge catalog (do not edit; `tools/export_std.py`) |
| [`schema/rose_schema.sql`](schema/rose_schema.sql) | MariaDB 11.8 corpus schema (`rose_*`, `VECTOR(1024)` + HNSW) |
| [`rose/`](rose) | compiler v1 (`rosec`): parser, unit checker, solve, tables, Python codegen, corpus access |
| [`tools/`](tools) | corpus importers (Wikidata, CODATA, OEIS) and embedding |
| [`tests/`](tests) | self-test: positive programs and negative programs per diagnostic code |
| [`TODO.md`](TODO.md) | open tasks and rules for contributors (humans and LLMs) |
| [`examples/`](examples) | `fn`, `law`, `ctrl`, `machine`, `table`, `bio` examples |

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
