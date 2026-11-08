# MCP server `rose` – tool specification (draft)

Transport: stdio (e.g. over `ssh -T <host> rose-mcp`), optional streamable HTTP.
Reference deployment: 192.168.5.23.
Storage: tables `rose_*` (see [`schema/rose_schema.sql`](../schema/rose_schema.sql)).
Embeddings: bge-m3 (1024 dimensions) via an OpenAI-compatible endpoint (`ROSE_EMBED_URL`).

Design rules

- Filtering, ranking, type and unit matching happen **in SQL on the server**, never in the model.
- Responses are small: a result list returns *signature cards*, not code. Default `k = 5`, max `k = 10`.
- Every result carries `level` and `license` so the model can prefer verified, permissive units.
- All errors are JSON objects with `code`, `message`, optional `fix`.

## Signature card (common result shape)

```json
{
  "ref": "rc:Sieve_of_Eratosthenes",
  "kind": "algo",
  "name": "Sieve of Eratosthenes",
  "intent": "all primes up to limit",
  "signature": "(limit: Int{>= 2}) -> List[Int]",
  "dims": null,
  "level": "cross_checked",
  "targets": ["python", "c", "st"],
  "license": "GFDL-1.3-or-later",
  "score": 0.81
}
```

## Tools

| Tool | Input | Output |
|---|---|---|
| `rose.search` | `query: str`, `kind?: algo\|math\|law\|const\|model\|ctrl\|machine\|table\|bio`, `target?: str`, `min_level?: str`, `license?: any\|permissive`, `k?: int` | list of signature cards |
| `rose.match_signature` | `signature: str` (Rose type, e.g. `"(Real[W], Real[K]) -> Real[kg/s]"`), `kind?`, `k?` | list of signature cards, exact dimension match first |
| `rose.get` | `ref: str`, `with?: [source, tests, provenance, deps]` | card + requested parts (Rose source, test vectors, origin URL, dependencies) |
| `rose.examples` | `ref: str`, `lang: str`, `k?: int` | implementations in that language with `level`, `license`, `source_url` (only tool that returns foreign code) |
| `rose.law_solve` | `ref: str`, `unknown: str`, `given?: {sym: quantity}` | closed form, dimension check, validity range; numeric value if all givens are set |
| `rose.check` | `source: str`, `file?: str` | `{ok: bool, diagnostics: [...]}` (codes E1xx–E5xx, R2xx) |
| `rose.compile` | `source: str`, `target: python\|c\|st\|esphome`, `license?: any\|permissive`, `self_contained?: bool` | `{code, lock, diagnostics}`; `lock` = pinned refs with hash, level, license |
| `rose.test` | `source: str`, `target?: str` | test results from the sandbox (no network, MemoryMax, ≤ 20 s) |
| `rose.submit` | `source: str`, `author: str`, `note?: str` | `{submission_id, status: staged}`; promoted only after green `rose.test` |
| `rose.explain` | `code: str` | explanation and example fix for a diagnostic code |

## Diagnostic codes (initial set)

| Code | Name | Meaning |
|---|---|---|
| E101 | syntax | parse error with expected tokens |
| E201 | unit-mismatch | incompatible units in an expression |
| E202 | missing-unit | numeric literal where a quantity is required |
| E203 | affine-temperature | `degC + degC` or similar |
| E301 | unknown-ref | `use` target not in corpus (with `did_you_mean`) |
| E302 | no-impl-for-target | unit has no implementation for the target |
| E303 | license-excluded | unit excluded by `--license permissive` |
| E304 | self-reference | `--self-contained`: the task itself is imported |
| E410 | ctrl-without-sample-time | `ctrl` without `sample` |
| E411 | unbounded-output | `ctrl` output without range |
| E501 | nondeterministic | two transitions enabled at once |
| E502 | unreachable-state | state never reached from `initial` |
| E503 | deadlock | reachable state without outgoing transition (and not final) |
| E511 | table-incomplete | input combination without rule (with counterexample) |
| E512 | table-overlap | input combination matched by > 1 rule under `hit unique` |
| E601 | remote-blast | NCBI online BLAST / `qblast` used; replace with `bio:search` (local DIAMOND nr) |
| E602 | unfiltered-nr-search | `bio:search` without taxon/length/new_days filter and without `scope all_nr` |
| E603 | charset-join | utf8mb4 accession joined on `blast_acc.acc` (ascii) without `CONVERT(... USING ascii)` |
| R201 | known-solution | hand-written body resembles a corpus unit |
| R202 | lower-level-chosen | a higher-level unit with the same signature exists |
| R203 | local-data-available | sequence downloaded (efetch/UniProt) although it is in the local nr |
| R204 | masked-residues | residues from the .dmnd may contain X runs (makedb masking) |

## Bio units: local DIAMOND shortcut

`kind = bio` never creates a new search path. The compiler maps it onto a local DIAMOND copy of
NCBI nr with its metadata in SQL (reference implementation:
[gerontec/blastDiamond](https://github.com/gerontec/blastDiamond)):

| Unit | Compiles to |
|---|---|
| `bio:meta.*` (accession, taxon, lineage, count, new since) | SQL on the sequence metadata |
| `bio:seq.get` | residues from the local database (offset table) |
| `bio:search.blastp` / `blastx` | a job in the backend's queue, two-stage: SQL pre-selection → sub-database → DIAMOND with `--dbsize` of the full nr |

Generated code never calls `diamond` directly, so the backend's memory planning stays the only one.
