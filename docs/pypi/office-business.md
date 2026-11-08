# Office/Business

[Index](README.md) · 22 packages in this topic, 19 more listed under another topic, by downloads.

### bokeh

Interactive plots and applications in the browser from Python

`pip install bokeh` · installs (wheel) · licence: BSD-3-Clause · rank 1610 · last release 2026-11-05 · [PyPI](https://pypi.org/project/bokeh/) · [docs](https://docs.bokeh.org) · [source](https://github.com/bokeh/bokeh)

<details><summary>README extract</summary>

Bokeh is an interactive visualization library for modern web browsers. It provides elegant, concise construction of versatile graphics and affords high-performance interactivity across large or streaming datasets. Bokeh can help anyone who wants to create interactive plots, dashboards, and data applications quickly and easily.

 Package

 Project ...

</details>

### odfpy

Python API and tools to manipulate OpenDocument files

`pip install odfpy` · installs from source (sdist only) · licence: Apache Software License; GNU General Public License (GPL); GNU Library or Lesser · rank 1777 · last release 2020-01-18 · [PyPI](https://pypi.org/project/odfpy/)

_README extract left out: share-alike licence._

### cleanco

Python library to process company names

`pip install cleanco` · installs (wheel) · licence: MIT License · rank 3677 · last release 2024-05-15 · [PyPI](https://pypi.org/project/cleanco/)

<details><summary>README extract</summary>

This is a Python package that processes company names, providing cleaned versions of the
names by stripping away terms indicating organization type (such as "Ltd." or "Corp").

Using a database of organization type terms, It also provides an utility to deduce the
type of organization, in terms of US/UK business entity types (ie. ...

Sections: cleanco - clean organization names, What is it / what does it do?, How does it work?, Are there bugs?, Special thanks to

</details>

### panel

The powerful data exploration & web app framework for Python.

`pip install panel` · installs (wheel) · licence: BSD License · rank 3801 · last release 2026-10-23 · [PyPI](https://pypi.org/project/panel/) · [source](https://github.com/holoviz/panel)

<details><summary>README extract</summary>

Panel is an open-source library for interactive dashboards and web apps. Widgets, plots and layouts are ordinary Python objects that you connect to your data and models, pass between functions and classes, and test like the rest of your code. There are no string IDs to match up and no script that reruns on every click. ...

Example:
```python
import numpy as np, panel as pn
import holoviews as hv

pn.extension()

window = pn.ui.IntSlider(label="Window", value=30, start=5, end=90)
sigma  = pn.ui.FloatSlider(label="Volatility", value=1.0, start=0.2, end=3)
ticker = pn.ui.RadioButtonGroup(label="Series", options=["AAPL", "MSFT", "NVDA"])

def series(window, sigma, ticker):
...
```

...

</details>

### xlsx2csv

xlsx to csv converter

`pip install xlsx2csv` · installs (wheel) · licence: MIT License · rank 4265 · last release 2026-01-31 · [PyPI](https://pypi.org/project/xlsx2csv/)

<details><summary>README extract</summary>

> xlsx to csv converter (

Converts xlsx files to csv format.
Handles large XLSX files. Fast and easy to use.

Sections: xlsx2csv, Meta

</details>

### aspose-words

Aspose.Words for Python is a Document Processing library that allows developers to work with documents in many popular formats without needing Office Automation.

`pip install aspose-words` · does not install on CPython 3.14 · licence: Free To Use But Restricted; Other/Proprietary License · rank 4925 · last release 2026-10-13 · [PyPI](https://pypi.org/project/aspose-words/) · [docs](https://docs.aspose.com/words/python-net/)

<details><summary>README extract</summary>

Product Page | Docs | Demos | API Reference | Examples | Blog | Search | Free Support | Temporary License

Try our free online Apps demonstrating some of the most popular Aspose.Words functionality. ...

Example:
```python
import aspose.words as aw

# Create a blank document.
doc = aw.Document()

# Use a document builder to add content to the document.
builder = aw.DocumentBuilder(doc)
# Write a new paragraph in the document with the text "Hello World!".
builder.writeln("Hello, World!")

...
```

Sections: Word API Features, Platform Independence, Get Started, Using Python to Create a DOCX File from Scratch, Using Python to Convert a Word Document to HTML, Using Python to Import PDF and Save as a DOCX File

</details>

### pyx12

HIPAA X12 validator, parser and converter

`pip install pyx12` · installs (wheel) · licence: BSD License · rank 6346 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pyx12/) · [docs](https://pyx12.readthedocs.io/) · [source](https://github.com/azoner/pyx12.git)

<details><summary>README extract</summary>

Pyx12 is a HIPAA X12 document parser, validator and converter. It reads an ANSI X12 data file and validates it against a representation of the X12 Implementation Guidelines. By default, it creates a 997 response for 4010 and a 999 response for 5010. ...

Example:
```python
src = pyx12.x12context.X12ContextReader(param, errh, fd_in)
for datatree in src.iter_segments('2300'):
    # do something with a 2300 claim loop
    # we have access to the 2300 loop and all its children
    for loop2400 in datatree.select('2400'):
        print(loop2400.get_value('SV101'))
        # update something
...
```

Sections: Pyx12, Usage, Code Examples, Where the maps live, Converting a 4010 map to 5010, Adding a new X12 IG, Running the project, Licensing

</details>

### unoserver

A server for file conversions with Libre Office

`pip install unoserver` · installs (wheel) · licence: MIT License · rank 7541 · last release 2026-06-10 · [PyPI](https://pypi.org/project/unoserver/)

<details><summary>README extract</summary>

Using LibreOffice as a server for converting documents.

Features:
Using LibreOffice to convert documents is easy, you can use a command like this to
convert a file to PDF, for example:
However, that will load LibreOffice into memory, convert a file and then exit LibreOffice,
which means that the next time you ...

Sections: unoserver, Overview, Usage, Unoserver, Unoconvert, Unocompare, Unoping, Comparison with `unoconv`, Differences for the user, 3.7 (2026-06-10), 3.6 (2025-11-24), 3.5 (2025-11-18), 3.4 (2025-09-26), 3.3.2 (2025-07-07)

</details>

### excel-mcp-server

MCP server for creating, reading and editing Excel workbooks without Microsoft Excel

`pip install excel-mcp-server` · installs (wheel) · licence: MIT · rank 7901 · last release 2026-10-31 · [PyPI](https://pypi.org/project/excel-mcp-server/) · [docs](https://github.com/haris-musa/excel-mcp-server/blob/main/TOOLS.md)

<details><summary>README extract</summary>

An open-source Model Context Protocol (MCP) server that lets
Claude, Cursor, VS Code Copilot, Codex and other AI clients create, read and edit Excel files:
charts, PivotTables, formulas, tables and more. It is built on `openpyxl`, needs **no Microsoft
Excel**, and runs on Windows, macOS and Linux. ...

Features:
Charts and PivotTables
- Create Excel charts with AI: column, bar, line, area, pie, doughnut, radar, scatter and
 bubble, with combos, secondary axes, trendlines and error bars ...

Sections: Excel MCP Server, Features, Quick start, Choosing which files it can use, Remote use (Streamable HTTP), Docker, Configuration, Tools, Choosing tools, CSV, Writing macros (opt-in), Limitations, Upgrading from 1.x

</details>

### ofxtools

Library for working with Open Financial Exchange (OFX) data

`pip install ofxtools` · installs (wheel) · licence: GPL-3.0-only · rank 8056 · last release 2026-06-12 · [PyPI](https://pypi.org/project/ofxtools/) · [docs](https://ofxtools.readthedocs.io/) · [source](https://github.com/csingley/ofxtools)

_README extract left out: share-alike licence._

### kreuzberg

High-performance document intelligence library for Python. Extract text, metadata, and structured data from PDFs, Office documents, images, and 88+ formats. Powered by Rust core for 10-50x speed improvements.

`pip install kreuzberg` · installs (wheel) · licence: MIT License · rank 8317 · last release 2026-09-21 · [PyPI](https://pypi.org/project/kreuzberg/) · [docs](https://kreuzberg.dev) · [source](https://github.com/kreuzberg-dev/kreuzberg-lts)

<details><summary>README extract</summary>

> [!NOTE]
> Kreuzberg v4 LTS — the long-term-support line for Kreuzberg v4. Active development has moved to
> Xberg (v5+), which receives all new features. This line receives
> critical bug and security fixes until the end of 2026, on a best-effort basis.
> See the migration guide & LTS policy → ...

Example:
```python
import asyncio
from kreuzberg import extract_file

async def main() -> None:
    result = await extract_file("document.pdf")
    print(result.content)

asyncio.run(main())
```

Sections: Python, System Requirements, Quick Start, Basic Extraction, Common Use Cases, Extract with Custom Configuration, Table Extraction, Processing Multiple Files, Async Processing, Next Steps, Features, Office Documents, Images (OCR-Enabled), Web & Data

</details>

### md2pdf

The Markdown to PDF conversion tool with styles

`pip install md2pdf` · installs (wheel) · licence: MIT · rank 9754 · last release 2026-03-31 · [PyPI](https://pypi.org/project/md2pdf/) · [source](https://github.com/jmaupetit/md2pdf)

<details><summary>README extract</summary>

Convert Markdown files to PDF with styles.

Example:
```python
from md2pdf.core import md2pdf

md2pdf(pdf,
       md=None,
       raw=None,
       css=None,
       base_url=None,
       extras=[],
       context={"foo": 1}
)
```

Sections: Usage, As a CLI, As a library, With Docker, Use Jinja templates as input, Hacking, Running the test suite, Ease your life

</details>

### taxjar

Sales tax API client for Python

`pip install taxjar` · installs (wheel) · licence: MIT License · rank 9843 · last release 2025-04-14 · [PyPI](https://pypi.org/project/taxjar/)

### fullbleed

Deterministic Python PDF engine for reports, invoices, accessible documents, print-ready output, and compiled VDP

`pip install fullbleed` · installs (wheel) · licence: MIT · rank 10507 · last release 2026-11-01 · [PyPI](https://pypi.org/project/fullbleed/) · [docs](https://docs.fullbleed.dev/) · [source](https://github.com/fullbleed-engine/fullbleed-official)

<details><summary>README extract</summary>

Generate PDFs from HTML/CSS in Python, Rust, JavaScript, and C#. MIT licensed.

Build invoices, reports, statements, and variable-data print jobs with a deterministic Rust engine. Use the native Rust API, the Python package, or the optional JavaScript and .NET integrations. ...

Features:
- Simple deployment: prebuilt wheels for 15 platform targets, with no browser or system-font installation needed for the bundled workflow. ...

Example:
```python
import fullbleed

engine = fullbleed.PdfEngine(
    page_width="8.5in",
    page_height="11in",
    margin="0.5in",
    pdf_version="1.7",
    pdf_profile="none",
    color_space="rgb",
)

html = "
# Invoice
Hello.
"
css = "body { font-family: sans-serif; }"

bytes_written = engine.render_pdf_to_file(html, css, "output/invoice.pdf")
...
```

...

</details>

### pantab

Converts pandas DataFrames into Tableau Hyper Extracts and back

`pip install pantab` · installs (wheel) · licence: not stated · rank 10598 · last release 2026-04-08 · [PyPI](https://pypi.org/project/pantab/) · [source](https://github.com/innobi/pantab)

<details><summary>README extract</summary>

Official documentation for the project and all of its features is hosted at:

Sections: Getting Help, Documentation, Licensing

</details>

### aspose-cad

Aspose.CAD for Python is a CAD and BIM drawings Processing library that allows developers to modify, convert and publish various drawing and image formats without need to have any other CAD software.

`pip install aspose-cad` · does not install on CPython 3.14 · licence: Free To Use But Restricted; Other/Proprietary License · rank 12148 · last release 2026-07-30 · [PyPI](https://pypi.org/project/aspose-cad/)

<details><summary>README extract</summary>

Aspose.CAD for Python is a standalone class library with Aspose.CAD for .NET under the hood to enhance applications to process, modify, render and publish CAD and BIM drawings without requiring AutoCAD or any other rendering workflow. ...

Example:
```python
from aspose.cad import *
from aspose.cad.imageoptions import *

cadImage = Image.load("drawing.dxf")

rasterizationOptions = CadRasterizationOptions()
rasterizationOptions.page_height = 1600.0
rasterizationOptions.page_width = 1600.0

pdfOptions = PdfOptions()
pdfOptions.vector_rasterization_options = rasterizationOptions

...
```

...

</details>

### dxpdf

A fast DOCX-to-PDF converter powered by Skia, written in Rust

`pip install dxpdf` · installs (wheel) · licence: MIT License · rank 12637 · last release 2026-09-14 · [PyPI](https://pypi.org/project/dxpdf/) · [docs](https://github.com/nerdy-pro/dxpdf#readme) · [source](https://github.com/nerdy-pro/dxpdf)

<details><summary>README extract</summary>

Convert Microsoft Word DOCX files to PDF without Microsoft Office, LibreOffice, or any cloud API.

dxpdf is an open-source, standalone DOCX-to-PDF conversion engine written in Rust and powered by Skia. ...

Features:
- Fast — business documents convert in 55–170 ms depending on how their fonts resolve, a 171-page document in about 420 ms
- High fidelity — parse → resolve → layout → subset → paint pipeline with pixel-accurate baseline positioning ...

Example:
```python
import dxpdf

# Bytes in, bytes out
pdf_bytes = dxpdf.convert(open("input.docx", "rb").read())

# File path to file path
dxpdf.convert_file("input.docx", "output.pdf")

# Customize embedded-image resolution (default 220 DPI)
pdf_bytes = dxpdf.convert(open("input.docx", "rb").read(), image_dpi=300)
...
```

...

</details>

### df2gspread

Export tables to Google Spreadsheets.

`pip install df2gspread` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 12851 · last release 2019-01-03 · [PyPI](https://pypi.org/project/df2gspread/)

_README extract left out: share-alike licence._

### excelrd

Library for developers to extract data from Microsoft Excel (tm) spreadsheet files

`pip install excelrd` · installs (wheel) · licence: BSD License · rank 13169 · last release 2023-07-08 · [PyPI](https://pypi.org/project/excelrd/)

<details><summary>README extract</summary>

`excelrd` is a modified version of xlrd to work for the latest Python versions.
`xlrd` will not work in Python 3.9 or newer versions.

Purpose: Provide a library for developers to use to extract data from Microsoft Excel (tm) spreadsheet files. It is not an end-user tool.

Author: John Machin

Licence: BSD-style (see licences.py) ...

Example:
```python
import excelrd as xlrd
```

Sections: excelrd, Quick start, Transition from xlrd to excelrd, Another quick start, Documentation

</details>

### yandex-cli

Interact with Yandex 360 services (Wiki, Tracker, Forms, …) from a CLI, an MCP server, or a Python SDK.

`pip install yandex-cli` · installs (wheel) · licence: MIT · rank 14220 · last release 2026-10-10 · [PyPI](https://pypi.org/project/yandex-cli/) · [docs](https://ycli.savaznatnov.dev/) · [source](https://github.com/bim-ba/ycli)

<details><summary>README extract</summary>

Yandex 360 for people and for agents.

Tracker, Wiki and Forms from a command line, an MCP server and Python: one tool, and one name for each operation everywhere.

English · Русский

- A command line that scripts well. JSON when piped, ready for `jq`, `--dry-run` for every write, an exit code for each kind of failure. ...

Example:
```python
from ycli.yandex.tracker.client import TrackerClient

tracker = TrackerClient(oauth_token="…", organization_id="…")
print(tracker.issues.get("TRACKER-1").summary)
```

Sections: ycli, Connect your AI client, Use it, Command line, MCP server, Python, Claude Code plugin, Configure, Coverage, Tracker, Wiki, Forms, DataLens, Against the published API

</details>

### pyexcel-ezodf

A Python package to create/manipulate OpenDocumentFormat files

`pip install pyexcel-ezodf` · installs (wheel) · licence: MIT License · rank 14256 · last release 2017-10-23 · [PyPI](https://pypi.org/project/pyexcel-ezodf/)

<details><summary>README extract</summary>

Since T0ha/ezodf was not updated for too long, pyexcel
tries to cover up the holiday period until @T0ha will come back to continue. pyexcel
is happy to push the changes if requested.

If you are a developer and are interested in this project, please apply for co-maintenanceship. ...

Example:
```python
from ezodf import newdoc, Paragraph, Heading, Sheet

odt = newdoc(doctype='odt', filename='text.odt')
odt.body += Heading("Chapter 1")
odt.body += Paragraph("This is a paragraph.")
odt.save()

ods = newdoc(doctype='ods', filename='spreadsheet.ods')
sheet = Sheet('SHEET', size=(10, 10))
ods.sheets += sheet
sheet['A1'].set_value("cell with text")
...
```

Sections: EzODF.py maintained by pyexcel, Maintenance, Abstract, Dependencies, Documentation, NEWS

</details>

### myorb

Personal AI-powered daily briefing dashboard that summarizes your email, calendar, tasks, finances and more.

`pip install myorb` · installs (wheel) · licence: AGPL-3.0-only · rank 14403 · last release 2026-11-07 · [PyPI](https://pypi.org/project/myorb/) · [source](https://github.com/eriktelepovsky/myorb)

_README extract left out: share-alike licence._

## Also in this topic

- [tqdm](desktop-environment.md#tqdm) - Fast, Extensible Progress Meter
- [slack-sdk](communications-chat.md#slack-sdk) - The Slack API Platform SDK for Python
- [xlrd](database.md#xlrd) - Library for developers to extract data from Microsoft Excel (tm) .xls spreadsheet files
- [progressbar2](desktop-environment.md#progressbar2) - A Python Progressbar library to provide visual (yet text based) progress to long running operations.
- [slackclient](communications-chat.md#slackclient) - Slack API clients for Web API and RTM API (Legacy) - Please use https://pypi.org/project/slack-sdk/ instead.
- [pymsteams](internet.md#pymsteams) - Format messages and post to Microsoft Teams.
- [xhtml2pdf](documentation.md#xhtml2pdf) - PDF generator using HTML and CSS
- [shtab](desktop-environment.md#shtab) - Automagic shell tab completion for Python CLI applications
- [SharePlum](internet-www-http.md#shareplum) - Python SharePoint Library
- [python-jobspy](internet-www-http.md#python-jobspy) - JobSpy: job scraper for LinkedIn, Indeed, Glassdoor, ZipRecruiter, Bayt, Naukri, BDJobs & HelloWork
- [workspace-mcp](communications-chat.md#workspace-mcp) - Comprehensive, highly performant Google Workspace Streamable HTTP & SSE MCP Server for Calendar, Gmail, Docs, Sheets, Slides & Drive
- [aspose-slides](multimedia-graphics.md#aspose-slides) - Aspose.Slides for Python via .NET is a presentation file formats processing library for working with Microsoft PowerPoint files without using Microsoft PowerPoint.
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [times](internet.md#times) - Times is a small, minimalistic, Python library for dealing with time conversions between universal time and arbitrary timezones.
- [sharepoint-to-text](communications-email.md#sharepoint-to-text) - Text extraction library for typical file formats found in SharePoint repositories
- [pyStrich](multimedia-graphics.md#pystrich) - PyStrich is a fast pure-Python module to generate 1D and 2D barcodes: Code 39, Code 128 (including GS1-128), EAN-13, ITF-14, Data Matrix (including GS1 Data Matrix), QR Code, PDF417 and Aztec Code.
- [highcharts-core](internet-www-http-2.md#highcharts-core) - High-end Data Visualization for the Python Ecosystem. Official wrapper for Highcharts Core (JS).
- [pyexcel-webio](internet-www-http-2.md#pyexcel-webio) - A generic request and response interface for pyexcel web extensions.
- [endesive](communications-email.md#endesive) - Digital signatures for PDF, S/MIME, XML (XAdES), and CMS in Python.
