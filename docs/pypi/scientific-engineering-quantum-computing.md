# Scientific/Engineering / Quantum Computing

[Index](README.md) · 11 packages in this topic, 2 more listed under another topic, by downloads.

### qiskit

An open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives.

`pip install qiskit` · installs (wheel) · licence: Apache-2.0 · rank 4112 · last release 2026-11-05 · [PyPI](https://pypi.org/project/qiskit/) · [docs](https://quantum.cloud.ibm.com/docs) · [source](https://github.com/Qiskit/qiskit)

<details><summary>README extract</summary>

<!--- long-description-skip-begin -->

<!--- long-description-skip-end -->

Qiskit is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives. ...

Example:
```python
import numpy as np
from qiskit import QuantumCircuit

# 1. A quantum circuit for preparing the quantum state |000> + i |111> / √2
qc = QuantumCircuit(3)
qc.h(0)             # generate superposition
qc.p(np.pi / 2, 0)  # add quantum phase
qc.cx(0, 1)         # 0th-qubit-Controlled-NOT gate on 1st qubit
...
```

Sections: Qiskit, Python, Standalone C library, Create your first quantum program in Qiskit, Executing your code on real quantum hardware

</details>

### cirq-core

A framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits.

`pip install cirq-core` · installs (wheel) · licence: Apache-2.0 · rank 7253 · last release 2026-06-29 · [PyPI](https://pypi.org/project/cirq-core/)

<details><summary>README extract</summary>

[Cirq] is a Python package for writing, manipulating, and running quantum
circuits on quantum computers
and simulators. Cirq provides useful abstractions for dealing with today’s
noisy intermediate-scale quantum (NISQ)
computers, where the details of quantum hardware are vital to achieving
state-of-the-art results. ...

Sections: cirq-core, Documentation, Disclaimer

</details>

### qm-qua

QUA language SDK to control a Quantum Computer

`pip install qm-qua` · installs (wheel) · licence: BSD-3-Clause · rank 9616 · last release 2026-11-02 · [PyPI](https://pypi.org/project/qm-qua/) · [docs](https://docs.quantum-machines.co/) · [source](https://github.com/qm-labs/qm-qua-sdk-public)

<details><summary>README extract</summary>

QUA is a pulse-level language used to control a Quantum System.
Read more about it and its uses here:

This package, qm-qua, is an implementation that uses the Quantum Machines OPX controller and is used to
communicate with the QOP and to implement a Pythonic implementation (DSL) of QUA. ...

</details>

### cirq-ionq

A Cirq package to simulate and connect to IonQ quantum computers

`pip install cirq-ionq` · installs (wheel) · licence: Apache-2.0 · rank 12068 · last release 2026-06-29 · [PyPI](https://pypi.org/project/cirq-ionq/)

<details><summary>README extract</summary>

This is the Cirq-IonQ integration module. It provides an interface that allows
[Cirq] quantum algorithms to run on quantum computers made by IonQ
Inc.. (See the Documentation section
below for information about getting access to IonQ devices.) ...

Sections: cirq-ionq, Documentation, Disclaimer

</details>

### cirq

A framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits.

`pip install cirq` · installs (wheel) · licence: Apache-2.0 · rank 12113 · last release 2026-06-29 · [PyPI](https://pypi.org/project/cirq/)

<details><summary>README extract</summary>

Python package for writing, manipulating, and running quantum
circuits on quantum computers
and simulators.

Features –
Installation –
Quick Start –
Documentation –
Integrations –
Community –
Citing Cirq –
Contact

Features:
Cirq provides useful abstractions for dealing with today’s noisy
intermediate-scale quantum (NISQ) computers,
where the details of quantum hardware are vital to achieving state-of-the-art
results. Some of its features include: ...

Example:
```python
import cirq

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit.
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)
print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
...

</details>

### cirq-google

The Cirq module that provides tools and access to the Google Quantum Computing Service

`pip install cirq-google` · installs (wheel) · licence: Apache-2.0 · rank 12355 · last release 2026-06-29 · [PyPI](https://pypi.org/project/cirq-google/)

<details><summary>README extract</summary>

This is the Cirq-Google integration module. It provides an interface to
Google's Quantum Computing
Service, and also contains
additional tools for calibration and characterization of Google's quantum
hardware devices.

| Please note! |

| Google's quantum hardware is currently available only to authorized partners. ...

Sections: cirq-google, Documentation, Disclaimer

</details>

### chromobius

A fast implementation of the Möbius color code decoder.

`pip install chromobius` · installs (wheel) · licence: Apache-2.0 · rank 12877 · last release 2025-11-21 · [PyPI](https://pypi.org/project/chromobius/)

<details><summary>README extract</summary>

Chromobius is an implementation of a "mobius decoder", which approximates the color code decoding problem as a minimum weight matching problem.
Chromobius uses PyMatching to solve the minimum weight matching problem.

See the paper "New circuits and an open source decoder for the color code" for more details on how Chromobius works.

Example:
```python
import stim
import chromobius
import numpy as np

def count_mistakes(circuit: stim.Circuit, shots: int) -> int:
    # Sample the circuit.
    dets, actual_obs_flips = circuit.compile_detector_sampler().sample(
        shots=shots,
        separate_observables=True,
        bit_packed=True,
    )

    # Decode with Chromobius.
...
```

...

</details>

### cirq-web

Web-based 3D visualization tools for Cirq.

`pip install cirq-web` · installs (wheel) · licence: Apache-2.0 · rank 13820 · last release 2026-06-29 · [PyPI](https://pypi.org/project/cirq-web/)

<details><summary>README extract</summary>

[Cirq] is a Python package for writing, manipulating, and running quantum
circuits on quantum computers
and simulators. Cirq provides useful abstractions for dealing with today’s
noisy intermediate-scale quantum (NISQ)
computers, where the details of quantum hardware are vital to achieving
state-of-the-art results. ...

Example:
```python
import cirq
from cirq_web import BlochSphere

# Prepare a state
zero_state = [1+0j, 0+0j]
state_vector = cirq.to_valid_state_vector(zero_state)

# Create and display the Bloch sphere
sphere = BlochSphere(state_vector=state_vector)
sphere.generate_html_file()
```

Sections: cirq-web, Documentation, Disclaimer

</details>

### cirq-pasqal

A Cirq package to simulate and connect to Pasqal quantum computers

`pip install cirq-pasqal` · installs (wheel) · licence: Apache-2.0 · rank 13824 · last release 2026-06-29 · [PyPI](https://pypi.org/project/cirq-pasqal/)

<details><summary>README extract</summary>

This is the Cirq-Pasqal integration module. It provides an interface that
allows [Cirq] quantum algorithms to run on quantum computers made by
Pasqal. (See the Documentation section
below for information about getting access to Pasqal devices.) ...

Sections: cirq-pasqal, Documentation, Disclaimer

</details>

### cirq-aqt

A Cirq package to simulate and connect to Alpine Quantum Technologies quantum computers

`pip install cirq-aqt` · installs (wheel) · licence: Apache-2.0 · rank 13841 · last release 2026-06-29 · [PyPI](https://pypi.org/project/cirq-aqt/)

<details><summary>README extract</summary>

This is the Cirq-AQT integration module. It provides an interface that allows
[Cirq] quantum algorithms to run on quantum computers made by Alpine Quantum
Technologies GmbH. (See the Documentation
section below for information about getting access to AQT devices.) ...

Sections: cirq-aqt, Documentation, Disclaimer

</details>

### pyqrack

pyqrack - Pure Python vm6502q/qrack Wrapper

`pip install pyqrack` · installs (wheel) · licence: MIT · rank 14944 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pyqrack/)

<details><summary>README extract</summary>

Pure Python bindings for the pure C++11/OpenCL Qrack quantum computer simulator library

(PyQrack is just pure Qrack.)

Note: You must also install OpenCL to use this version of Qrack. (There are also CPU-only and CUDA version.)

If you're looking for Mac ARM support, use the package `pyqrack`, not `pyqrack-cpu`. ...

Example:
```python
sim = QrackSimulator(pyzxCircuit=c)
```

</details>

## Also in this topic

- [openfermion](scientific-engineering-chemistry.md#openfermion) - Package to compile and analyze quantum algorithms for simulating fermionic systems.
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
