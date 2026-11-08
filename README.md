# Rose

**Search before you write.** Rose is a concept for a small, LLM-optimised programming
language. Instead of re-inventing solved problems, an LLM *references* verified building
blocks – algorithms from [Rosetta Code](https://rosettacode.org), mathematical facts,
physical laws, controllers and state machines – and writes only the glue. A MCP server
finds the blocks, checks the result (types, physical units, contracts, exhaustive
tables and state machines) and compiles it to Python, C, IEC 61131-3 ST or ESPHome C++.

> Status: **concept (M0)**. No compiler, no MCP server, no corpus imported yet.

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
| [`docs/KONZEPT.md`](docs/KONZEPT.md) | full concept (German): principles, language, corpus sources and licences, verification levels, MCP integration, benchmark and go/no-go rule, roadmap |
| [`spec/grammar.ebnf`](spec/grammar.ebnf) | grammar draft v0 |
| [`spec/mcp-tools.md`](spec/mcp-tools.md) | MCP tool specification and diagnostic codes |
| [`schema/rose_schema.sql`](schema/rose_schema.sql) | MariaDB 11.8 corpus schema (`rose_*`, `VECTOR(1024)` + HNSW) |
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
