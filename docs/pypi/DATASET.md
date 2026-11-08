# PyPI overview dataset

One compact, LLM-readable record per PyPI project: what it is for, its licence, whether its latest
release installs on CPython 3.14 (Linux x86_64), when it was last released, links, and a cleaned
README extract. Published as release assets of this repository (`pypi-YYYY-MM`), not in the git
history. Built by [`tools/pypi_dataset.py`](../../tools/pypi_dataset.py); background and size
estimate in [`docs/CONCEPT.md` §6.1](../CONCEPT.md).

## Files

- `pypi-<a…z, 0…9, _>.jsonl.gz` – one JSON object per line, projects grouped by the first character
  of their normalised name, sorted by name
- `STATS.md` – counts of this build (projects, installable, with README extract, by year of the
  last release)

## Fields

| Field | Meaning |
|---|---|
| `name`, `version` | project name and latest version as on PyPI |
| `summary`, `keywords` | as the project published them |
| `topics` | Trove `Topic ::` classifiers, levels joined with ` / ` |
| `license` | SPDX `License-Expression`, else the licence classifiers, else a short `License` field |
| `share_alike` | `true` for GPL-family, CC BY-SA and EUPL licences – such records carry no README extract |
| `requires_python` | as declared |
| `install_cp314` | `wheel` (a wheel matches the tags of CPython 3.14 / Linux x86_64), `sdist` (only a source distribution), absent (does not install) |
| `last_release` | upload date of the latest release (YYYY-MM-DD) |
| `url`, `docs`, `homepage`, `source` | PyPI page and project links |
| `readme` | cleaned README extract, at most 800 characters: opening text, feature list, one code example (not `pip install`), section names. Badges, images, HTML and link targets are removed |
| `error` | metadata that could not be read (the name is kept) |

## How it was made

- Names: PyPI simple index (all projects at the time of the run).
- Records: PyPI JSON API `https://pypi.org/pypi/<name>/json`, one request per project, with a
  shared back-off on HTTP 429/5xx. Removed or quarantined projects (HTTP 404) are left out.
- Nothing is installed or run. "Installs" is decided from file names and `requires_python` with
  `packaging`, not by installing.

## Licences and use

- The metadata is used as each project published it on PyPI; the dataset as a whole has no
  licence of its own beyond that (`LicenseRef-PyPI-metadata`).
- A README extract is a short excerpt of the project's own text and stays under the project's
  licence (field `license`); extracts of share-alike projects are not included.
- The dataset points to packages, it does not vouch for them: many projects are abandoned, and
  PyPI removes malicious ones continually – filter by `last_release`, `install_cp314` and your own
  checks before installing anything.

## Limits

- One snapshot; PyPI changes daily.
- 63 % of projects declare no Topic classifier, so grouping by topic misses many.
- README extracts are produced by rules, not by a model; about 30 % of projects get none (no
  README, too short, share-alike licence, or nothing left after cleaning).
