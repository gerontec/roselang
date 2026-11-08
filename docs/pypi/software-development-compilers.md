# Software Development / Compilers

[Index](README.md) · 63 packages in this topic, 37 more listed under another topic, by downloads.

### pyparsing

pyparsing - Classes and methods to define and execute parsing grammars

`pip install pyparsing` · installs (wheel) · licence: MIT · rank 91 · last release 2026-09-20 · [PyPI](https://pypi.org/project/pyparsing/) · [docs](https://pyparsing-docs.readthedocs.io/en/latest/) · [source](https://github.com/pyparsing/pyparsing.git)

<details><summary>README extract</summary>

The pyparsing module is an alternative approach to creating and
executing simple grammars, vs. the traditional lex/yacc approach, or the
use of regular expressions. The pyparsing module provides a library of
classes that client code uses to construct the grammar directly in
Python code. ...

Example:
```python
from pyparsing import Word, alphas
greet = Word(alphas) + "," + Word(alphas) + "!"
hello = "Hello, World!"
print(hello, "->", greet.parse_string(hello))
```

Sections: PyParsing -- A Python Parsing Module, Introduction, Documentation, AI Instructions, Performance benchmarks

</details>

### numba

compiling Python code using LLVM

`pip install numba` · installs (wheel) · licence: BSD License · rank 387 · last release 2026-10-27 · [PyPI](https://pypi.org/project/numba/)

<details><summary>README extract</summary>

Numba is an open source, NumPy-aware optimizing compiler for Python sponsored
by Anaconda, Inc. It uses the LLVM compiler project to generate machine code
from Python syntax.

Numba can compile a large subset of numerically-focused Python, including many
NumPy functions. ...

Sections: Numba, A Just-In-Time Compiler for Numerical Functions in Python, Demo, Contact

</details>

### tree-sitter

Python bindings to the Tree-sitter parsing library

`pip install tree-sitter` · installs (wheel) · licence: MIT License · rank 480 · last release 2026-06-30 · [PyPI](https://pypi.org/project/tree-sitter/) · [docs](https://tree-sitter.github.io/py-tree-sitter/) · [source](https://github.com/tree-sitter/py-tree-sitter)

<details><summary>README extract</summary>

[](
[](
[](

This module provides Python bindings to the [tree-sitter] parsing library.

Example:
```python
parser = Parser(PY_LANGUAGE)
```

Sections: Python Tree-sitter, Usage, Setup, Basic parsing, Walking syntax trees, Editing, Pattern-matching, Captures, Matches

</details>

### tree-sitter-javascript

JavaScript grammar for tree-sitter

`pip install tree-sitter-javascript` · installs (wheel) · licence: MIT · rank 1022 · last release 2025-09-01 · [PyPI](https://pypi.org/project/tree-sitter-javascript/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

JavaScript and JSX grammar for tree-sitter.

This grammar intends to be a close approximation of the ECMAScript
specification, with some extensions to support JSX syntax. We try to support the
latest version of the spec, though it is possible that some very new features may
not be supported yet.

References ...

</details>

### tree-sitter-python

Python grammar for tree-sitter

`pip install tree-sitter-python` · installs (wheel) · licence: MIT · rank 1102 · last release 2025-09-11 · [PyPI](https://pypi.org/project/tree-sitter-python/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

Python grammar for tree-sitter.

- Python 2 Grammar
- Python 3 Grammar

Sections: tree-sitter-python, References

</details>

### tree-sitter-typescript

TypeScript and TSX grammars for tree-sitter

`pip install tree-sitter-typescript` · installs (wheel) · licence: MIT License · rank 1115 · last release 2024-11-11 · [PyPI](https://pypi.org/project/tree-sitter-typescript/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

TypeScript and TSX grammars for tree-sitter.

Because TSX and TypeScript are actually two different dialects, this module defines two grammars. Require them as follows:

For Javascript files with [flow] type annotations you can use the `tsx` parser.

References

- TypeScript Language Spec

</details>

### tree-sitter-bash

Bash grammar for tree-sitter

`pip install tree-sitter-bash` · installs (wheel) · licence: MIT License · rank 1126 · last release 2025-12-02 · [PyPI](https://pypi.org/project/tree-sitter-bash/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

Bash grammar for tree-sitter.

Sections: tree-sitter-bash, References

</details>

### tree-sitter-c

C grammar for tree-sitter

`pip install tree-sitter-c` · installs (wheel) · licence: MIT License · rank 1298 · last release 2026-04-22 · [PyPI](https://pypi.org/project/tree-sitter-c/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

C grammar for tree-sitter.
Adapted from this C99 grammar.

</details>

### libclang

Clang Python Bindings, mirrored from the official LLVM repo: https://github.com/llvm/llvm-project/tree/main/clang/bindings/python, to make the installation process easier.

`pip install libclang` · installs (wheel) · licence: Apache Software License · rank 1360 · last release 2024-06-30 · [PyPI](https://pypi.org/project/libclang/) · [docs](https://libclang.readthedocs.io) · [source](https://github.com/sighingnow/libclang)

<details><summary>README extract</summary>

The repository contains code taken from the LLVM project, to make it easier to install
clang's python bindings.

The repository copies necessary Python binding files from LLVM repo, adds packaging scripts
to make it a valid Python package and finally uploads the package to pypi. ...

Example:
```python
library_path = os.path.join(os.path.dirname(os.path.realpath(file)), 'native')
```

</details>

### tree-sitter-java

Java grammar for tree-sitter

`pip install tree-sitter-java` · installs (wheel) · licence: MIT License · rank 1407 · last release 2024-12-21 · [PyPI](https://pypi.org/project/tree-sitter-java/)

### tree-sitter-go

Go grammar for tree-sitter

`pip install tree-sitter-go` · installs (wheel) · licence: MIT · rank 1432 · last release 2025-08-29 · [PyPI](https://pypi.org/project/tree-sitter-go/)

### tree-sitter-c-sharp

C# grammar for tree-sitter

`pip install tree-sitter-c-sharp` · installs (wheel) · licence: MIT License · rank 1443 · last release 2026-04-14 · [PyPI](https://pypi.org/project/tree-sitter-c-sharp/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

C# grammar for tree-sitter based upon the Roslyn grammar with changes in order to:

- Deal with differences between the parsing technologies
- Work around some bugs in that grammar
- Handle `#if`, `#else`, `#elif`, `#endif` blocks
- Support syntax highlighting/parsing of fragments
- Simplify the output tree ...

Sections: tree-sitter-c-sharp, References

</details>

### tree-sitter-rust

Rust grammar for tree-sitter

`pip install tree-sitter-rust` · installs (wheel) · licence: MIT License · rank 1444 · last release 2026-03-27 · [PyPI](https://pypi.org/project/tree-sitter-rust/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

Rust grammar for tree-sitter.

Features:
- Speed — When initially parsing a file, `tree-sitter-rust` takes around two to three times
 as long as rustc's hand-written parser. ...

Sections: tree-sitter-rust, Features, References

</details>

### tree-sitter-yaml

YAML grammar for tree-sitter

`pip install tree-sitter-yaml` · installs (wheel) · licence: MIT · rank 1566 · last release 2025-10-07 · [PyPI](https://pypi.org/project/tree-sitter-yaml/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

A tree-sitter parser for YAML files.

- YAML version 1.2

Sections: tree-sitter-yaml, References

</details>

### tree-sitter-cpp

C++ grammar for tree-sitter

`pip install tree-sitter-cpp` · installs (wheel) · licence: MIT License · rank 1755 · last release 2024-11-11 · [PyPI](https://pypi.org/project/tree-sitter-cpp/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

C++ grammar for tree-sitter.

- Hyperlinked C++ BNF Grammar
- EBNF Syntax: C++

Sections: tree-sitter-cpp, References

</details>

### tree-sitter-ruby

Ruby grammar for tree-sitter

`pip install tree-sitter-ruby` · installs (wheel) · licence: MIT License · rank 1915 · last release 2024-11-11 · [PyPI](https://pypi.org/project/tree-sitter-ruby/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

Ruby grammar for tree-sitter.

- AST Format of the Whitequark parser

Sections: tree-sitter-ruby, References

</details>

### tree-sitter-php

PHP grammar for tree-sitter

`pip install tree-sitter-php` · installs (wheel) · licence: MIT · rank 1943 · last release 2026-10-06 · [PyPI](https://pypi.org/project/tree-sitter-php/)

### parsy

Easy-to-use parser combinators, for parsing in pure Python

`pip install parsy` · installs (wheel) · licence: MIT License · rank 2033 · last release 2025-09-12 · [PyPI](https://pypi.org/project/parsy/)

<details><summary>README extract</summary>

Parsy is an easy and elegant way to parse text in Python by combining small
parsers into complex, larger parsers. If it means anything to you, it's a
monadic parser combinator library for LL(infinity) grammars in the spirit of
Parsec, Parsnip, and Parsimmon. But don't worry, it has really good
documentation and it doesn't say things like that! ...

</details>

### tree-sitter-json

JSON grammar for tree-sitter

`pip install tree-sitter-json` · installs (wheel) · licence: MIT License · rank 2306 · last release 2024-11-11 · [PyPI](https://pypi.org/project/tree-sitter-json/)

### tree-sitter-embedded-template

Embedded Template (ERB, EJS) grammar for tree-sitter

`pip install tree-sitter-embedded-template` · installs (wheel) · licence: MIT · rank 2380 · last release 2025-08-29 · [PyPI](https://pypi.org/project/tree-sitter-embedded-template/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

A tree-sitter parser for templating languages like ERB and EJS, in which scripting code can be embedded within text content using the delimiters `<%` and `%>`.

References

- ERB Documentation
- EJS Documentation
- ETLua Documentation
- ETA Documentation

</details>

### tree-sitter-elixir

Elixir grammar for tree-sitter

`pip install tree-sitter-elixir` · installs (wheel) · licence: MIT License · rank 2462 · last release 2026-03-02 · [PyPI](https://pypi.org/project/tree-sitter-elixir/)

<details><summary>README extract</summary>

Elixir grammar for tree-sitter.

Ready for production. Currently used by GitHub itself for source code highlighting and code navigation.

</details>

### cuda-tile

CUDA Tile Compiler

`pip install cuda-tile` · installs (wheel) · licence: Apache-2.0 · rank 2474 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cuda-tile/) · [docs](https://docs.nvidia.com/cuda/cutile-python) · [source](https://github.com/nvidia/cutile-python)

<details><summary>README extract</summary>

<!--- SPDX-FileCopyrightText: Copyright (c) <2025> NVIDIA CORPORATION & AFFILIATES. All rights reserved. -->
<!--- SPDX-License-Identifier: Apache-2.0 -->

cuTile Python is a programming language for NVIDIA GPUs. The official documentation can be found
on docs.nvidia.com,
or built from source located in the docs folder.

Example ...

Example:
```python
# This examples uses CuPy which can be installed via `pip install cupy-cuda13x`
# Make sure cuda toolkit 13.1+ is installed:

import cuda.tile as ct
import cupy
import numpy as np

TILE_SIZE = 16

# cuTile kernel for adding two dense vectors. It runs in parallel on the GPU.
@ct.kernel
def vector_add_kernel(a, b, result):
    block_id = ct.bid(0)
...
```

</details>

### wasmtime

A WebAssembly runtime powered by Wasmtime

`pip install wasmtime` · installs (wheel) · licence: Apache-2.0 WITH LLVM-exception · rank 2545 · last release 2026-10-22 · [PyPI](https://pypi.org/project/wasmtime/) · [docs](https://bytecodealliance.github.io/wasmtime-py/) · [source](https://github.com/bytecodealliance/wasmtime-py)

<details><summary>README extract</summary>

Python embedding of
 Wasmtime

 A Bytecode Alliance project

Example:
```python
from wasmtime import Store, Module, Instance, Func, FuncType

store = Store()
module = Module(store.engine, """
  (module
    (func $hello (import "" "hello"))
    (func (export "run") (call $hello))
  )
""")

def say_hello():
    print("Hello from Python!")
hello = Func(store, FuncType([], []), say_hello)

...
```

Sections: wasmtime-py, Versioning, Usage, Components

</details>

### tree-sitter-kotlin

Kotlin grammar for tree-sitter

`pip install tree-sitter-kotlin` · installs (wheel) · licence: MIT License · rank 2555 · last release 2025-01-09 · [PyPI](https://pypi.org/project/tree-sitter-kotlin/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

Kotlin grammar for tree-sitter.

- Kotlin Grammar

Sections: tree-sitter-kotlin, References

</details>

### tree-sitter-swift

Swift grammar for tree-sitter

`pip install tree-sitter-swift` · installs (wheel) · licence: MIT License · rank 2602 · last release 2026-10-04 · [PyPI](https://pypi.org/project/tree-sitter-swift/)

<details><summary>README extract</summary>

This contains a `tree-sitter` grammar for the Swift programming language.

Example:
```python
let mut parser = tree_sitter::Parser::new();
parser.set_language(tree_sitter_swift::language())?;

// ...

let tree = parser.parse(&my_source_code, None)
    .ok_or_else(|| /* error handling code */)?;
```

Sections: tree-sitter-swift, Getting started, Rust, Javascript, Editing the grammar, Using tree-sitter-swift in Web Assembly, Frequently asked questions, Where is your `parser.c`?

</details>

### tree-sitter-powershell

A Powershell grammar for tree-sitter

`pip install tree-sitter-powershell` · installs (wheel) · licence: MIT · rank 2655 · last release 2026-05-04 · [PyPI](https://pypi.org/project/tree-sitter-powershell/)

<details><summary>README extract</summary>

Powershell grammar for tree-sitter

* Powershell 7.3

Sections: tree-sitter-powershell, References

</details>

### Arpeggio

Packrat parser interpreter

`pip install Arpeggio` · installs (wheel) · licence: MIT License · rank 2785 · last release 2025-09-12 · [PyPI](https://pypi.org/project/Arpeggio/)

<details><summary>README extract</summary>

Arpeggio is a recursive descent parser with memoization based on PEG grammars
(aka Packrat parser).

Documentation with tutorials is available here.

Note: for a higher level parsing/language tool (i.e., a nicer interface to
Arpeggio) see textX.

</details>

### tree-sitter-scala

Scala grammar for tree-sitter

`pip install tree-sitter-scala` · installs (wheel) · licence: MIT License · rank 2878 · last release 2026-11-07 · [PyPI](https://pypi.org/project/tree-sitter-scala/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](

Scala grammar for tree-sitter
covering both Scala 2 and 3.

_Scala 2_

- The Scala 2 Language Specification
- Scala 2 Syntax Summary

_Scala 3_

- Scala 3 Syntax Summary

Sections: tree-sitter-scala, References

</details>

### tree-sitter-lua

Lua grammar for tree-sitter

`pip install tree-sitter-lua` · installs (wheel) · licence: MIT · rank 2976 · last release 2026-02-26 · [PyPI](https://pypi.org/project/tree-sitter-lua/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](

Lua grammar for tree-sitter.

- Lua 5.x
- LuaJIT 2.x

- Lua Documentation

Sections: tree-sitter-lua, References

</details>

### tree-sitter-groovy

Groovy grammar for tree-sitter

`pip install tree-sitter-groovy` · installs (wheel) · licence: MIT · rank 3053 · last release 2024-11-19 · [PyPI](https://pypi.org/project/tree-sitter-groovy/)

<details><summary>README extract</summary>

> [!Note]
> this is a WIP and is not super polished, I cobbled this together in an hour to test something, eventually I'd like to clean it up but it works for me for now.

</details>

### tree-sitter-toml

TOML grammar for tree-sitter

`pip install tree-sitter-toml` · installs (wheel) · licence: MIT · rank 3075 · last release 2024-12-03 · [PyPI](https://pypi.org/project/tree-sitter-toml/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

A tree-sitter parser for TOML files.

- TOML v1.0.0

Sections: tree-sitter-toml, References

</details>

### tree-sitter-objc

Objective-C grammar for tree-sitter

`pip install tree-sitter-objc` · installs (wheel) · licence: MIT · rank 3121 · last release 2024-12-16 · [PyPI](https://pypi.org/project/tree-sitter-objc/)

### tree-sitter-zig

Zig grammar for tree-sitter

`pip install tree-sitter-zig` · installs (wheel) · licence: MIT · rank 3128 · last release 2024-12-22 · [PyPI](https://pypi.org/project/tree-sitter-zig/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

Zig grammar for tree-sitter.

- Zig Grammar

Sections: tree-sitter-zig, References

</details>

### tree-sitter-julia

Julia grammar for tree-sitter

`pip install tree-sitter-julia` · installs (wheel) · licence: MIT License · rank 3192 · last release 2024-11-11 · [PyPI](https://pypi.org/project/tree-sitter-julia/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

A tree-sitter parser for Julia.

- The Julia Parser
- Julia ASTs documentation
- JuliaSyntax.jl

Sections: tree-sitter-julia, References

</details>

### tree-sitter-verilog

Verilog grammar for tree-sitter

`pip install tree-sitter-verilog` · installs (wheel) · licence: MIT License · rank 3208 · last release 2024-11-10 · [PyPI](https://pypi.org/project/tree-sitter-verilog/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](

SystemVerilog grammar for tree-sitter.

Sections: tree-sitter-verilog, References, Test

</details>

### tree-sitter-fortran

Fortran grammar for tree-sitter

`pip install tree-sitter-fortran` · installs (wheel) · licence: MIT License · rank 3230 · last release 2026-04-24 · [PyPI](https://pypi.org/project/tree-sitter-fortran/)

<details><summary>README extract</summary>

Fortran grammar for tree-sitter. Adapted from this Fortran grammar.

Sections: tree-sitter-fortran, Setup and usage

</details>

### tree-sitter-sql

Tree-sitter Grammar for SQL

`pip install tree-sitter-sql` · installs (wheel) · licence: MIT License · rank 3336 · last release 2025-10-01 · [PyPI](https://pypi.org/project/tree-sitter-sql/)

<details><summary>README extract</summary>

A general/permissive SQL grammar for tree-sitter.

Features:
For a complete list of features see the the tests

Sections: tree-sitter-sql, Step 1: Download the parser files, Step 2: Compile the Parser, Using cargo, Using npm, Using pip, Features, References, Other projects

</details>

### tree-sitter-xml

XML & DTD grammars for tree-sitter

`pip install tree-sitter-xml` · installs (wheel) · licence: MIT License · rank 3382 · last release 2024-11-13 · [PyPI](https://pypi.org/project/tree-sitter-xml/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

A tree-sitter parser for XML & DTD files.

- Extensible Markup Language (XML) 1.0
- Associating Schemas with XML documents 1.0
- Associating Style Sheets with XML documents 1.0

- [x] Neovim
- [ ] Helix _(has alternatives)_
- [x] Emacs
- [ ] Zed

Sections: tree-sitter-xml, References, Editors

</details>

### tree-sitter-html

HTML grammar for tree-sitter

`pip install tree-sitter-html` · installs (wheel) · licence: MIT License · rank 3383 · last release 2024-11-11 · [PyPI](https://pypi.org/project/tree-sitter-html/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

HTML grammar for tree-sitter.

References

- The HTML5 Spec

</details>

### tree-sitter-markdown

Markdown grammar for tree-sitter

`pip install tree-sitter-markdown` · installs (wheel) · licence: MIT License · rank 3446 · last release 2026-10-24 · [PyPI](https://pypi.org/project/tree-sitter-markdown/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

A Markdown parser for [tree-sitter].

The parser is designed to read markdown according to the [CommonMark Spec],
but some extensions to the spec from different sources such as [Github flavored
markdown] are also included. These can be toggled on or off at compile time.
For specifics see Extensions ...

Sections: tree-sitter-markdown, Goals, Extensions, Usage in Editors, Standalone usage, Usage with WASM

</details>

### tree-sitter-css

CSS grammar for tree-sitter

`pip install tree-sitter-css` · installs (wheel) · licence: MIT · rank 3486 · last release 2025-09-28 · [PyPI](https://pypi.org/project/tree-sitter-css/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

CSS grammar for tree-sitter.

References

- CSS Syntax Guide

</details>

### tree-sitter-regex

Regex grammar for tree-sitter

`pip install tree-sitter-regex` · installs (wheel) · licence: MIT · rank 3690 · last release 2025-09-13 · [PyPI](https://pypi.org/project/tree-sitter-regex/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

Regex grammar for tree-sitter. Note that this grammar supports the [PCRE2], [POSIX], and [JavaScript] regex syntaxes.

</details>

### clang

libclang python bindings

`pip install clang` · installs (wheel) · licence: Apache Software License · rank 4079 · last release 2025-12-18 · [PyPI](https://pypi.org/project/clang/)

<details><summary>README extract</summary>

This repository builds and releases the clang package on pypi .

The wheel is built from the LLVM libclang python binding source code directly. Thanks @nightlark for the 2025 refresh of the build process.

This package does not contain binary files for the libclang library, only the python bindings.

</details>

### PyShexC

PyShExC - Python ShEx compiler

`pip install PyShexC` · installs (wheel) · licence: MIT License · rank 4799 · last release 2026-05-01 · [PyPI](https://pypi.org/project/PyShexC/)

<details><summary>README extract</summary>

This repository was originally developed by Eric Prud'hommeaux (@ericprud). All credit goes to him and other original developers. The reason for creating a detached fork (original repo) in the LinkML organization was to be able to support Python 3.14 in LinkML and to put the project in an organization that would allow for sustainability through ...

Sections: PyShExC - The Python ShExC Parser, Usage, Command Line

</details>

### PyShEx

Python ShEx interpreter

`pip install PyShEx` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 4804 · last release 2026-05-07 · [PyPI](https://pypi.org/project/PyShEx/)

<details><summary>README extract</summary>

This repository was originally developed by Harold Solbrig and was kindly contributed
to the LinkML organization because of his retirement. All credit for the original development of this repository goes
to him.

Since development was taken over after a long time of no development, there are tests that are not passing. ...

Example:
```python
        ...
if isinstance(se, ShExJ.ShapeAnd):
    return satisfiesShapeAnd(cntxt, n, se)
        ...
def satisfiesShapeAnd(cntxt: Context, n: nodeSelector, se: ShExJ.ShapeAnd) -> bool:
    return all(satisfies(cntxt, n, se2) for se2 in se.shapeExprs)
```

Sections: Special note, Python implementation of ShEx 2.0, Revisions, shexeval CLI, Documentation, General Layout, Dependencies, Conformance, Docker, Build, Run

</details>

### ShExJSG

ShExJSG - Astract Syntax Tree Definition for the ShEx 2.0 language

`pip install ShExJSG` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 4805 · last release 2026-05-04 · [PyPI](https://pypi.org/project/ShExJSG/)

<details><summary>README extract</summary>

This repository was originally developed by Harold Solbrig and was kindly contributed
to the LinkML organization because of his retirement. All credit for the original development of this repository goes
to him.

Python representation of the ShEx AST(ish) specification.

Example:
```python
from ShExJSG import Schema, ShExJ
from PyShExC import ShExC
from pyjsg.jsglib.loader import is_valid

schema = Schema()

schema.start = ShExJ.Shape()

print(is_valid(schema))
print(schema._as_json_dumps())
print(str(ShExC(schema)))
```

Sections: ShExJSG -, Use, ShExJ.jsg, ShExJ.py, Updating the parser

</details>

### tree-sitter-hcl

HCL and terraform grammar for tree-sitter

`pip install tree-sitter-hcl` · installs (wheel) · licence: Apache-2.0 · rank 5585 · last release 2025-06-16 · [PyPI](https://pypi.org/project/tree-sitter-hcl/)

<details><summary>README extract</summary>

tree-sitter grammar for the HCL language

Try the parser in the playground

Sections: tree-sitter-hcl, Try It Out, Example, Running Tests, Compliance, Fuzzing, Attributions

</details>

### TatSu

TatSu takes a grammar in a variation of EBNF as input, and outputs a memoizing PEG/Packrat parser in Python.

`pip install TatSu` · installs (wheel) · licence: BSD License · rank 5739 · last release 2026-07-09 · [PyPI](https://pypi.org/project/TatSu/) · [docs](https://neogeny.github.io/TatSu) · [source](https://github.com/neogeny/TatSu)

<details><summary>README extract</summary>

license| ​
fury| ​ ​ ​
sponsor|

 *At least for the people who send me mail about a new language that
 they're designing, the general advice is: do it to learn about how
 to write a compiler. Don't have any expectations that anyone will
 use it, unless you hook up with some sort of organization in a
 position to push it hard. ...

Features:
Regular expressions are *“memory-less”*—they excel at finding flat patterns
like email addresses or phone numbers, but they fail once data becomes
hierarchical. ...

Example:
```python
parser = tatsu.compile(grammar)
```

Sections: The New CLI Tool, Why use a PEG parser generator?, Compatibility, Using the Tool, Documentation, Questions?, Changes, For Fun

</details>

### textX

Meta-language for DSL implementation inspired by Xtext

`pip install textX` · installs (wheel) · licence: MIT License · rank 7672 · last release 2026-07-08 · [PyPI](https://pypi.org/project/textX/) · [source](https://github.com/textX/textX/)

<details><summary>README extract</summary>

textX is a meta-language for building Domain-Specific Languages (DSLs) in
Python. It is inspired by [Xtext].

In a nutshell, textX will help you build your textual language in an easy way.
You can invent your own language or build a support for already existing textual
language or file format. ...

Example:
```python
from textx import metamodel_from_str, get_children_of_type

grammar = """
Model: commands*=DrawCommand;
DrawCommand: MoveCommand | ShapeCommand;
ShapeCommand: LineTo | Circle;
MoveCommand: MoveTo | MoveBy;
MoveTo: 'move' 'to' position=Point;
MoveBy: 'move' 'by' vector=Point;
Circle: 'circle' radius=INT;
LineTo: 'line' 'to' point=Point;
...
```

...

</details>

### tree-sitter-starlark

Starlark grammar for tree-sitter

`pip install tree-sitter-starlark` · installs (wheel) · licence: MIT · rank 9055 · last release 2024-12-05 · [PyPI](https://pypi.org/project/tree-sitter-starlark/)

<details><summary>README extract</summary>

Starlark grammar for tree-sitter

Adapted from the official spec
and the Google spec

</details>

### tree-sitter-dart

Dart grammar for tree-sitter (covers Flutter)

`pip install tree-sitter-dart` · installs (wheel) · licence: MIT License · rank 9381 · last release 2026-06-21 · [PyPI](https://pypi.org/project/tree-sitter-dart/) · [source](https://github.com/efrenbl/tree-sitter-dart)

<details><summary>README extract</summary>

A tree-sitter grammar for the Dart programming
language — which also covers Flutter (Flutter widgets are ordinary Dart
classes; there is no separate Flutter syntax).

This is a fork of UserNobody14/tree-sitter-dart
(MIT) packaged and published as a **Python distribution with pre-compiled
wheels** (Linux/macOS/Windows), since no `tree-sitter-dart` ...

Example:
```python
import tree_sitter_dart
from tree_sitter import Language, Parser

parser = Parser(Language(tree_sitter_dart.language()))
tree = parser.parse(b"class MyWidget extends StatelessWidget { Widget build(c) {} }")
print(tree.root_node.type)  # -> program
```

Sections: tree-sitter-dart, Python usage, Getting started, To test a single highlight file, To test a single test file

</details>

### scan-build

Run the Clang static analyzer on projects with a compilation database.

`pip install scan-build` · installs (wheel) · licence: MIT · rank 10431 · last release 2026-08-10 · [PyPI](https://pypi.org/project/scan-build/) · [source](https://github.com/rizsotto/scan-build)

<details><summary>README extract</summary>

`clanganalyzer` runs the Clang static analyzer against a project using
its compilation database, and generates a report of the potential bugs
it finds. It lets you analyze an existing code base without modifying the
build.

Sections: clanganalyzer, How to use, Prerequisites and limitations, Problem reports

</details>

### etcd-distro

Python distribution for etcd, a key-value store, to make the installation easier on various platforms

`pip install etcd-distro` · installs (wheel) · licence: Apache Software License · rank 10526 · last release 2021-12-21 · [PyPI](https://pypi.org/project/etcd-distro/) · [source](https://github.com/sighingnow/etcd-distro)

<details><summary>README extract</summary>

etcd-distro

etcd-distro is a etcd Python distribution to make it can be easier
installed on various platforms only with `pip` command,

etcd-distro is inspired by the CMake Python distribution project.

License

The etcd-distro package use the same license as etcd, i.e., Apache 2.0 license.

</details>

### tree-sitter-fsharp

F# grammars (implementation and signature files) for tree-sitter

`pip install tree-sitter-fsharp` · installs (wheel) · licence: MIT · rank 13574 · last release 2026-09-12 · [PyPI](https://pypi.org/project/tree-sitter-fsharp/)

<details><summary>README extract</summary>

F# grammars for tree-sitter, packaged for Python.

The package ships two parsers:

| Function | Grammar | File types |

| `language()` | implementation files | `.fs`, `.fsx` |
| `language_signature()` | signature files | `.fsi` |

Example:
```python
from tree_sitter import Language, Parser
import tree_sitter_fsharp

parser = Parser(Language(tree_sitter_fsharp.language()))

tree = parser.parse(b"let x = 1\n")
print(tree.root_node)
```

Sections: tree-sitter-fsharp, Usage, Queries

</details>

### pyPEG2

An intrinsic PEG Parser-Interpreter for Python

`pip install pyPEG2` · installs from source (sdist only) · licence: GNU General Public License v2 (GPLv2) · rank 13604 · last release 2015-10-07 · [PyPI](https://pypi.org/project/pyPEG2/)

_README extract left out: share-alike licence._

### guppylang

Pythonic quantum-classical programming language

`pip install guppylang` · installs (wheel) · licence: Apache Software License · rank 13865 · last release 2026-10-26 · [PyPI](https://pypi.org/project/guppylang/) · [source](https://github.com/quantinuum/guppylang)

<details><summary>README extract</summary>

[](
[](
[](

Guppy is a quantum programming language that is fully embedded into Python.
It allows you to write high-level hybrid quantum programs with classical control flow and mid-circuit measurements using Pythonic syntax:

Example:
```python
from guppylang import guppy
from guppylang.std.builtins import owned
from guppylang.std.quantum import cx, h, measure, qubit, x, z

@guppy
def teleport(src: qubit @ owned, tgt: qubit) -> None:
    """Teleports the state in `src` to `tgt`."""
    # Create ancilla and entangle it with src and tgt
    tmp = qubit()
    h(tmp)
    cx(tmp, tgt)
...
```

Sections: Guppy, Documentation, Attribution

</details>

### guppylang-internals

Compiler internals for `guppylang` package.

`pip install guppylang-internals` · installs (wheel) · licence: Apache Software License · rank 13967 · last release 2026-10-26 · [PyPI](https://pypi.org/project/guppylang-internals/)

<details><summary>README extract</summary>

This packages contains the internals of the Guppy compiler.

See `guppylang` for the package providing the user-facing language frontend.

</details>

### tree-sitter-cmake

CMake grammar for tree-sitter

`pip install tree-sitter-cmake` · installs from source (sdist only) · licence: MIT · rank 14083 · last release 2025-11-24 · [PyPI](https://pypi.org/project/tree-sitter-cmake/)

<details><summary>README extract</summary>

This is a tree-sitter grammar for CMake.

Note: This repository is a fork of uyha/tree-sitter-cmake.
If you encounter any issues or have questions, please submit them to the issue tracker.

Example:
```python
import tree_sitter_cmake
import tree_sitter

# Load the CMake language
cmake_language = tree_sitter.Language(tree_sitter_cmake.language())

# Initialize the parser
parser = tree_sitter.Parser(cmake_language)

# Parse some CMake code
source_code = b"""
cmake_minimum_required(VERSION 3.10)
project(Test)

set(CMAKE_CXX_STANDARD 17)
...
```

Sections: tree-sitter-cmake, Usage, Parsed Syntax, Requirements

</details>

### tree-sitter-pascal

Pascal grammar for tree-sitter

`pip install tree-sitter-pascal` · installs (wheel) · licence: AGPL-3.0-only · rank 14154 · last release 2026-07-01 · [PyPI](https://pypi.org/project/tree-sitter-pascal/) · [source](https://github.com/jimmckeeth/tree-sitter-pascal)

_README extract left out: share-alike licence._

### tree-sitter-haskell

Haskell grammar for tree-sitter

`pip install tree-sitter-haskell` · installs (wheel) · licence: MIT License · rank 14170 · last release 2026-09-30 · [PyPI](https://pypi.org/project/tree-sitter-haskell/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

Haskell grammar for [tree-sitter].

- Haskell 2010 Language Report – Syntax References
- GHC Language Extensions

Sections: tree-sitter-haskell, References, Bugs, CPP, Querying, Output path, The grammar, Generating the parser, Compiling the parser, WebAssembly, Debugging, Tracing

</details>

### tree-sitter-vb-dotnet

Tree sitter grammar for VB.NET

`pip install tree-sitter-vb-dotnet` · installs (wheel) · licence: MIT · rank 14287 · last release 2026-09-04 · [PyPI](https://pypi.org/project/tree-sitter-vb-dotnet/)

<details><summary>README extract</summary>

> Tree‑sitter grammar for Visual Basic .NET (VB.NET) – incremental parsing for editors, code‑intel, refactoring tools and static‑analysis pipelines.

Example:
```python
import tree_sitter
import tree_sitter_vb_dotnet

language = tree_sitter.Language(tree_sitter_vb_dotnet.language())
```

Sections: tree‑sitter‑vb‑dotnet, Python package

</details>

### tree-sitter-luau

Luau grammar for tree-sitter

`pip install tree-sitter-luau` · installs (wheel) · licence: MIT · rank 14395 · last release 2024-12-22 · [PyPI](https://pypi.org/project/tree-sitter-luau/)

<details><summary>README extract</summary>

Luau grammar for tree-sitter.

Adapted from the syntax spec

</details>

### tree-sitter-svelte

Svelte grammar for tree-sitter

`pip install tree-sitter-svelte` · installs (wheel) · licence: MIT License · rank 14931 · last release 2024-09-08 · [PyPI](https://pypi.org/project/tree-sitter-svelte/)

## Also in this topic

- [asttokens](software-development-code-generators.md#asttokens) - Annotate AST trees with source code positions
- [Cython](software-development-code-generators.md#cython) - The Cython compiler for writing C extensions in the Python language.
- [llvmlite](software-development-code-generators.md#llvmlite) - lightweight wrapper around basic LLVM functionality
- [boolean.py](scientific-engineering-mathematics.md#booleanpy) - Define boolean algebras, create and parse boolean expressions and create custom boolean DSL.
- [pyelftools](file-formats.md#pyelftools) - Library for analyzing ELF files and DWARF debugging information
- [astor](software-development-code-generators.md#astor) - Read/rewrite/write Python ASTs
- [libsass](internet-www-http.md#libsass) - Sass for Python: A straightforward binding of libsass for Python.
- [ziglang](software-development-build-tools.md#ziglang) - Zig is a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.
- [pyslang](scientific-engineering-electronic-design-automation-eda.md#pyslang) - Python bindings for slang, a library for compiling SystemVerilog
- [platformio](software-development.md#platformio) - Your Gateway to Embedded Software Development Excellence. Unlock the true potential of embedded software development with PlatformIO's collaborative ecosystem, embracing declarative principles, test-driven methodologies, and modern toolchains for unrivaled success.
- [pytensor](scientific-engineering-mathematics.md#pytensor) - Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
- [esprima](software-development-code-generators.md#esprima) - ECMAScript parsing infrastructure for multipurpose analysis in Python
- [systemrdl-compiler](scientific-engineering-electronic-design-automation-eda.md#systemrdl-compiler) - Parse and elaborate front-end for SystemRDL 2.0
- [qiskit](scientific-engineering-quantum-computing.md#qiskit) - An open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives.
- [protoc-gen-connect-python](software-development-code-generators.md#protoc-gen-connect-python) - Code generator for connect-python
- [Nuitka](software-development-build-tools.md#nuitka) - Python compiler with full language support and CPython compatibility
- [pythran](software-development-code-generators.md#pythran) - Ahead of Time compiler for numeric kernels
- [livereload](software-development-build-tools.md#livereload) - Python LiveReload is an awesome tool for web developers
- [wasmer](software-development.md#wasmer) - Python extension to run WebAssembly binaries
- [wasmer-compiler-cranelift](software-development.md#wasmer-compiler-cranelift) - The Cranelift compiler for the `wasmer` package (to compile WebAssembly module)
- [cxxheaderparser](software-development.md#cxxheaderparser) - Modern C++ header parser
- [protoc-gen-connectrpc](software-development-code-generators.md#protoc-gen-connectrpc) - Code generator for Connect RPC
- [pioarduino](software-development.md#pioarduino) - pioarduino core is needed to run pioarduino Platform espressif32.
- [solc-select](software-development-build-tools.md#solc-select) - Manage multiple Solidity compiler versions.
- [latex2sympy2](education.md#latex2sympy2) - Convert latex to sympy with ANTLR and support Matrix, Linear Algebra and CAS functions.
- [odata-query](database.md#odata-query) - An OData query parser and transpiler.
- [taichi](games-entertainment-simulation.md#taichi) - The Taichi Programming Language
- [prophy](scientific-engineering-interface-engine-protocol-translator.md#prophy) - prophy: fast serialization protocol
- [quadrants](games-entertainment-simulation.md#quadrants) - The Quadrants Programming Language
- [Theano-PyMC](scientific-engineering-mathematics.md#theano-pymc) - Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
- [CppHeaderParser](software-development.md#cppheaderparser) - Parse C++ header files and generate a data structure representing the class
- [ethos-u-vela](scientific-engineering-artificial-intelligence.md#ethos-u-vela) - Neural network model compiler for Arm Ethos-U NPUs
- [Theano](scientific-engineering-mathematics.md#theano) - Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
- [buf-bin](software-development-build-tools.md#buf-bin) - Buf CLI distributed via PyPI
- [TatSu-LTS](software-development-code-generators.md#tatsu-lts) - TatSu takes a grammar in a variation of EBNF as input, and outputs a memoizing PEG/Packrat parser in Python.
- [pyvcg](scientific-engineering-mathematics.md#pyvcg) - Verification Condition Generator
- [miss-hit-core](scientific-engineering-2.md#miss-hit-core) - Code formatting and code metrics for programs written in the MATLAB/Simulink and Octave languages.
