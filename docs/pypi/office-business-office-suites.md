# Office/Business / Office Suites

[Index](README.md) · 8 packages in this topic, 5 more listed under another topic, by downloads.

### python-docx

Create, read, and update Microsoft Word .docx files.

`pip install python-docx` · installs (wheel) · licence: MIT License · rank 258 · last release 2025-06-16 · [PyPI](https://pypi.org/project/python-docx/) · [docs](https://python-docx.readthedocs.org/en/latest/) · [source](https://github.com/python-openxml/python-docx)

<details><summary>README extract</summary>

*python-docx* is a Python library for reading, creating, and updating Microsoft Word 2007+ (.docx) files.

Example:
```python
>>> from docx import Document

>>> document = Document()
>>> document.add_paragraph("It was a dark and stormy night.")
<docx.text.paragraph.Paragraph object at 0x10f19e760>
>>> document.save("dark-and-stormy.docx")

>>> document = Document("dark-and-stormy.docx")
>>> document.paragraphs[0].text
'It was a dark and stormy night.'
```

Sections: python-docx, Example

</details>

### python-pptx

Create, read, and update PowerPoint 2007+ (.pptx) files.

`pip install python-pptx` · installs (wheel) · licence: MIT License · rank 268 · last release 2024-08-07 · [PyPI](https://pypi.org/project/python-pptx/) · [docs](https://python-pptx.readthedocs.io/en/latest/) · [source](https://github.com/scanny/python-pptx)

<details><summary>README extract</summary>

*python-pptx* is a Python library for creating, reading, and updating PowerPoint (.pptx)
files.

A typical use would be generating a PowerPoint presentation from dynamic content such as
a database query, analytics output, or a JSON payload, perhaps in response to an HTTP
request and downloading the generated PPTX file in response. ...

</details>

### docx2pdf

Convert docx to pdf on Windows or macOS directly using Microsoft Word (must be installed).

`pip install docx2pdf` · installs (wheel) · licence: MIT License · rank 5618 · last release 2021-12-11 · [PyPI](https://pypi.org/project/docx2pdf/) · [source](https://github.com/AlJohri/docx2pdf)

<details><summary>README extract</summary>

Convert `docx` to `pdf` on Windows or macOS directly using Microsoft Word (must be installed).

On Windows, this is implemented via `win32com` while on macOS this is implemented via JXA (Javascript for Automation, aka AppleScript in JS).

Example:
```python
from docx2pdf import convert

convert("input.docx")
convert("input.docx", "output.pdf")
convert("my_docx_folder/")
```

Sections: docx2pdf, CLI, Library, Jupyter Notebook

</details>

### python-docx-ml6

Create, read, and update Microsoft Word .docx files. This is a fork from the original library that includes feature requests that have been provided by the open source community but have not yet been merged in the original package.

`pip install python-docx-ml6` · installs (wheel) · licence: MIT License · rank 7642 · last release 2023-11-09 · [PyPI](https://pypi.org/project/python-docx-ml6/) · [docs](https://python-docx.readthedocs.org/en/latest/) · [source](https://github.com/ml6team/python-docx)

<details><summary>README extract</summary>

This package is a fork from the original `python-docx`. It includes feature requests that are yet to be merged in the original one.
*python-docx* is a Python library for reading, creating, and updating Microsoft Word 2007+ (.docx) files.

Example:
```python
>>> from docx import Document

>>> document = Document()
>>> document.add_paragraph("It was a dark and stormy night.")
<docx.text.paragraph.Paragraph object at 0x10f19e760>
>>> document.save("dark-and-stormy.docx")

>>> document = Document("dark-and-stormy.docx")
>>> document.paragraphs[0].text
'It was a dark and stormy night.'
```

Sections: python-docx, Example

</details>

### ezodf

A Python package to create/manipulate OpenDocumentFormat files.

`pip install ezodf` · installs from source (sdist only) · licence: MIT License · rank 7700 · last release 2015-12-14 · [PyPI](https://pypi.org/project/ezodf/)

<details><summary>README extract</summary>

If you want to support us

ezodf is a Python package to create new or open existing OpenDocument
(ODF) files to extract, add, modify or delete document data.

a simple example:
for more examples see: /examples folder

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

Sections: EzODF.py, Abstract, Dependencies, Documentation, NEWS

</details>

### paper-pptx

Create, read, and update PowerPoint 2007+ (.pptx) files.

`pip install paper-pptx` · installs (wheel) · licence: MIT License · rank 9418 · last release 2026-09-23 · [PyPI](https://pypi.org/project/paper-pptx/) · [docs](https://github.com/paper-instruments/paper-pptx) · [source](https://github.com/paper-instruments/paper-pptx)

<details><summary>README extract</summary>

An import-compatible, agent-safe fork of python-pptx for creating and editing PowerPoint presentations without silent corruption.

`paper-pptx` is an import-compatible hard fork of python-pptx for creating and editing PowerPoint (`.pptx`) presentations. ...

Example:
```python
from pptx import Presentation
from pptx.edit import replace_text

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text = "FY25 plan"
prs.save("deck.pptx")

prs = Presentation("deck.pptx")
result = replace_text(prs, "FY25", "FY26")
prs.save("deck-v2.pptx")
print(result.replacements)  # 1
```

Sections: paper-pptx, Quick start, Documentation

</details>

### paper-docx

Create, read, and update Microsoft Word .docx files.

`pip install paper-docx` · installs (wheel) · licence: MIT · rank 9761 · last release 2026-09-23 · [PyPI](https://pypi.org/project/paper-docx/) · [docs](https://github.com/paper-instruments/paper-docx) · [source](https://github.com/paper-instruments/paper-docx)

<details><summary>README extract</summary>

An import-compatible, agent-safe fork of python-docx for creating and editing Word documents without silent corruption.

`paper-docx` is an import-compatible hard fork of python-docx for creating and editing Microsoft Word (`.docx`) documents. ...

Example:
```python
import docx
from docx.package import compare

original = docx.Document()
original.add_paragraph("Payment is due within thirty calendar days.")
original.save("original.docx")

revised = docx.Document()
revised.add_paragraph("Payment is due within thirty business days.")
revised.save("revised.docx")

...
```

Sections: paper-docx, Quick start, Documentation

</details>

### pypptx-with-oxml

Create, read, and update PowerPoint 2007+ (.pptx) files.

`pip install pypptx-with-oxml` · installs (wheel) · licence: MIT License · rank 11801 · last release 2026-01-30 · [PyPI](https://pypi.org/project/pypptx-with-oxml/)

<details><summary>README extract</summary>

A significant experimental feature has been added to enable the parsing of MathML (specifically ``<a14:m>`` elements containing either ``<m:oMathPara>`` for block equations or ``<m:oMath>`` for inline equations) embedded within PowerPoint files. This MathML content can then be converted into LaTeX strings. ...

Sections: python-pptx, More Information

</details>

## Also in this topic

- [python-oxmsg](communications-email.md#python-oxmsg) - Extract attachments from Outlook .msg files.
- [aspose-words](office-business.md#aspose-words) - Aspose.Words for Python is a Document Processing library that allows developers to work with documents in many popular formats without needing Office Automation.
- [aspose-slides](multimedia-graphics.md#aspose-slides) - Aspose.Slides for Python via .NET is a presentation file formats processing library for working with Microsoft PowerPoint files without using Microsoft PowerPoint.
- [streamlit-pdf](multimedia-graphics.md#streamlit-pdf) - A Streamlit component for viewing PDF files
- [pyexcel-ezodf](office-business.md#pyexcel-ezodf) - A Python package to create/manipulate OpenDocumentFormat files
