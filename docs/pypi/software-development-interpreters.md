# Software Development / Interpreters

[Index](README.md) · 5 packages in this topic, 16 more listed under another topic, by downloads.

### cel-expr-python

The CEL Python runtime

`pip install cel-expr-python` · installs (wheel) · licence: Apache-2.0 · rank 4614 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cel-expr-python/) · [source](https://github.com/cel-expr/cel-python)

<details><summary>README extract</summary>

This is a Python wrapper for the CEL C++ implementation.

Example:
```python
from cel_expr_python import cel
```

Sections: CEL Python Wrapper (cel-expr-python), Usage, Importing CEL module, Creating and configuring CEL environment, Optional configuration parameters, Compiling expressions, Evaluation, Using an Activation, Using an Arena, Working with Protobufs, Custom functions, Extensions, Standard extensions, Defining a custom extension in Python

</details>

### empy

A templating system for Python.

`pip install empy` · installs from source (sdist only) · licence: BSD License · rank 4921 · last release 2026-02-09 · [PyPI](https://pypi.org/project/empy/)

<details><summary>README extract</summary>

EmPy is a powerful, robust and mature
templating system for inserting Python code in template text. EmPy
takes a source document, processes it, and produces output. This is
accomplished via expansions, which are signals to the EmPy system
where to act and are indicated with markup. ...

</details>

### quickjs-rs

Sandboxed JavaScript execution for Python, via wasmtime + rquickjs.

`pip install quickjs-rs` · installs (wheel) · licence: MIT License · rank 5140 · last release 2026-10-20 · [PyPI](https://pypi.org/project/quickjs-rs/)

<details><summary>README extract</summary>

Sandboxed JavaScript execution for Python.

JS runs inside a WebAssembly sandbox: quickjs-ng (a QuickJS fork) via rquickjs is compiled to `wasm32-wasip1` and driven by wasmtime. The package is pure Python - one universal wheel that bundles the guest `.wasm` artifacts; the only runtime dependency is `wasmtime`. ...

Example:
```python
from quickjs_rs import Runtime

with Runtime() as rt:
    with rt.new_context() as ctx:
        assert ctx.eval("1 + 2") == 3

        # Register a Python callable as a JS global.
        @ctx.function
        def greet(name: str) -> str:
            return f"hi {name}"
        assert ctx.eval("greet('world')") == "hi world"
```

Sections: quickjs-rs, Quickstart, ES modules, TypeScript, Snapshots

</details>

### common-expression-language

Python bindings for the Common Expression Language (CEL)

`pip install common-expression-language` · installs (wheel) · licence: Apache-2.0 · rank 6407 · last release 2026-09-15 · [PyPI](https://pypi.org/project/common-expression-language/) · [source](https://github.com/hardbyte/python-common-expression-language)

<details><summary>README extract</summary>

Fast, Safe, and Expressive evaluation of Google's Common Expression Language (CEL) in Python, powered by Rust.

The Common Expression Language (CEL) is a non-Turing complete language designed for simplicity, speed, and safety. ...

Features:
- ✅ Fast Evaluation: Microsecond-level expression evaluation via Rust
- ✅ Rich Type System: Integers, floats, strings, lists, maps, timestamps, durations, bytes, optionals ...

Example:
```python
from cel import evaluate, Context

# Access control policy
policy = """
user.role == "admin" ||
(resource.owner == user.id && current_hour >= 9 && current_hour <= 17)
"""

context = Context()
context.update({
    "user": {"id": "alice", "role": "user"},
    "resource": {"owner": "alice"},
    "current_hour": 14  # 2 PM
})

...
```

...

</details>

### spyder-kernels

Jupyter kernels for Spyder's console

`pip install spyder-kernels` · installs (wheel) · licence: MIT · rank 11342 · last release 2026-11-02 · [PyPI](https://pypi.org/project/spyder-kernels/)

<details><summary>README extract</summary>

Package that provides Jupyter kernels for use with the consoles of Spyder, the
Scientific Python Development Environment.

These kernels can be launched either through Spyder itself or in an independent
Python session, and allow for interactive or file-based execution of Python
code inside Spyder. ...

Sections: Jupyter kernels for the Spyder console, Dependencies

</details>

## Also in this topic

- [asttokens](software-development-code-generators.md#asttokens) - Annotate AST trees with source code positions
- [pyinstaller](software-development.md#pyinstaller) - PyInstaller bundles a Python application and all its dependencies into a single package.
- [parsy](software-development-compilers.md#parsy) - Easy-to-use parser combinators, for parsing in pure Python
- [wasmtime](software-development-compilers.md#wasmtime) - A WebAssembly runtime powered by Wasmtime
- [Arpeggio](software-development-compilers.md#arpeggio) - Packrat parser interpreter
- [abnf](software-development-code-generators.md#abnf) - Parsers for ABNF grammars.
- [bashkit](security.md#bashkit) - A sandboxed bash interpreter for AI agents
- [wasmer](software-development.md#wasmer) - Python extension to run WebAssembly binaries
- [wasmer-compiler-cranelift](software-development.md#wasmer-compiler-cranelift) - The Cranelift compiler for the `wasmer` package (to compile WebAssembly module)
- [textX](software-development-compilers.md#textx) - Meta-language for DSL implementation inspired by Xtext
- [hachoir](multimedia.md#hachoir) - Package of Hachoir parsers used to open binary files
- [fortranformat](scientific-engineering-2.md#fortranformat) - Mimics Fortran textual IO in Python.
- [cppyy-cling](software-development.md#cppyy-cling) - Re-packaged Cling, as backend for cppyy
- [pyPEG2](software-development-compilers.md#pypeg2) - An intrinsic PEG Parser-Interpreter for Python
- [cppyy-backend](software-development.md#cppyy-backend) - C/C++ wrapper for Cling
- [TatSu-LTS](software-development-code-generators.md#tatsu-lts) - TatSu takes a grammar in a variation of EBNF as input, and outputs a memoizing PEG/Packrat parser in Python.
