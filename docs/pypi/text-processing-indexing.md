# Text Processing / Indexing

[Index](README.md) · 1 packages in this topic, 23 more listed under another topic, by downloads.

### pagefind

Python API for Pagefind

`pip install pagefind` · installs (wheel) · licence: MIT · rank 7424 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pagefind/)

<details><summary>README extract</summary>

An async python API for the pagefind binary.

Example:
```python
import asyncio
import json
import logging
import os
from pagefind.index import PagefindIndex, IndexConfig

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))
log = logging.getLogger(name)
html_content = (
    ""
    "  "
    "    "
    "
# Example HTML
"
    "      This is an example HTML page.
"
    "    "
    "  "
    ""
)

...
```

Sections: `pagefind`, Usage

</details>

## Also in this topic

- [nltk](scientific-engineering.md#nltk) - Natural Language Toolkit
- [snowballstemmer](database.md#snowballstemmer) - This package provides 36 stemmers for 34 languages generated from Snowball algorithms.
- [Sphinx](documentation.md#sphinx) - Python documentation generator
- [jieba](text-processing.md#jieba) - Chinese Words Segmentation Utilities
- [firecrawl-py](internet.md#firecrawl-py) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [xhtml2pdf](documentation.md#xhtml2pdf) - PDF generator using HTML and CSS
- [python-iso639](text-processing.md#python-iso639) - ISO 639 language codes, names, and other associated information
- [stringzilla](file-formats.md#stringzilla) - Search, hash, sort, and process strings faster via SWAR and SIMD
- [jaro-winkler](text-processing.md#jaro-winkler) - Original, standard and customisable versions of the Jaro-Winkler functions.
- [PyStemmer](database.md#pystemmer) - Snowball stemming algorithms, for information retrieval
- [Whoosh](software-development-libraries-2.md#whoosh) - Fast, pure-Python full text indexing, search, and spell checking library.
- [ocrmypdf](scientific-engineering-image-recognition.md#ocrmypdf) - OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched
- [firecrawl](internet.md#firecrawl) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [ir-datasets](text-processing.md#ir-datasets) - provides a common interface to many IR ad-hoc ranking benchmarks, training datasets, etc.
- [phonetics](internet-www-http.md#phonetics) - Compute phonetic key of strings for indexing or fuzzy matching
- [ultimate-sitemap-parser](internet-www-http.md#ultimate-sitemap-parser) - A performant library for parsing and crawling sitemaps
- [nvidia-sphinx-theme](documentation.md#nvidia-sphinx-theme) - A Sphinx theme for NVIDIA projects
- [cpca](text-processing.md#cpca) - Chinese Province, City and Area Recognition Utilities
- [cocoindex](software-development-libraries-3.md#cocoindex) - With CocoIndex, users declare the transformation, CocoIndex creates & maintains an index, and keeps the derived index up to date based on source update, with minimal computation and changes.
- [exomem](scientific-engineering-artificial-intelligence.md#exomem) - Local knowledge substrate for owned markdown/Obsidian vaults, exposed through MCP, REST, and CLI with multimodal OCR/ASR/CLIP search
- [sharepoint-to-text](communications-email.md#sharepoint-to-text) - Text extraction library for typical file formats found in SharePoint repositories
- [pytextrank](scientific-engineering-artificial-intelligence.md#pytextrank) - Python implementation of TextRank as a spaCy pipeline extension, for graph-based natural language work plus related knowledge graph practices; used for for phrase extraction of text documents.
- [Fuzzy](text-processing.md#fuzzy) - Fast Python phonetic algorithms
