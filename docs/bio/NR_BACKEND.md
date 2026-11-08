# Building the local NCBI nr backend (DIAMOND)

Rose answers bio tasks that need a homology search (`bio:search.blastp`, `bio:search.blastx`) through a
**local** copy of NCBI nr searched with [DIAMOND](https://github.com/bbuchfink/diamond) – never NCBI
online BLAST (concept §5.7). Rose does not ship or host this database: it is large, changes daily and
can be built by anyone from public NCBI data. This page says how, with the figures measured on the
reference installation. Reference implementation of the whole backend (pipeline, job queue, API,
SQL schema): [gerontec/blastDiamond](https://github.com/gerontec/blastDiamond).

Not every bio task needs this: GO terms, sequence statistics, format conversion or the Biopython
functions do not; counting questions ("how many sequences of taxon X since …") are plain SQL on the
metadata (`bio:meta.count`), not a search.

## What you need (measured, reference installation, 2026-09 to 2026-11)

| Item | Size / figure | Note |
|---|---|---|
| NCBI nr, BLAST v5 format (download) | 176 volumes; `nr.000` alone 51 GB; 857 GB unpacked | needed to build the DIAMOND database and, until replaced, to fetch residues by accession (`blastdbcmd`) |
| DIAMOND database `nr_full.dmnd` | **463 GB** | about 120 GB of it are the full merged sequence titles; shortening titles to accessions on a rebuild saves most of that |
| Disk | NVMe recommended for the `.dmnd`; ~1.4 TB in total while both formats exist | searches read the database in blocks |
| RAM | searches planned within min(48 GB, available − 4 GB) | `--block-size` 2 … 0.1 chosen per search from the measured peak memory of earlier searches |
| SQL database | accession, taxon, length, creation date per sequence | for pre-selection and counting |
| DIAMOND version | 2.2.8 for the first build; `makedb --append` for daily updates is in DIAMOND master since 2026-10-21 ([PR #991](https://github.com/bbuchfink/diamond/pull/991)) | the `.dmnd` format is tied to the DIAMOND version |
| Time for the first `makedb` | not recorded on the reference installation | plan for many hours |

## Steps

1. **Download** nr in BLAST v5 format from NCBI (`update_blastdb.pl --decompress nr`, or the NCBI FTP /
   cloud open-data copies). Keep the shared LMDB files (`nr.pdb`, `.pos`, `.pot`, `.ptf`, `.pto`,
   `nr.pal`): they come only with `nr.000`, and `blastdbcmd` fails on the other volumes without them.
2. **Taxonomy**: download `taxdump` (and `prot.accession2taxid`) from NCBI; refresh every ~30 days.
3. **Build the DIAMOND database**: export the sequences (`blastdbcmd -entry all`) and run
   `diamond makedb --in nr.fasta --db nr_full --taxonmap … --taxonnodes … --taxonnames …`.
4. **Metadata into SQL**: one row per accession with taxon, length and creation date – the creation
   date comes from the GenBank/RefSeq daily files, not from nr itself.
5. **Daily delta** instead of rebuilding: GenBank and RefSeq daily updates, `pdb_seqres`,
   UniProt/Swiss-Prot, appended with `diamond makedb --append`. RefSeq daily files reach back only
   about 21 days – a pipeline that stops for longer leaves a gap that must be filled from a full release.

   Measured duration (33 daily runs, 2026-10-03 to 2026-11-08, 15.0 million new sequences in total;
   median 153 846 new per run, from 269 to 3.85 million on a catch-up day):

   | Step | Median | Range | Scales with new sequences? |
   |---|---|---|---|
   | whole run | **12.7 min** | 6.4–21.6 min | barely: about 12 min fixed + 2 min per million new |
   | duplicate check against a hash cache of all sequences (merge) | 8.2 min | 4.5–15.9 min | no – it works on the cache of all ~1.17 billion sequences |
   | download + parse of the daily files | 2.6 min | 0.1–7.2 min | a little |
   | `diamond makedb --append` | 1.6 min | 1.1–2.3 min | barely (84 s for 3.85 million new) |
   | metadata into SQL (one transaction) | 0.3 min | 0–1.9 min | yes, about 29 µs per new sequence |

   The fixed part dominates, so a daily run costs about the same whether 300 or 3 million
   sequences arrive; the duplicate check over the whole cache is the step to optimise first (for
   example: keep a daily hash delta and merge it weekly). 10 of 43 scheduled starts failed, almost all
   on TLS handshake timeouts at NCBI; nothing is lost – the open daily files are caught up by the next
   run – but plan for delays of up to two days and retry the same day.
6. **Search in two stages** (what makes it usable):
   - pre-select in SQL by taxon (with sub-taxa), length range and creation date → a small partial
     `.dmnd` (cached);
   - search it with `--dbsize` set to the size of the **full** nr, so that E-values stay comparable to a
     search of the whole database.
   Measured: sequences of the last 90 days (2.5 million) – **1.8 s instead of 895 s** for the full
   database; an ultra-sensitive search over 100 days – 1.88 GB RAM, 46 s.
7. **Run searches through one job queue**, not directly: the queue owns the memory planning, so that
   parallel searches do not exhaust RAM.

## What Rose expects from a backend

| Rose unit | Backend operation |
|---|---|
| `bio:meta.count`, `bio:meta.taxon` | SQL on the metadata, no search |
| `bio:seq.get(acc, range?)` | residues by accession from the local copy (no `efetch`) |
| `bio:search.blastp` / `blastx` | a job in the queue: pre-selection, then DIAMOND with `--dbsize` of the full nr; a search without any filter is an error (`E602`) unless `scope all_nr` is stated |

Generated code never calls `diamond` itself.
