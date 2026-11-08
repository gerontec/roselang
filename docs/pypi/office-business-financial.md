# Office/Business / Financial

[Index](README.md) · 78 packages in this topic, 16 more listed under another topic, by downloads.

### statsmodels

Statistical computations and models for Python

`pip install statsmodels` · installs (wheel) · licence: BSD-3-Clause · rank 570 · last release 2026-08-30 · [PyPI](https://pypi.org/project/statsmodels/) · [docs](https://www.statsmodels.org/stable/index.html) · [source](https://github.com/statsmodels/statsmodels)

<details><summary>README extract</summary>

statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

The documentation for the latest release is at


The documentation for the development version is at


Recent improvements are highlighted in the release notes ...

Sections: About statsmodels, Documentation, Main Features, How to get it, Getting the latest code, Bug Reports

</details>

### gspread

Google Spreadsheets Python API

`pip install gspread` · installs (wheel) · licence: MIT License · rank 600 · last release 2025-05-14 · [PyPI](https://pypi.org/project/gspread/) · [docs](https://gspread.readthedocs.io/en/latest/) · [source](https://github.com/burnash/gspread)

<details><summary>README extract</summary>

Simple interface for working with Google Sheets.

Features:

- Open a spreadsheet by title, key or URL.
- Read, write, and format cell ranges.
- Sharing and access control.
- Batching updates.

Example:
```python
import gspread

# First you need access to the Google API. Based on the route you
# chose in Step 1, call either service_account(), oauth() or api_key().
gc = gspread.service_account()

# Open a sheet from a spreadsheet in one go
wks = gc.open("Where is the money Lebowski?").sheet1

# Update a range of cells using the top left corner address
...
```

...

</details>

### yfinance

Download market data from Yahoo! Finance API

`pip install yfinance` · installs (wheel) · licence: Apache Software License · rank 924 · last release 2026-11-03 · [PyPI](https://pypi.org/project/yfinance/) · [docs](https://ranaroussi.github.io/yfinance) · [source](https://github.com/ranaroussi/yfinance)

<details><summary>README extract</summary>

yfinance offers a Pythonic way to fetch financial & market data from Yahoo!Ⓡ finance.

> [!IMPORTANT]
> Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of Yahoo, Inc.
> yfinance is not affiliated, endorsed, or vetted by Yahoo, Inc. ...

Sections: Download market data from Yahoo! Finance's API, Main components, Legal Stuff, P.S.

</details>

### python-stdnum

Python module to handle standardized numbers and codes

`pip install python-stdnum` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 1639 · last release 2026-01-04 · [PyPI](https://pypi.org/project/python-stdnum/) · [docs](https://arthurdejong.org/python-stdnum/doc/) · [source](https://github.com/arthurdejong/python-stdnum/)

_README extract left out: share-alike licence._

### numpy-financial

Simple financial functions

`pip install numpy-financial` · installs (wheel) · licence: BSD-3-Clause · rank 1730 · last release 2026-09-15 · [PyPI](https://pypi.org/project/numpy-financial/)

<details><summary>README extract</summary>

The `numpy-financial` package contains a collection of elementary financial
functions.

The financial functions in NumPy
are deprecated and eventually will be removed from NumPy; see
NEP-32
for more information. This package is the replacement for the original
NumPy financial functions.

The source code for this package is available at ...

Example:
```python
>>> import numpy_financial as npf
>>> npf.irr([-250000, 100000, 150000, 200000, 250000, 300000])
0.5672303344358536
```

</details>

### gspread-dataframe

Read/write gspread worksheets using pandas DataFrames

`pip install gspread-dataframe` · installs (wheel) · licence: MIT License · rank 2381 · last release 2024-06-12 · [PyPI](https://pypi.org/project/gspread-dataframe/)

<details><summary>README extract</summary>

This package allows easy data flow between a worksheet in a Google spreadsheet
and a Pandas DataFrame. Any worksheet you can obtain using the `gspread` package
can be retrieved as a DataFrame with `get_as_dataframe`; DataFrame objects can
be written to a worksheet using `set_with_dataframe`: ...

Example:
```python
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe

worksheet = some_worksheet_obtained_from_gspread_client

df = pd.DataFrame.from_records([{'a': i, 'b': i * 2} for i in range(100)])
set_with_dataframe(worksheet, df)

df2 = get_as_dataframe(worksheet)
```

Sections: gspread-dataframe, Formatting Google worksheets for DataFrames, Requirements, From PyPI, From GitHub

</details>

### ccxt

A cryptocurrency trading API with more than 100 exchanges in JavaScript / TypeScript / Python / C# / PHP / Go

`pip install ccxt` · installs (wheel) · licence: MIT · rank 2620 · last release 2026-11-04 · [PyPI](https://pypi.org/project/ccxt/) · [docs](https://github.com/ccxt/ccxt/wiki)

<details><summary>README extract</summary>

Example:
```python
import ccxt
print(ccxt.exchanges) # print a list of all available exchange classes
```

Sections: CCXT Terminal, See Also, Prediction Market Exchanges, Builder Code Exchanges, JavaScript (NPM), JavaScript (for use with the `` tag), Python, PHP, .net/C, Go, Java, Rust, Docker, Usage

</details>

### numbers-parser

Read and write Apple Numbers spreadsheets

`pip install numbers-parser` · installs (wheel) · licence: MIT · rank 3225 · last release 2026-11-04 · [PyPI](https://pypi.org/project/numbers-parser/) · [docs](https://github.com/masaccio/numbers-parser/blob/main/README.md) · [source](https://github.com/masaccio/numbers-parser)

<details><summary>README extract</summary>

`numbers-parser` is a Python module for reading and editing Apple Numbers`.numbers` files. It supports Numbers files generated by Numbers versions 3.x and later. It is tested against Numbers documents from 10.0 through to 14.4 (the last version of Numbers) and Numbers Creator Studio up to version 15.1, which the most current as of February 2026. ...

Example:
```python
>>> from numbers_parser import Document
>>> doc = Document("mydoc.numbers")
>>> sheets = doc.sheets
>>> tables = sheets[0].tables
>>> rows = tables[0].rows()
```

Sections: numbers-parser, Quick Start, Cell Data, Writing Numbers Documents, Styles, Cell Data Formatting, Borders, API, Command-line scripts, cat-numbers, csv2numbers, Deleting columns, Renaming columns, Date columns

</details>

### pygsheets

Google Spreadsheets Python API v4

`pip install pygsheets` · installs (wheel) · licence: MIT License · rank 3377 · last release 2022-11-30 · [PyPI](https://pypi.org/project/pygsheets/)

<details><summary>README extract</summary>

A simple, intuitive library for google sheets which gets your work done.

Features:

* Open, create, delete and share spreadsheets using _title_ or _key_
* Intuitive models - spreadsheet, worksheet, cell, datarange
* Control permissions of spreadsheets. ...

Example:
```python
import pygsheets
import numpy as np

gc = pygsheets.authorize()

# Open spreadsheet and then worksheet
sh = gc.open('my new sheet')
wks = sh.sheet1

# Update a cell with value (just to let him know values is updated ;) )
wks.update_value('A1', "Hey yank this numpy array")
my_nparray = np.random.randint(10, size=(3, 4))

...
```

...

</details>

### py-moneyed

Provides Currency and Money classes for use in your Python code.

`pip install py-moneyed` · installs (wheel) · licence: BSD License · rank 3484 · last release 2022-11-27 · [PyPI](https://pypi.org/project/py-moneyed/) · [docs](https://py-moneyed.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Features:
The need to represent instances of money frequently arises in software
development, particularly any financial/economics software. ...

Example:
```python
from moneyed import Money, USD

five_dollars = Money(5, USD)
```

Sections: Overview, Quick start

</details>

### smartsheet-python-sdk

Library that uses Python to connect to Smartsheet services (using API 2.0).

`pip install smartsheet-python-sdk` · installs (wheel) · licence: Apache-2.0 · rank 3694 · last release 2026-08-12 · [PyPI](https://pypi.org/project/smartsheet-python-sdk/)

<details><summary>README extract</summary>

A library for connecting to the Smartsheet API from Python applications.

The SDK is compatible with actively supported Python versions `3.10`, `3.9`, `3.8`, `3.7`.

Example:
```python
import smartsheet

smart = smartsheet.Smartsheet()             # Create a Smartsheet client

response = smart.Sheets.list_sheets()       # Call the list_sheets() function and store the response object
sheetId = response.data[0].id               # Get the ID of the first sheet in the response
...
```

Sections: Smartsheet Python SDK, Requirements, Getting Started, Documentation, Advanced Topics

</details>

### schwifty

IBAN parsing and validation

`pip install schwifty` · installs (wheel) · licence: MIT · rank 3812 · last release 2026-11-05 · [PyPI](https://pypi.org/project/schwifty/) · [docs](https://schwifty.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

`schwifty` is a Python library that lets you easily work with IBANs and BICs
as specified by the ISO. IBAN is the International Bank Account Number and BIC
the Business Identifier Code. Both are used for international money transfer.

Features:
`schwifty` lets you

* validate check-digits and the country specific format of IBANs
* validate the national check digits of the BBAN for more than 20 countries
* validate format and country codes from BICs
* generate BICs from country and ...

Sections: Gotta get schwifty with your IBANs, Features, Versioning, Project Information, Name

</details>

### databento

Official Python client library for Databento

`pip install databento` · installs (wheel) · licence: Apache-2.0 · rank 3946 · last release 2026-11-03 · [PyPI](https://pypi.org/project/databento/) · [docs](https://databento.com/docs) · [source](https://github.com/databento/databento-python)

<details><summary>README extract</summary>

The official Python client library for Databento.

Key features include:
- Fast, lightweight access to both live and historical data from multiple markets.
- Multiple schemas such as MBO, MBP, top of book, OHLCV, last sale, and more.
- Fully normalized, i.e. ...

Example:
```python
import databento as db

client = db.Historical('YOUR_API_KEY')
data = client.timeseries.get_range(
    dataset='GLBX.MDP3',
    symbols='ES.FUT',
    stype_in='parent',
    start='2022-06-10T14:30',
    end='2022-06-10T14:40',
)

data.replay(callback=print)  # market replay, with `print` as event handler
```

Sections: databento-python, Documentation, Requirements, Building from source, Usage

</details>

### edgartools

Python library to access and analyze SEC Edgar filings, XBRL financial statements, 10-K, 10-Q, and 8-K reports

`pip install edgartools` · installs (wheel) · licence: MIT · rank 4016 · last release 2026-10-23 · [PyPI](https://pypi.org/project/edgartools/) · [docs](https://dgunning.github.io/edgartools/) · [source](https://github.com/dgunning/edgartools)

<details><summary>README extract</summary>

EdgarTools is a Python library for accessing SEC EDGAR filings as structured data. Parse financial statements, insider trades, fund holdings, proxy statements, and 20+ other filing types with a consistent Python API — in a few lines of code. Free and open source.

Features:
SEC EDGAR has every filing back to 1994, free — and almost none of it is ready to use. EdgarTools turns any filing into a typed Python object, so a 10-K's revenue is one line instead of an afternoon of XBRL parsing.

 Financial Statements ...

Example:
```python
from edgar import *
set_identity("your.name@example.com")
```

...

</details>

### gspread-formatting

Complete Google Sheets formatting support for gspread worksheets

`pip install gspread-formatting` · installs (wheel) · licence: MIT License · rank 4068 · last release 2025-03-07 · [PyPI](https://pypi.org/project/gspread-formatting/)

<details><summary>README extract</summary>

This package provides complete cell formatting for Google spreadsheets
using the popular `gspread` package, along with a few related features such as setting
"frozen" rows and columns in a worksheet. Both basic and conditional formatting operations
are supported. ...

Example:
```python
from gspread_formatting import *

fmt = cellFormat(
    backgroundColor=color(1, 0.9, 0.9),
    textFormat=textFormat(bold=True, foregroundColor=color(1, 0, 1)),
    horizontalAlignment='CENTER'
    )

format_cell_range(worksheet, 'A1:J1', fmt)
```

...

</details>

### iso4217

ISO 4217 currency data package for Python

`pip install iso4217` · installs (wheel) · licence: Public Domain · rank 4083 · last release 2026-03-03 · [PyPI](https://pypi.org/project/iso4217/)

<details><summary>README extract</summary>

This Python package contains ISO 4217 currency data, represented as
enum module which was introduced in 3.4.

>>> from iso4217 import Currency
>>> Currency.USD
<Currency.USD: 'USD'>
>>> Currency.USD.code
'USD'
>>> Currency.USD.currency_name
'US Dollar'
>>> Currency.USD.exponent # USD has cents
>>> Currency.JPY
<Currency.JPY: 'JPY'>
>>> ...

</details>

### pyxirr

Rust-powered collection of financial functions for Python.

`pip install pyxirr` · installs (wheel) · licence: The Unlicense (Unlicense) · rank 4377 · last release 2025-11-03 · [PyPI](https://pypi.org/project/pyxirr/)

<details><summary>README extract</summary>

Rust-powered collection of financial functions.

PyXIRR stands for "Python XIRR" (for historical reasons), but contains many other financial functions such as IRR, FV, NPV, etc.

Features:

- correct
- supports different day count conventions (e.g. ACT/360, 30E/360, etc.) ...

Example:
```python
from datetime import date
from pyxirr import xirr

dates = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]
amounts = [-1000, 750, 500]

# feed columnar data
xirr(dates, amounts)
# feed iterators
xirr(iter(dates), (x / 2 for x in amounts))
# feed an iterable of tuples
xirr(zip(dates, amounts))
# feed a dictionary
...
```

...

</details>

### xlutils

Utilities for working with Excel files that require both xlrd and xlwt

`pip install xlutils` · installs (wheel) · licence: MIT License · rank 4576 · last release 2016-06-09 · [PyPI](https://pypi.org/project/xlutils/)

<details><summary>README extract</summary>

This package provides a collection of utilities for working with Excel
files. Since these utilities may require either or both of the xlrd
and xlwt packages, they are collected together here, separate from either
package.

Currently available are:

xlutils.copy
 Tools for copying xlrd.Book objects to xlwt.Workbook objects. ...

Sections: xlutils, Documentation, Problems?, Licensing

</details>

### QuantLib

Python bindings for the QuantLib library

`pip install QuantLib` · installs (wheel) · licence: BSD-3-Clause · rank 4601 · last release 2026-10-13 · [PyPI](https://pypi.org/project/QuantLib/)

<details><summary>README extract</summary>

QuantLib ( is a free/open-source C++ library
for financial quantitative analysts and developers, aimed at providing
a comprehensive software framework for quantitative finance.

QuantLib is Non-Copylefted Free Software and OSI Certified Open Source Software. ...

</details>

### xlwings

Make Excel fly: Interact with Excel from Python and vice versa.

`pip install xlwings` · installs (wheel) · licence: BSD License · rank 4673 · last release 2026-10-23 · [PyPI](https://pypi.org/project/xlwings/) · [docs](https://docs.xlwings.org) · [source](https://github.com/xlwings/xlwings)

<details><summary>README extract</summary>

xlwings is a BSD-licensed Python library that makes it easy to call Python from Excel and vice versa:

* Scripting: Automate/interact with Excel from Python using a syntax that is close to VBA.
* Macros: Replace your messy VBA macros with clean and powerful Python code.
* UDFs: Write User Defined Functions (UDFs) in Python (Windows only). ...

Sections: xlwings - Make Excel fly with Python!, xlwings (Open Source), xlwings Lite, xlwings PRO, Links

</details>

### sec-api

SEC EDGAR Filings API

`pip install sec-api` · installs (wheel) · licence: MIT License · rank 4682 · last release 2026-04-13 · [PyPI](https://pypi.org/project/sec-api/) · [docs](https://sec-api.io/docs) · [source](https://github.com/sec-api-io/sec-api-python)

<details><summary>README extract</summary>

- 20+ million EDGAR filings and 100+ million exhibits — from license agreements, investor presentations, and other Reg FD disclosures, over insider trading, credit & bond agreements, bylaws, IPOs, secondaries & shelf offerings, M&A terms, government contracts, audit reports, SEC enforcement actions, AAERs, and executive employment agreements to ...

Features:
EDGAR Filing Search & Download APIs

- SEC Filing Search API
- Full-Text Search API
- Real-Time Filing Stream API
- Download API - Download any SEC filing, exhibit and attached file
- PDF Generator API - Download SEC filings and exhibits as PDF ...

Example:
```python
from sec_api import DownloadApi

# 200+ requests / second per account
downloadApi = DownloadApi(api_key="YOUR_API_KEY")

filing_url = "

...

</details>

### ib_async

Python sync/async framework for Interactive Brokers API

`pip install ib_async` · installs (wheel) · licence: Other/Proprietary License · rank 4737 · last release 2025-12-08 · [PyPI](https://pypi.org/project/ib_async/) · [source](https://github.com/ib-api-reloaded/ib_async)

<details><summary>README extract</summary>

<!-- --> <!-- -->

Features:
* Simple and Intuitive: Write straightforward Python code without dealing with callback complexity
* Automatic Synchronization: The IB component stays in sync with TWS/Gateway automatically
* Async-Ready: Built on asyncio and eventkit for ...

Example:
```python
from ib_async import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)
# Your code here
ib.disconnect()
```

Sections: ib_async, Update, Introduction, What You Can Build, Key Features, Build Manually, Generate Docs, Check Types, Build Package, Upload Package (if maintaining), Setup Interactive Brokers, 1. Download IB Gateway or TWS, 2. Configure API Access, 3. Performance Settings

</details>

### TA-Lib

Python wrapper for TA-Lib

`pip install TA-Lib` · installs (wheel) · licence: not stated · rank 5010 · last release 2026-10-28 · [PyPI](https://pypi.org/project/TA-Lib/)

<details><summary>README extract</summary>

<!-- Badges -->

This is a Python wrapper for TA-LIB based on Cython
instead of SWIG. From the homepage:

> TA-Lib is widely used by trading software developers requiring to perform
> technical analysis of financial market data.
> * Includes 150+ indicators such as ADX, MACD, RSI, Stochastic, Bollinger
> Bands, etc. ...

Example:
```python
>>> import talib
>>> import numpy as np
>>> c = np.random.randn(100)

# this is the library function
>>> k, d = talib.STOCHRSI(c)

# this produces the same result, calling STOCHF
>>> rsi = talib.RSI(c)
>>> k, d = talib.STOCHF(rsi, rsi, rsi)

# you might want this instead, calling STOCH
>>> rsi = talib.RSI(c)
>>> k, d = talib.STOCH(rsi, rsi, rsi)
```

...

</details>

### nautilus-trader

Production-grade Rust-native trading engine with deterministic event-driven architecture

`pip install nautilus-trader` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 5353 · last release 2026-08-02 · [PyPI](https://pypi.org/project/nautilus-trader/) · [docs](https://nautilustrader.io/docs) · [source](https://github.com/nautechsystems/nautilus_trader)

_README extract left out: share-alike licence._

### dj-stripe

Django + Stripe made easy

`pip install dj-stripe` · installs (wheel) · licence: MIT · rank 5376 · last release 2026-06-26 · [PyPI](https://pypi.org/project/dj-stripe/) · [docs](https://dj-stripe.dev/dj-stripe/) · [source](https://github.com/dj-stripe/dj-stripe)

<details><summary>README extract</summary>

Stripe Models for Django.

dj-stripe implements all of the Stripe models, for Django. Set up your
webhook endpoint and start receiving model updates. You will then have
a copy of all the Stripe models available in Django models, as soon as
they are updated!

The full documentation is available on Read the Docs.

Features:
- Stripe Core
- Stripe Billing
- Stripe Cards (JS v2) and Sources (JS v3)
- Payment Methods and Payment Intents (SCA support)
- Support for multiple accounts and API keys
- Stripe Connect (partial support) ...

Sections: dj-stripe - Django + Stripe Made Easy, Introduction, Features, Requirements, Similar libraries

</details>

### ib-insync

Python sync/async framework for Interactive Brokers API

`pip install ib-insync` · installs (wheel) · licence: BSD License · rank 5491 · last release 2023-07-02 · [PyPI](https://pypi.org/project/ib-insync/)

<details><summary>README extract</summary>

The goal of the IB-insync library is to make working with the
Trader Workstation API
from Interactive Brokers as easy as possible.

The main features are:

* An easy to use linear style of programming;
* An IB component
 that automatically keeps in sync with the TWS or IB Gateway application;
* A fully asynchonous framework based on
 asyncio
 and ...

Example:
```python
from ib_insync import *
# util.startLoop()  # uncomment this line when in a notebook

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

contract = Forex('EURUSD')
bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

...
```

Sections: Introduction, Example, Documentation, Discussion, Disclaimer

</details>

### mplfinance

Utilities for the visualization, and visual analysis, of financial data

`pip install mplfinance` · installs (wheel) · licence: BSD License · rank 6122 · last release 2023-08-02 · [PyPI](https://pypi.org/project/mplfinance/)

<details><summary>README extract</summary>

matplotlib utilities for the visualization, and visual analysis, of financial data

Example:
```python
import pandas as pd
daily = pd.read_csv('examples/data/SP500_NOV2019_Hist.csv',index_col=0,parse_dates=True)
daily.index.name = 'Date'
daily.shape
daily.head(3)
daily.tail(3)
```

Sections: mplfinance, The New API, Basic Usage, Old API availability

</details>

### pandas-ta

A Comprehensive Python 3 Technical Analysis Library with Pandas Dataframe Extension for Quantitative Researchers, Traders, and Investors.

`pip install pandas-ta` · installs (wheel) · licence: not stated · rank 6252 · last release 2025-09-14 · [PyPI](https://pypi.org/project/pandas-ta/) · [docs](https://www.pandas-ta.dev/api) · [source](https://github.com/twopirllc/pandas-ta)

<details><summary>README extract</summary>

A popular and comprehensive Technical Analysis Library in Python 3 that leverages _numba_ and _numpy_ for accuracy and performance, and _pandas_ for simplicity and bulk processing. The library contains more than 150 indicators and utilities as well as 60 Candlestick Patterns when TA Lib is installed. ...

Sections: Pandas TA, Details

</details>

### factur-x

Factur-X and Order-X: electronic invoicing and ordering standards

`pip install factur-x` · installs (wheel) · licence: BSD License · rank 6503 · last release 2026-10-30 · [PyPI](https://pypi.org/project/factur-x/) · [source](https://github.com/akretion/factur-x)

<details><summary>README extract</summary>

Factur-X is a Franco-German e-invoicing standard which complies with the European e-invoicing standard EN 16931. The Factur-X specifications are available on the FNFE-MPE website in English and French. The Factur-X standard is also called ZUGFeRD 2.x in Germany. ...

Example:
```python
from facturx import generate_from_file

generate_from_file(regular_pdf_file, xml_file)
```

Sections: Factur-X / Order-X / UBL Python library, Usage, Use hatch, Execute the test, Command line tools, Tutorial: generate a Factur-X invoice under Windows, Webservice

</details>

### quantstats

Portfolio analytics for quants

`pip install quantstats` · installs (wheel) · licence: Apache-2.0 · rank 6531 · last release 2026-09-27 · [PyPI](https://pypi.org/project/quantstats/) · [docs](https://github.com/ranaroussi/quantstats) · [source](https://github.com/ranaroussi/quantstats)

<details><summary>README extract</summary>

QuantStats Python library that performs portfolio profiling, allowing quants and portfolio managers to understand their performance better by providing them with in-depth analytics and risk metrics.

Changelog »

1. `quantstats.stats` - for calculating various performance metrics, like Sharpe ratio, Win rate, Volatility, etc.
2. ...

Example:
```python
%matplotlib inline
import quantstats as qs

# extend pandas functionality with metrics, etc.
qs.extend_pandas()

# fetch the daily returns for a stock
stock = qs.utils.download_returns('META')

# show sharpe ratio
qs.stats.sharpe(stock)

# or using extend_pandas() :)
stock.sharpe()
```

...

</details>

### vectorbt

Python library for backtesting and analyzing trading strategies at scale

`pip install vectorbt` · installs (wheel) · licence: not stated · rank 6535 · last release 2026-10-19 · [PyPI](https://pypi.org/project/vectorbt/)

<details><summary>README extract</summary>

简体中文 / English |
 Features ·
 Installation ·
 Examples ·
 Links

VectorBT takes a radically different approach to backtesting: instead of looping through bars one strategy at a time, it packs thousands of configurations into NumPy arrays, accelerates the hot path with Numba and Rust, and runs them all at once, turning hours of grid search into ...

Features:
Fast, vectorized backtesting

 Research strategies at scale with pandas, NumPy, and Numba.

 Optional Rust engine

 Use precompiled kernels for supported operations without JIT compilation.

 Pandas-native API ...

Example:
```python
import vectorbt as vbt

data = vbt.YFData.download("BTC-USD")
price = data.get("Close")

pf = vbt.Portfolio.from_holding(price, init_cash=100)
print(pf.total_profit())
```

...

</details>

### sec-edgar-downloader

Download SEC filings from the EDGAR database using Python

`pip install sec-edgar-downloader` · installs (wheel) · licence: MIT License · rank 6836 · last release 2026-02-02 · [PyPI](https://pypi.org/project/sec-edgar-downloader/) · [docs](https://sec-edgar-downloader.readthedocs.io) · [source](https://github.com/jadchaar/sec-edgar-downloader)

<details><summary>README extract</summary>

sec-edgar-downloader is a Python package for downloading company filings from the SEC EDGAR database.
Searches can be conducted either by stock ticker or Central Index Key (CIK).
You can use the SEC CIK lookup tool if you cannot find an appropriate ticker.

Example:
```python
from sec_edgar_downloader import Downloader

# Initialize a downloader instance. Download filings to the current
# working directory. Must declare company name and email address
# to form a user-agent string that complies with the SEC Edgar's
# programmatic downloading fair access policy.
# More info:
...
```

Sections: sec-edgar-downloader, Quick Start, Basic Usage, Advanced Usage, Documentation

</details>

### energyquantified

Energy Quantified Time series API client.

`pip install energyquantified` · installs (wheel) · licence: Apache Software License · rank 6977 · last release 2026-10-26 · [PyPI](https://pypi.org/project/energyquantified/) · [docs](https://energyquantified-python.readthedocs.io) · [source](https://github.com/energyquantified/eq-python-client)

<details><summary>README extract</summary>

Documentation |
Python package |
GitHub repository

The Python library for Energy Quantified's
Time Series API. It allows you to access thousands of data series directly from
Energy Quantified's time series database. It integrates with the popular
pandas library and the polars
libarary for high-performance data analysis and manipulation. ...

Features:
- Simple authentication
- Metadata caching
- Rate-limiting and automatic retries on network errors
- Full-text search and keyword search for curves and powerplants
- Forecasts- and time series data
- Period-based data ...

Example:
```python
from datetime import date, timedelta
from energyquantified import EnergyQuantified

# Initialize client
eq = EnergyQuantified(api_key='<insert api key here>')

...

</details>

### asciichartpy

Nice-looking lightweight console ASCII line charts ╭┈╯ with no dependencies

`pip install asciichartpy` · installs (wheel) · licence: MIT License · rank 7679 · last release 2020-08-17 · [PyPI](https://pypi.org/project/asciichartpy/)

<details><summary>README extract</summary>

Console ASCII line charts in pure Javascript (for NodeJS and browsers) with no dependencies. This code is absolutely free for any usage, you just do whatever the fuck you want.

Sections: asciichart, Usage, NodeJS, Browsers, Options, Scale To Desired Height, Auto-range, Multiple Series, Colors, See Also, Ports, Future work (coming soon, hopefully)

</details>

### ironcalc

Create, edit and evaluate Excel spreadsheets

`pip install ironcalc` · installs (wheel) · licence: Apache Software License; MIT License · rank 8001 · last release 2026-10-21 · [PyPI](https://pypi.org/project/ironcalc/) · [source](https://github.com/ironcalc/ironcalc)

### rustpy-xlsxwriter

High-performance Excel and CSV file generation powered by Rust (~7-9x faster)

`pip install rustpy-xlsxwriter` · installs (wheel) · licence: MIT License · rank 8074 · last release 2026-11-07 · [PyPI](https://pypi.org/project/rustpy-xlsxwriter/) · [source](https://github.com/rahmadafandi/rustpy-xlsxwriter)

<details><summary>README extract</summary>

High-performance Excel and CSV file generation for Python, powered by Rust. ~7x-9x faster than XlsxWriter, ~5x faster CSV (records) than Python's `csv` module, and ~12x faster Pandas DataFrame → CSV than `pandas.to_csv` via zero-copy Arrow. ...

Features:
Data Sources
- List of dicts, generators/iterators, Pandas DataFrame, Polars DataFrame
- All Python types: `str`, `int`, `float`, `bool`, `None`, `datetime`, `date`
- Numpy scalar types (`numpy.int64`, `numpy.float64`, `numpy.bool`) ...

Example:
```python
from rustpy_xlsxwriter import FastExcel

# One line
FastExcel("report.xlsx").sheet("Sheet1", records).save()

# Or with options
(
    FastExcel("report.xlsx")
    .format(float_format="0.00", bold_headers=True)
    .freeze(row=1)
    .sheet("Users", users)
    .sheet("Orders", orders)
...

</details>

### backtesting

Backtest trading strategies in Python

`pip install backtesting` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 8125 · last release 2026-07-22 · [PyPI](https://pypi.org/project/backtesting/) · [docs](https://kernc.github.io/backtesting.py/doc/backtesting/) · [source](https://github.com/kernc/backtesting.py/)

_README extract left out: share-alike licence._

### fiscalyear

Utilities for managing the fiscal calendar

`pip install fiscalyear` · installs (wheel) · licence: MIT License · rank 8197 · last release 2022-02-17 · [PyPI](https://pypi.org/project/fiscalyear/)

<details><summary>README extract</summary>

Features:
fiscalyear is a small, lightweight Python module providing helpful utilities for managing the fiscal calendar. It is designed as an extension of the built-in datetime and calendar modules, adding the ability to query the fiscal year, fiscal quarter, ...

Example:
```python
>>> from fiscalyear import *
>>> a = FiscalYear(2017)
>>> a.start
FiscalDateTime(2016, 10, 1, 0, 0)
>>> a.end
FiscalDateTime(2017, 9, 30, 23, 59, 59)
>>> a.isleap
False
```

Sections: Overview, Basic Usage, FiscalYear, FiscalQuarter, FiscalMonth, FiscalDay, FiscalDateTime, FiscalDate, Documentation

</details>

### pandas-ta-classic

Technical Analysis Indicators - Pandas TA Classic is an easy to use Python 3 Pandas Extension with a comprehensive collection of indicators and TA-Lib patterns.

`pip install pandas-ta-classic` · installs (wheel) · licence: MIT · rank 8205 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pandas-ta-classic/) · [docs](https://xgboosted.github.io/pandas-ta-classic/) · [source](https://github.com/xgboosted/pandas-ta-classic.git)

<details><summary>README extract</summary>

> Pandas TA Classic is an easy-to-use library that leverages the Pandas package with 224 indicators and utility functions and 62 native candlestick patterns (284 total unique — no TA-Lib required). ...

Features:
- 284 Unique Indicators & Patterns: 224 Category indicators + 62 CDL patterns via `cdl_pattern()` = 284 unique (doji and inside appear in both counts; all CDL patterns use native Python — no TA-Lib required) ...

Example:
```python
import pandas as pd
import pandas_ta_classic as ta

# Load your data
df = pd.read_csv("path/to/symbol.csv")
# OR fetch OHLCV with yfinance directly (pandas-ta-classic does not fetch data;
# see examples/fetch_market_data.py):
# import yfinance as yf
# df = yf.download("AAPL", period="1y")

# Calculate indicators
...
```

...

</details>

### kiteconnect

The official Python client for the Kite Connect trading API

`pip install kiteconnect` · installs (wheel) · licence: MIT License · rank 8331 · last release 2026-09-15 · [PyPI](https://pypi.org/project/kiteconnect/)

<details><summary>README extract</summary>

The official Python client for communicating with the Kite Connect API.

Kite Connect is a set of REST-like APIs that expose many capabilities required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (WebSockets), and more, with the simple HTTP API collection. ...

Example:
```python
import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="your_api_key")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
...
```

...

</details>

### pyxero

Python API for accessing the REST API of the Xero accounting tool.

`pip install pyxero` · installs (wheel) · licence: BSD-3-Clause · rank 8420 · last release 2025-06-04 · [PyPI](https://pypi.org/project/pyxero/) · [source](https://github.com/freakboy3742/pyxero)

<details><summary>README extract</summary>

PyXero is a Python API for accessing the REST API provided by the Xero
accounting tool. It allows access to both Public, Private and Partner applications.

Example:
```python
from xero import Xero
from xero.auth import OAuth2PKCECredentials
from xero.constants import XeroScopes

# Get client_id, client_secret from config file or settings then
credentials = OAuth2PKCECredentials(
    client_id, port=8080,
    scope=[XeroScopes.OFFLINE_ACCESS, XeroScopes.ACCOUNTING_CONTACTS,
...
```

Sections: PyXero, Quickstart, Using OAuth2 Credentials, Using PKCE Credentials, CLI OAuth2 App Example, Older authentication methods, Using the Xero API, Payroll, Projects, Under the hood, Filter operator

</details>

### backtrader

BackTesting Engine

`pip install backtrader` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 8805 · last release 2023-04-19 · [PyPI](https://pypi.org/project/backtrader/)

_README extract left out: share-alike licence._

### gspread-pandas

A package to easily open an instance of a Google spreadsheet and interact with worksheets through Pandas DataFrames.

`pip install gspread-pandas` · installs (wheel) · licence: BSD License · rank 8884 · last release 2026-08-12 · [PyPI](https://pypi.org/project/gspread-pandas/)

<details><summary>README extract</summary>

Features:
A package to easily open an instance of a Google spreadsheet and
interact with worksheets through Pandas DataFrames. It enables you to
easily pull data from Google spreadsheets into DataFrames as well as
push data into spreadsheets from DataFrames. ...

Example:
```python
import pandas as pd
from gspread_pandas import Spread, Client

file_name = "
df = pd.read_csv(file_name)

# 'Example Spreadsheet' needs to already exist and your user must have access to it
spread = Spread('Example Spreadsheet')
# This will ask to authenticate if you haven't done so before

# Display available worksheets
spread.sheets

...
```

Sections: Getting Started, Overview, Working with messy sheets, Optional: better matching with a model, Client Credentials, Example, Troubleshooting

</details>

### skfolio

Portfolio optimization, factor model construction, and risk management built on top of scikit-learn

`pip install skfolio` · installs (wheel) · licence: BSD License · rank 9116 · last release 2026-11-06 · [PyPI](https://pypi.org/project/skfolio/) · [docs](https://skfolio.org) · [source](https://github.com/skfolio/skfolio)

<details><summary>README extract</summary>

|CI/CDDownloadsRuffContributionWebsiteJupyterLiteDiscordDOI|

skfolio is a Python library for portfolio optimization, factor model construction,
and risk management built on top of scikit-learn. It offers a unified interface and
tools compatible with scikit-learn to build, fine-tune, cross-validate, and stress-test
portfolio models. ...

Example:
```python
from sklearn import set_config
from sklearn.model_selection import (
    GridSearchCV,
    KFold,
    RandomizedSearchCV,
    train_test_split,
)
from sklearn.pipeline import Pipeline
from scipy.stats import loguniform

from skfolio import RatioMeasure, RiskMeasure
from skfolio.datasets import (
    load_factors_dataset,
    load_sp500_dataset,
...
```

...

</details>

### thetadata

Python client library for ThetaData market data APIs

`pip install thetadata` · installs (wheel) · licence: Apache-2.0 · rank 9139 · last release 2026-10-30 · [PyPI](https://pypi.org/project/thetadata/) · [source](https://github.com/AXIOMXLLC/python_library)

<details><summary>README extract</summary>

Python client library for accessing ThetaData market data APIs over gRPC.

This package provides a `ThetaClient` for querying US stock, option, and index market data from ThetaData. Results can be returned as either Polars or Pandas DataFrames.

Features:
- Direct client access to ThetaData services
- Stock, option, and index endpoints
- Return data as Polars or Pandas DataFrames
- Built-in response decompression
- Simple authentication with a credentials file or explicit credentials

Example:
```python
from thetadata import ThetaClient

client = ThetaClient()
```

...

</details>

### metatrader5

API Connector to MetaTrader 5 Terminal

`pip install metatrader5` · does not install on CPython 3.14 · licence: MIT License · rank 9165 · last release 2026-09-27 · [PyPI](https://pypi.org/project/metatrader5/) · [docs](https://www.mql5.com/en/docs/integration/python_metatrader5)

<details><summary>README extract</summary>

MetaTrader is a multi-asset platform for trading in the Forex market and stock exchanges.
In addition to the basic trading functionality which enables access to financial markets, the platform provides powerful
tools for analyzing vast amounts of price data. ...

</details>

### wolfxl

Openpyxl-compatible Excel library with a Rust backend: speed up openpyxl code with one import change and edit .xlsx templates without losing formatting, conditional formatting, or data validation. WolfXL 2.0.21 measured 6.7-12.0x faster than openpyxl 3.1.5 on the committed read/write benchmark (small-file gains vary). MIT.

`pip install wolfxl` · installs (wheel) · licence: MIT License · rank 9322 · last release 2026-10-31 · [PyPI](https://pypi.org/project/wolfxl/) · [source](https://github.com/SynthGL/wolfxl-oss)

<details><summary>README extract</summary>

Example:
```python
from wolfxl import load_workbook

wb = load_workbook("report.xlsx", modify=True)  # edit the existing file
wb"Summary" = 1500
print(wb.calculate()["Summary!B4"])  # 2450.0 from =SUM(B2:B3)
wb.save("report-updated.xlsx")  # cells you did not touch keep their formatting
wb.close()
```

Sections: Edit an existing workbook, Compared with openpyxl, Performance, measured, Choose the right edition

</details>

### lseg-data

Client for LSEG Data Platform API's

`pip install lseg-data` · installs (wheel) · licence: Apache Software License · rank 9798 · last release 2025-04-04 · [PyPI](https://pypi.org/project/lseg-data/) · [docs](https://developers.lseg.com/en/api-catalog/lseg-data-platform/lseg-data-library-for-python/documentation)

<details><summary>README extract</summary>

The LSEG Data Library for Python provides a set of ease-of-use interfaces offering your applications a uniform access to the breadth and depth of financial data and services available on the Data Platform. ...

Example:
```python
import lseg.data as ld
```

Sections: Some examples..., ... with the Access layer, Import the LSEG Data Library, Open a data session, Get pricing snapshots and fundamental data, Close the session, ... with the Content layer dedicated to advanced use cases, Fundamental And Reference data retrieval, Historical data retrieval, Real-time streaming data retrieval, Search

</details>

### py-vollib

Deprecated transition package for vollib.

`pip install py-vollib` · installs (wheel) · licence: MIT · rank 9941 · last release 2026-06-01 · [PyPI](https://pypi.org/project/py-vollib/) · [source](https://github.com/vollib/py_vollib)

<details><summary>README extract</summary>

`py-vollib` is deprecated. The canonical package name is now `vollib`.

This release intentionally contains no library code. It depends on the official
`vollib` package so existing dependency specifications that still name
`py-vollib` resolve to the maintained package.

New installs should use: ...

</details>

### pyportfolioopt

Financial portfolio optimization in python

`pip install pyportfolioopt` · installs (wheel) · licence: MIT License · rank 10100 · last release 2026-02-26 · [PyPI](https://pypi.org/project/pyportfolioopt/) · [docs](https://pyportfolioopt.readthedocs.io/en/latest/) · [source](https://github.com/pyportfolio/pyportfolioopt)

<details><summary>README extract</summary>

PyPortfolioOpt is a library implementing portfolio optimization methods, including
classical mean-variance optimization, Black-Litterman allocation, or shrinkage and Hierarchical Risk Parity. ...

Features:
In this section, we detail some of PyPortfolioOpt's available functionality. More examples are offered in the Jupyter notebooks here. Another good resource is the tests. ...

Example:
```python
import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

# Read in price data
df = pd.read_csv("tests/resources/stock_prices.csv", parse_dates=True, index_col="date")

# Calculate expected returns and sample covariance
mu = expected_returns.mean_historical_return(df)
...
```

...

</details>

### schwab-py

Unofficial API wrapper for the Schwab HTTP API

`pip install schwab-py` · installs (wheel) · licence: MIT License · rank 10212 · last release 2025-06-30 · [PyPI](https://pypi.org/project/schwab-py/) · [docs](https://schwab-py.readthedocs.io/en/latest/) · [source](https://github.com/alexgolec/schwab-py)

<details><summary>README extract</summary>

`schwab-py` is an unofficial wrapper around the Charles Schwab Consumer APIs.
It strives to be as thin and unopinionated as possible, offering an elegant
programmatic interface over each endpoint. Notable functionality includes: ...

Features:
`schwab-py` was designed to provide a few important pieces of functionality:

1. Safe Authentication: Schwab's API supports OAuth authentication, but too
 many people online end up rolling their own implementation of the OAuth
 callback flow. ...

Example:
```python
from schwab import auth, client
import json

api_key = 'YOUR_API_KEY'
app_secret = 'YOUR_APP_SECRET'
callback_url = '
token_path = '/path/to/token.json'

c = auth.easy_client(api_key, app_secret, callback_url, token_path)

r = c.get_price_history_every_day('AAPL')
r.raise_for_status()
...

</details>

### tradingeconomics

Trading Economics API

`pip install tradingeconomics` · installs (wheel) · licence: MIT License · rank 10404 · last release 2026-07-08 · [PyPI](https://pypi.org/project/tradingeconomics/)

<details><summary>README extract</summary>

The Trading Economics Python package provides direct access to over 300,000 economic indicators, exchange rates, stock market indexes, government bond yields, and commodity prices. This package offers various request methods to query the Trading Economics databases and supports exporting data in XML, CSV, or JSON format. ...

Sections: Trading Economics API, Authentication, Sample Usage, GitHub Examples, Documentation

</details>

### py-vollib-vectorized

A fast, vectorized approach to calculating Implied Volatility and Greeks using the Black, Black-Scholes and Black-Scholes-Merton pricing.

`pip install py-vollib-vectorized` · installs (wheel) · licence: MIT License · rank 10472 · last release 2021-02-28 · [PyPI](https://pypi.org/project/py-vollib-vectorized/)

<details><summary>README extract</summary>

The `py_vollib_vectorized` package makes pricing thousands of option contracts and calculating greeks fast and effortless.
It is built on top of the `py_vollib` library.
Upon import, it will automatically patch the corresponding `py_vollib` functions so as to support vectorization. ...

Example:
```python
# The usual py_vollib syntax

import numpy as np
import pandas as pd

import py_vollib.black_scholes
flag = 'c'  # 'c' for call, 'p' for put
S = 100  # Underlying asset price
K = 90  # Strike
t = 0.5  # (Annualized) time-to-expiration
r = 0.01  # Interest free rate
iv = 0.2  # Implied Volatility

...
```

Sections: py_vollib_vectorized, Introduction, Requirements, Code samples, Patching `py_vollib`, Utility functions, Benchmarking

</details>

### vollib

Python library for calculating option prices, implied volatility and greeks.

`pip install vollib` · installs (wheel) · licence: MIT License · rank 11277 · last release 2026-06-01 · [PyPI](https://pypi.org/project/vollib/) · [source](https://github.com/vollib/py_vollib)

<details><summary>README extract</summary>

`vollib` is a python library for calculating option prices, implied volatility and greeks. At its core is Peter Jaeckel's source code for `LetsBeRational`, an extremely fast and accurate algorithm for obtaining Black's implied volatility from option prices. ...

Example:
```python
from vollib.black_scholes import black_scholes
```

Sections: vollib, Input domain, Migration from py_vollib, Implied volatility from option price, Dependencies, About the reference Python implementation, About "Let's be Rational", Links

</details>

### alpha-vantage

Python module to get stock data from the Alpha Vantage Api

`pip install alpha-vantage` · installs (wheel) · licence: MIT License · rank 11673 · last release 2024-07-18 · [PyPI](https://pypi.org/project/alpha-vantage/)

<details><summary>README extract</summary>

*Python module to get stock data/cryptocurrencies from the Alpha Vantage API*

Alpha Vantage delivers a free API for real time financial data and most used finance indicators in a simple json or pandas format. This module implements a python interface to the free API provided by Alpha Vantage. ...

Example:
```python
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='YOUR_API_KEY')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
```

Sections: alpha_vantage, News, Usage, Data frame structure, Plotting, Time Series, Technical indicators, Crypto currencies., Foreign Exchange (FX), Examples, Tests, Documentation, TODOs, Contact

</details>

### ks-xlsx-parser

Production-grade Excel Workflow Parser for RAG + auditability systems

`pip install ks-xlsx-parser` · installs (wheel) · licence: MIT License · rank 11712 · last release 2026-05-19 · [PyPI](https://pypi.org/project/ks-xlsx-parser/) · [docs](https://github.com/knowledgestack/ks-xlsx-parser#readme) · [source](https://github.com/knowledgestack/ks-xlsx-parser)

<details><summary>README extract</summary>

ks-xlsx-parser — the open-source Python library that parses Excel (.xlsx) files into citation-ready JSON for LLMs, RAG pipelines, and AI agents (LangChain, LangGraph, CrewAI, OpenAI Agents SDK, Claude, MCP).

> [!TIP]
> `.xlsx` → structured, typed, citation-ready JSON that an LLM can actually reason about. ...

Example:
```python
from ks_xlsx_parser import parse_workbook

result = parse_workbook(path="q4_forecast.xlsx")

# LLM-ready chunks with citation URIs
for chunk in result.chunks:
    print(chunk.source_uri)          # q4_forecast.xlsx#Revenue!A1:F18
    print(chunk.token_count)         # 412
    print(chunk.render_text[:200])   # Pipe-delimited Markdown-ish text
...
```

...

</details>

### technical

Technical Indicators for Financial Analysis

`pip install technical` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 12096 · last release 2026-07-21 · [PyPI](https://pypi.org/project/technical/)

_README extract left out: share-alike licence._

### sec-parser

Parse SEC EDGAR HTML documents into a tree of elements that correspond to the visual structure of the document.

`pip install sec-parser` · installs (wheel) · licence: MIT License · rank 12238 · last release 2024-06-09 · [PyPI](https://pypi.org/project/sec-parser/) · [source](https://github.com/alphanome-ai/sec-parser)

<details><summary>README extract</summary>

Essentials ➔

 Health ➔

 Quality ➔

 Distribution ➔

 Community ➔

 Parse SEC EDGAR HTML documents into a tree of elements that correspond to the visual structure of the document.

 See Demo |
 Read Docs |
 Join Discussions |
 Join Discord

Features:
The `sec-parser` project simplifies extracting meaningful information from SEC EDGAR HTML documents by organizing them into semantic elements and a tree structure. ...

Example:
```python
from sec_downloader import Downloader

# Initialize the downloader with your company name and email
dl = Downloader("MyCompanyName", "email@example.com")

# Download the latest 10-Q filing for Apple
html = dl.get_filing_html(ticker="AAPL", form="10-Q")
```

...

</details>

### ft-pandas-ta

An easy to use Python 3 Pandas Extension with 130+ Technical Analysis Indicators. Can be called from a Pandas DataFrame or standalone like TA-Lib. Correlation tested with TA-Lib.

`pip install ft-pandas-ta` · installs (wheel) · licence: MIT License · rank 12359 · last release 2025-09-29 · [PyPI](https://pypi.org/project/ft-pandas-ta/)

<details><summary>README extract</summary>

An easy to use Python 3 Pandas Extension with 130+ Technical Analysis Indicators. Can be called from a Pandas DataFrame or standalone like TA-Lib. Correlation tested with TA-Lib.

</details>

### longbridge

A Python library for Longbridge Open API

`pip install longbridge` · installs (wheel) · licence: not stated · rank 12388 · last release 2026-10-26 · [PyPI](https://pypi.org/project/longbridge/) · [docs](https://open.longbridge.com/en/docs) · [source](https://github.com/longbridge/openapi)

<details><summary>README extract</summary>

`longbridge` provides an easy-to-use interface for invoking `Longbridge OpenAPI`.

| Context | Description |

| `QuoteContext` | Real-time quotes, candlesticks, options, warrants, watchlists, push subscriptions |
| `TradeContext` | Orders, positions, account balance, executions, cash flow |
| `AssetContext` | Account statement download |
| ...

Example:
```python
from longbridge.openapi import OAuthBuilder, Config

oauth = OAuthBuilder("your-client-id").build(
    lambda url: print(f"Open this URL to authorize: {url}")
)
config = Config.from_oauth(oauth)
```

...

</details>

### smartapi-python

Angel Broking openApi integration

`pip install smartapi-python` · installs (wheel) · licence: not stated · rank 12395 · last release 2025-02-07 · [PyPI](https://pypi.org/project/smartapi-python/)

<details><summary>README extract</summary>

SMARTAPI-PYTHON is a Python library for interacting with Angel's Trading platform ,that is a set of REST-like HTTP APIs that expose many capabilities required to build stock market investment and trading platforms. It lets you execute orders in real time..

Example:
```python
# package import statement
from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp
from logzero import logger

api_key = 'Your Api Key'
username = 'Your client code'
pwd = 'Your pin'
smartApi = SmartConnect(api_key)
try:
    token = "Your QR value"
    totp = pyotp.TOTP(token).now()
except Exception as e:
...
```

Sections: SMARTAPI-PYTHON, Usage

</details>

### xlcalculator

Converts MS Excel formulas to Python and evaluates them.

`pip install xlcalculator` · installs from source (sdist only) · licence: MIT License · rank 12475 · last release 2023-02-06 · [PyPI](https://pypi.org/project/xlcalculator/)

<details><summary>README extract</summary>

xlcalculator is a Python library that reads MS Excel files and, to the extent
of supported functions, can translate the Excel functions into Python code and
subsequently evaluate the generated Python code. Essentially doing the Excel
calculations without the need for Excel.

xlcalculator is a modernization of the
koala2 library. ...

Example:
```python
from xlcalculator.xlfunctions import xl

@xl.register()
@xl.validate_args
def ADDONE(num: xl.Number):
    return num + 1
```

Sections: Excel Calculator, Run tests, Run Example, Adding/Registering Excel Functions, Excel number precision, TODO, Compatibility, Date and Time, Engineering, Financial, Information, Logical, Lookup and reference, Math and Trigonometry

</details>

### python-escpos

Python library to manipulate ESC/POS Printers

`pip install python-escpos` · installs (wheel) · licence: MIT License · rank 12785 · last release 2023-12-17 · [PyPI](https://pypi.org/project/python-escpos/) · [docs](https://python-escpos.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Python ESC/POS is a library which lets the user have access to all those printers handled
by ESC/POS commands, as defined by Epson, from a Python application.

The library tries to implement the functions provided by the ESC/POS-command-set and supports sending text, images,
barcodes and qr-codes to the printer. ...

Example:
```python
from escpos.printer import Usb

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
p = Usb(0x04b8, 0x0202, 0, profile="TM-T88III")
p.text("Hello World\n")
p.image("logo.gif")
p.barcode('4006381333931', 'EAN13', 64, 2, '', '')
p.cut()
```

Sections: Description, Dependencies, Documentation and Usage, Disclaimer

</details>

### varrd

Statistically validated trading edges across futures, equities, and crypto. See which edges are firing, get trade levels, or test any idea with real market data. MCP server + CLI + Python SDK.

`pip install varrd` · installs (wheel) · licence: MIT License · rank 12857 · last release 2026-08-27 · [PyPI](https://pypi.org/project/varrd/) · [docs](https://github.com/varrdinc/varrd#readme) · [source](https://github.com/varrdinc/varrd)

<details><summary>README extract</summary>

The governed live edge layer.

 Statistically validated market behaviors, monitored in real time.

 Web App · MCP Endpoint · PyPI · varrd.com

 Every edge shows exact entry, stop, target, and the full statistical methodology behind it.

 Equity curves, Monte Carlo simulations, regime analysis, edge decay, and full audit trail.

1. Tell your AI. ...

Features:
Finding edges is not hard. Finding non-data-mined edges with proper precautions at every step is much harder.

An LLM by itself will happily write you a backtest, show you a beautiful equity curve, and tell you it has a 70% win rate. ...

Example:
```python
from varrd import VARRD

v = VARRD()

# Browse the edge library
edges = v.edges()                              # free — which markets are firing
...

</details>

### bitcoinlib

Bitcoin cryptocurrency Library

`pip install bitcoinlib` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 12903 · last release 2026-10-03 · [PyPI](https://pypi.org/project/bitcoinlib/)

_README extract left out: share-alike licence._

### lttb

Largest-Triangle-Three-Buckets algorithm for downsampling time series-like data

`pip install lttb` · installs (wheel) · licence: MIT License · rank 12979 · last release 2024-09-06 · [PyPI](https://pypi.org/project/lttb/) · [source](https://git.sr.ht/~javiljoen/lttb-numpy)

<details><summary>README extract</summary>

Numpy implementation of Steinarsson’s *Largest-Triangle-Three-Buckets* algorithm
for downsampling time series–like data
while retaining the overall shape and variability in the data ...

Example:
```python
import numpy as np
import lttb

# Generate an example data set of 100 random points:
# - column 0 represents time values (strictly increasing)
# - column 1 represents the metric of interest: CPU usage, stock price, etc.
data = np.array([range(100), np.random.random(100)]).T

# Downsample it to 20 points:
...
```

Sections: lttb, Usage, Input validation, 0.3.2 / 2024-09-06, 0.3.1 / 2020-10-14, 0.3.0 / 2020-09-15, 0.2.2 / 2020-01-08, 0.2.1 / 2019-11-25, 0.2.0 / 2018-02-11, 0.1.0 / 2017-03-18

</details>

### fintech

The Python Fintech package (SEPA, EBICS & more)

`pip install fintech` · installs (wheel) · licence: Free To Use But Restricted · rank 13074 · last release 2026-10-28 · [PyPI](https://pypi.org/project/fintech/)

<details><summary>README extract</summary>

This package contains all the functionality that is required to work with
EBICS, SEPA and other financial technologies. The usage has been realised
as simple as possible but also as flexible as necessary.

Features:
- Support of EBICS versions 2.4, 2.5 and 3.0
- Support of EBICS websockets
- Direct communication with the bank. No third parties involved.
- Obtain bank account statements (incl. CAMT and MT940 parser) ...

Example:
```python
import fintech
fintech.register()
from fintech.sepa import Account, SEPACreditTransfer

# Create the debtor account from an IBAN
debtor = Account('DE89370400440532013000', 'Max Mustermann')
# Create the creditor account from a tuple (IBAN, BIC)
creditor = Account(('AT611904300234573201', 'BKAUATWW'), 'Maria Musterfrau')
...
```

...

</details>

### mollie-api-python

Mollie API client for Python

`pip install mollie-api-python` · installs (wheel) · licence: BSD License · rank 13119 · last release 2026-04-28 · [PyPI](https://pypi.org/project/mollie-api-python/)

<details><summary>README extract</summary>

Accepting iDEAL, Bancontact/Mister Cash, SOFORT Banking, Creditcard, SEPA Bank transfer, SEPA Direct debit, PayPal, Belfius Direct Net, KBC/CBC, Klarna Pay later/Pay now/Slice it, paysafecard, Giftcards, Giropay, EPS, Przelewy24 and Billie online payments without fixed monthly costs or any punishing registration procedures. ...

Example:
```python
from mollie.api.client import Client
```

Sections: Mollie API client for Python, Requirements, Migration to v3, How to receive payments, Getting started, Retrieving payments, Payment webhook, Multicurrency, Fully integrated iDEAL payments, OAuth2, Initializing via OAuth2, API documentation, Want to help us make our API client even better?

</details>

### xbbg

Independent client for Bloomberg-connected data workflows

`pip install xbbg` · installs (wheel) · licence: Apache-2.0 · rank 13201 · last release 2026-11-04 · [PyPI](https://pypi.org/project/xbbg/) · [docs](https://xbbg.org/) · [source](https://github.com/underloam/xbbg)

<details><summary>README extract</summary>

Python

JavaScript

Rust

Links: Documentation · Quickstart · Configuration · Examples notebook · Contributing · Changelog

Latest release: xbbg==1.8.1 (release: notes)

> This `main` branch is the Rust-powered v1 release. For the legacy pure-Python line, use `release/0.x`.

> Important: xbbg is an independent open-source project. ...

Features:
xbbg's project goal is direct: be the most complete, technically advanced, and performance-focused open-source Bloomberg client for Python workflows, while staying independent of Bloomberg and requiring users to bring their own authorized Bloomberg ...

Example:
```python
from xbbg import blp

# Reference data
prices = blp.bdp(["AAPL US Equity", "MSFT US Equity"], "PX_LAST")

# Historical data
...

</details>

### formualizer

Embeddable spreadsheet engine — parse, evaluate & mutate Excel workbooks at native speed

`pip install formualizer` · installs (wheel) · licence: MIT · rank 13226 · last release 2026-10-25 · [PyPI](https://pypi.org/project/formualizer/) · [docs](https://docs.rs/formualizer) · [source](https://github.com/PSU3D0/formualizer)

<details><summary>README extract</summary>

The fastest open-source spreadsheet engine. Native speed, from Python.

The shared Rust engine calculates a million-formula financial model in 0.26 seconds. See the benchmarks.

Load Excel workbooks, change inputs, recalculate and read results—in-process, with no Excel installation or office-suite service. ...

Features:
| Capability | Description |

| Tokenization | Break formulas into structured `Token` objects with byte spans and operator metadata |
| Parsing | Produce a rich AST with reference normalization, source tracking, and 64-bit structural fingerprints ...

Example:
```python
import formualizer as fz

result = fz.recalculate_xlsx_file("book.xlsx")  # in place
result = fz.recalculate_xlsx_file("book.xlsx", output="calculated.xlsx")
...

</details>

### riskfolio-lib

Portfolio Optimization in Python

`pip install riskfolio-lib` · installs (wheel) · licence: BSD (3-clause) · rank 13258 · last release 2026-11-04 · [PyPI](https://pypi.org/project/riskfolio-lib/) · [docs](https://portfoliooptimization.org)

<details><summary>README extract</summary>

Portfolio Optimization in Python, Easy for Everyone.

Riskfolio-Lib is a library for making Portfolio Optimization in Python made in Peru 🇵🇪. Its objective is to help students, academics and practitioners to build investment portfolios based on mathematically complex models with low effort. ...

Sections: Riskfolio-Lib, Description, Documentation, Choosing a Solver, Dependencies, Citing, RoadMap

</details>

### shioaji

Shioaji — cross-language, cross-platform universal trading API. Native Python bindings, HTTP API with SSE streaming, standalone CLI, and a visual dashboard.

`pip install shioaji` · installs (wheel) · licence: not stated · rank 13313 · last release 2026-11-05 · [PyPI](https://pypi.org/project/shioaji/) · [docs](https://sinotrade.github.io/) · [source](https://github.com/Sinotrade/Shioaji)

<details><summary>README extract</summary>

繁體中文

Shioaji is a trading API provided by Sinopac that offers a comprehensive and user-friendly platform for accessing the Taiwan financial markets. Shioaji is a cross-language, cross-platform universal trading platform — accessible through native Python bindings (`import shioaji as sj`) or any HTTP-capable language (JavaScript/TypeScript, Go, ...

Example:
```python
import shioaji as sj

api = sj.Shioaji()
accounts = api.login(api_key="YOUR_KEY", secret_key="YOUR_SECRET")
api.activate_ca(
    ca_path="/c/your/ca/path/Sinopac.pfx",
    ca_passwd="YOUR_CA_PASSWORD",
)
```

...

</details>

### focus-data-toolkit

Generate provider-realistic FOCUS 1.2/1.3 sample data (AWS, Azure, GCP) and convert it to the four FOCUS 1.4 datasets — strictly from source facts, completed by client supplements including native AWS/Azure/GCP exports — with schema detection, gap analysis, a cross-dataset validation gate and atomic writes.

`pip install focus-data-toolkit` · installs (wheel) · licence: MIT AND CC-BY-4.0 · rank 13849 · last release 2026-10-09 · [PyPI](https://pypi.org/project/focus-data-toolkit/) · [docs](https://github.com/guymano/focus-data-toolkit#readme) · [source](https://github.com/guymano/focus-data-toolkit)

<details><summary>README extract</summary>

Generate realistic FOCUS 1.2 / 1.3 cost and usage data (AWS, Azure, GCP), convert it to
FOCUS 1.4, and validate the result. One dependency-free Python core, usable three ways.

FOCUS is the open standard for cloud cost and usage data. FOCUS 1.4 defines four datasets: Cost and Usage, Contract Commitment, Billing Period, and Invoice Detail. ...

Features:
- Converts FOCUS 1.2/1.3 Cost and Usage into the four FOCUS 1.4 datasets. Values a 1.4 rule
 fixes deterministically are migrated and reported (`FDT-MIG-*`). Values it cannot fix without
 inventing a fact are refused. See docs/conversion-rules.md. ...

Example:
```python
from focus_data_toolkit import convert_files

convert_files("cost_and_usage.csv", "focus-1.4", mode="strict")
```

...

</details>

### finvizfinance

Finviz Finance. Information downloader.

`pip install finvizfinance` · installs (wheel) · licence: MIT License · rank 14094 · last release 2026-08-29 · [PyPI](https://pypi.org/project/finvizfinance/) · [docs](https://finvizfinance.readthedocs.io/en/latest/) · [source](https://github.com/lit26/finvizfinance)

<details><summary>README extract</summary>

finvizfinance is a package which collects financial information from FinViz website. The package provides the information of the following:

- Stock charts, fundamental & technical information, insider information and stock news
- Forex charts and performance
- Crypto charts and performance ...

Example:
```python
from finvizfinance.screener.overview import Overview

foverview = Overview()
filters_dict = {'Index':'S&P 500','Sector':'Basic Materials'}
foverview.set_filter(filters_dict=filters_dict)
df = foverview.screener_view()
df.head()
```

Sections: finvizfinance, Downloads, Quote, Chart, Fundament, Description, Peer, ETF Holders, Outer Ratings, Inside Trader, News, Insider, Example: Overview, Screener (Ticker)

</details>

### beanquery

Customizable lightweight SQL query tool

`pip install beanquery` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 14641 · last release 2025-03-24 · [PyPI](https://pypi.org/project/beanquery/)

_README extract left out: share-alike licence._

### freqtrade-client

Freqtrade - Client scripts

`pip install freqtrade-client` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 14654 · last release 2026-10-30 · [PyPI](https://pypi.org/project/freqtrade-client/) · [docs](https://freqtrade.io)

_README extract left out: share-alike licence._

### freqtrade

Freqtrade - Crypto Trading Bot

`pip install freqtrade` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 14678 · last release 2026-10-30 · [PyPI](https://pypi.org/project/freqtrade/) · [docs](https://freqtrade.io)

_README extract left out: share-alike licence._

### wechatpayv3

微信支付 Python SDK(python sdk for wechatpay)

`pip install wechatpayv3` · installs (wheel) · licence: MIT · rank 14683 · last release 2026-09-11 · [PyPI](https://pypi.org/project/wechatpayv3/)

<details><summary>README extract</summary>

微信支付接口 V3 版 python 库。

欢迎微信支付开发者扫码进 QQ 群(群号：973102221)讨论，欢迎提交代码，欢迎star、follow、fork：

wechatpayv3同时支持微信支付直连模式及服务商模式，接口说明详见官网。

Example:
```python
# 微信支付商户号，服务商模式下为服务商户号，即官方文档中的sp_mchid。
MCHID = '1230000109'

# 商户证书私钥，此文件不要放置在下面设置的CERT_DIR目录里。
with open('path_to_mch_private_key/apiclient_key.pem') as f:
    PRIVATE_KEY = f.read()

# 商户证书序列号
CERT_SERIAL_NO = '444F4864EA9B34415...'

# API v3密钥，
APIV3_KEY = 'MIIEvwIBADANBgkqhkiG9w0BAQE...'

...
```

Sections: 微信支付 API v3 Python SDK, 介绍, 适用对象, 特性, 源码, 安装, 使用方法, 准备, 一个最小的后端, 常见问题, 接口清单, 接口函数参数, 接口函数返回值

</details>

## Also in this topic

- [holidays](file-formats-json.md#holidays) - Open World Holidays Framework
- [streamlit](database-front-ends.md#streamlit) - A faster way to build and share data apps
- [xlwt](database.md#xlwt) - Library to create spreadsheet files compatible with MS Excel 97/2000/XP/2003 XLS files, on any platform, with Python 2.6, 2.7, 3.3+
- [dash](database-front-ends.md#dash) - A Python framework for building reactive web-apps. Developed by Plotly.
- [bokeh](office-business.md#bokeh) - Interactive plots and applications in the browser from Python
- [panel](office-business.md#panel) - The powerful data exploration & web app framework for Python.
- [sigfig](education.md#sigfig) - Python library for rounding numbers (with expected results)
- [weave](database-front-ends.md#weave) - A toolkit for building composable interactive data driven applications.
- [excel-mcp-server](office-business.md#excel-mcp-server) - MCP server for creating, reading and editing Excel workbooks without Microsoft Excel
- [ofxtools](office-business.md#ofxtools) - Library for working with Open Financial Exchange (OFX) data
- [taxjar](office-business.md#taxjar) - Sales tax API client for Python
- [fullbleed](office-business.md#fullbleed) - Deterministic Python PDF engine for reports, invoices, accessible documents, print-ready output, and compiled VDP
- [st-theme](database-front-ends.md#st-theme) - A component that returns the active theme of the Streamlit app.
- [dash-auth](database-front-ends.md#dash-auth) - Dash Authorization Package.
- [gsheets](internet-www-http-2.md#gsheets) - Pythonic wrapper for the Google Sheets API
- [excelrd](office-business.md#excelrd) - Library for developers to extract data from Microsoft Excel (tm) spreadsheet files
