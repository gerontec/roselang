# Rose

**Search before you write.** Rose is a concept for a small, LLM-optimised programming
language. Instead of re-inventing solved problems, an LLM *references* verified building
blocks – algorithms from [Rosetta Code](https://rosettacode.org), mathematical facts,
physical laws, controllers and state machines – and writes only the glue. A MCP server
finds the blocks, checks the result (types, physical units, contracts, exhaustive
tables and state machines) and compiles it to Python, C, IEC 61131-3 ST or ESPHome C++.

> Status: **compiler v1 (experimental)**. Corpus imported from Wikidata, CODATA and OEIS;
> compiler handles `fn`, `const`, `use`, `law` + `solve`, `table`, `test` and emits Python.
> Not yet: Rosetta Code import, `machine`/`ctrl`, C/ST/ESPHome targets, MCP server.
> Want to help? See [`TODO.md`](TODO.md).

```sh
python3 tests/run_tests.py                       # offline self-test
ROSE_OFFLINE=1 ./rosec test tests/units_demo.rose
./rosec plan "mass flow of water for 9 kW at 5 K spread"   # needs the corpus
```

```rose
use law:water_heat_flow                      # P = mdot * cp * dT

fn required_flow(p: Real[W], dT: Real[K]) -> Real[kg/s]
  intent "mass flow needed to carry thermal power p at temperature spread dT"
do
  return solve water_heat_flow for mdot given P = p, dT = dT
end

test required_flow(9 kW, 5 K) == 0.430 kg/s within 1 %
```

## Contents

| Path | What |
|---|---|
| [`docs/CONCEPT.md`](docs/CONCEPT.md) | full concept: principles, language, corpus sources and licences, verification levels, MCP integration, benchmark and go/no-go rule, roadmap |
| [`spec/grammar.ebnf`](spec/grammar.ebnf) | grammar draft v0 |
| [`spec/mcp-tools.md`](spec/mcp-tools.md) | MCP tool specification and diagnostic codes |
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
- **Provenance and licences** in `rose.lock`; `--license permissive` excludes
  share-alike sources (Rosetta Code is GFDL).
- **Bio tasks take the local shortcut:** sequence, homology and taxon questions compile onto the
  local DIAMOND nr ([gerontec/blastDiamond](https://github.com/gerontec/blastDiamond)): MariaDB
  pre-selection, then DIAMOND through the existing job queue; online BLAST is a compile error.
- **Measured, not assumed:** the language is dropped if LLM + MCP + Rose does not beat
  LLM + MCP alone.

## Licence

Language, tools and documents: MIT. Corpus data keeps the licence of its source.
