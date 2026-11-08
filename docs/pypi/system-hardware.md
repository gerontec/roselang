# System / Hardware

[Index](README.md) · 8 packages in this topic, 43 more listed under another topic, by downloads.

### libusb-package

Package containing libusb so it can be installed via Python package managers

`pip install libusb-package` · installs (wheel) · licence: Apache Software License · rank 3683 · last release 2026-06-30 · [PyPI](https://pypi.org/project/libusb-package/)

<details><summary>README extract</summary>

This Python package functions as an installation vehicle for libusb shared libraries, to
simplify installation of tools that require libusb. The main use case is so that users
don't have to install libusb manually for projects that use pyusb. However, any Python
project that uses a libusb wrapper can also benefit. ...

Example:
```python
import libusb_package

for dev in libusb_package.find(find_all=True):
    print(dev)
```

Sections: Container package for libusb, APIs, Versioning, Examples, Source distribution

</details>

### nvitop

An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management.

`pip install nvitop` · installs (wheel) · licence: Apache Software License; GNU General Public License v3 (GPLv3) · rank 7976 · last release 2026-10-26 · [PyPI](https://pypi.org/project/nvitop/) · [docs](https://nvitop.readthedocs.io) · [source](https://github.com/XuehaiPan/nvitop)

_README extract left out: share-alike licence._

### python-snap7

Pure Python S7 communication library for Siemens PLCs

`pip install python-snap7` · installs (wheel) · licence: MIT · rank 9101 · last release 2026-10-28 · [PyPI](https://pypi.org/project/python-snap7/) · [docs](https://python-snap7.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

python-snap7 is a pure-Python library for communicating with Siemens S7 PLCs
using the classic S7 protocol. It supports S7-300 and S7-400 controllers, as
well as S7-1200 and S7-1500 controllers with PUT/GET access enabled. It
supports Python 3.10+ on Windows, Linux, and macOS without native dependencies. ...

Example:
```python
from s7 import Client

client = Client()
client.connect("192.168.1.10", 0, 1)
data = client.db_read(1, 0, 4)
client.disconnect()
```

Sections: python-snap7, S7-1200 and S7-1500, Quick start, Documentation

</details>

### nidaqmx

Official NI-DAQmx Python API

`pip install nidaqmx` · installs (wheel) · licence: MIT License · rank 10697 · last release 2026-10-26 · [PyPI](https://pypi.org/project/nidaqmx/) · [docs](https://nidaqmx-python.readthedocs.io) · [source](https://github.com/ni/nidaqmx-python)

<details><summary>README extract</summary>

+------------+-----------------------------------------------------------+
| Info
+------------+-----------------------------------------------------------+
| Author
+------------+-----------------------------------------------------------+ ...

Example:
```python
>>> import nidaqmx
>>> with nidaqmx.Task() as task:
...     task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
...     task.read()
...
-0.07476920729381246
>>> with nidaqmx.Task() as task:
...     task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
...     task.read(number_of_samples_per_channel=2)
...
[0.26001373311970705, 0.37796597238117036]
...
```

...

</details>

### feetech-servo-sdk

This is source code from official feetech repository

`pip install feetech-servo-sdk` · installs from source (sdist only) · licence: The Unlicense (Unlicense) · rank 12521 · last release 2022-11-08 · [PyPI](https://pypi.org/project/feetech-servo-sdk/)

<details><summary>README extract</summary>

This is source code from official feetech repository.
The repository structure copies the structure of the original library

The `scsservo_sdk_example` directories contain examples of using the library.

The source code of the library is located in the `scservo_sdk` directory. ...

Sections: Feetech-Servo-SDK, Structure, Usage, Method 1. Clone repositry

</details>

### libucx-cu13

The Unified Communication X library (UCX)

`pip install libucx-cu13` · installs (wheel) · licence: BSD-3-Clause · rank 12662 · last release 2026-09-30 · [PyPI](https://pypi.org/project/libucx-cu13/)

<details><summary>README extract</summary>

This repository hosts code for building wheels of UCX.

RAPIDS publishes multiple libraries that rely on UCX, including UCXX.
One of the ways that RAPIDS vendors these libraries is in the form of pip wheels.
For portability, wheels should be as self-contained as possible as per the manylinux standard. ...

Sections: UCX wheel building, Purpose, How UCX Wheels Are Built

</details>

### libucx-cu12

The Unified Communication X library (UCX)

`pip install libucx-cu12` · installs (wheel) · licence: BSD-3-Clause · rank 14052 · last release 2026-09-30 · [PyPI](https://pypi.org/project/libucx-cu12/)

<details><summary>README extract</summary>

This repository hosts code for building wheels of UCX.

RAPIDS publishes multiple libraries that rely on UCX, including UCXX.
One of the ways that RAPIDS vendors these libraries is in the form of pip wheels.
For portability, wheels should be as self-contained as possible as per the manylinux standard. ...

Sections: UCX wheel building, Purpose, How UCX Wheels Are Built

</details>

### PyTmcStepper

This is a Python libary to drive a stepper motor with a Trinamic stepper driver and a single board computer like a Raspberry Pi

`pip install PyTmcStepper` · installs (wheel) · licence: GPL-3.0 · rank 14612 · last release 2026-08-14 · [PyPI](https://pypi.org/project/PyTmcStepper/)

_README extract left out: share-alike licence._

## Also in this topic

- [psutil](software-development-libraries.md#psutil) - Cross-platform lib for process and system monitoring.
- [nvidia-ml-py](software-development-libraries.md#nvidia-ml-py) - Python Bindings for the NVIDIA Management Library
- [pyusb](scientific-engineering-interface-engine-protocol-translator.md#pyusb) - Easy USB access for Python
- [python-can](software-development-embedded-systems.md#python-can) - Controller Area Network interface module for Python
- [pynvml](software-development-libraries.md#pynvml) - Python utilities for the NVIDIA Management Library
- [circular-dict](software-development-debuggers.md#circular-dict) - CircularDict is a high-performance Python data structure that blends the functionality of dictionaries and circular buffers. Inheriting the usage of traditional dictionaries, it allows you to define constraints on size and memory usage. This way, the CircularDict will be always up-to-date with the last N added elements, ensuring that neither the maximum length nor the memory usage limit is exceeded. It is ideal for caching large data structures while maintaining control over memory footprint.
- [pyudev](software-development-libraries-2.md#pyudev) - A libudev binding
- [libusb1](software-development-libraries-2.md#libusb1) - Pure-python wrapper for libusb-1.0
- [btsocket](education.md#btsocket) - Python library for BlueZ Bluetooth Management API
- [nvidia-ml-py3](software-development-libraries-2.md#nvidia-ml-py3) - Python Bindings for the NVIDIA Management Library
- [pyftdi](software-development-libraries-2.md#pyftdi) - FTDI device driver (pure Python)
- [phidget22](scientific-engineering.md#phidget22) - Phidget22 Python Library
- [dlipower](software-development-libraries-2.md#dlipower) - Control digital loggers web power switch
- [gpiozero](education.md#gpiozero) - A simple interface to GPIO devices with Raspberry Pi
- [pylibftdi](scientific-engineering.md#pylibftdi) - Pythonic interface to FTDI devices using libftdi.
- [spsdk](scientific-engineering.md#spsdk) - Open Source Secure Provisioning SDK for NXP MCU/MPU
- [libusbsio](scientific-engineering.md#libusbsio) - Python wrapper around NXP LIBUSBSIO library
- [minimalmodbus](communications.md#minimalmodbus) - Easy-to-use Modbus RTU and Modbus ASCII implementation for Python
- [spidev](software-development.md#spidev) - Python bindings for Linux SPI access through spidev
- [Adafruit-PlatformDetect](software-development-libraries-3.md#adafruit-platformdetect) - Platform detection for use by libraries like Adafruit-Blinka.
- [python-miio](home-automation.md#python-miio) - Python library for interfacing with Xiaomi smart appliances
- [Adafruit-PureIO](software-development-libraries-3.md#adafruit-pureio) - Pure python (i.e. no native extensions) access to Linux IO including I2C and SPI. Drop in replacement for smbus and spidev modules.
- [labjack-ljm](software-development.md#labjack-ljm) - LJM library Python wrapper for LabJack T4, T7 and T8.
- [adafruit-circuitpython-requests](software-development-embedded-systems.md#adafruit-circuitpython-requests) - A requests-like library for web interfacing
- [adafruit-circuitpython-typing](software-development-embedded-systems.md#adafruit-circuitpython-typing) - Types needed for type annotation that are not in `typing`
- [adafruit-circuitpython-busdevice](software-development-embedded-systems.md#adafruit-circuitpython-busdevice) - CircuitPython bus device classes to manage bus sharing.
- [inputs](software-development-embedded-systems.md#inputs) - Cross-platform Python support for keyboards, mice and gamepads.
- [pylspci](software-development-libraries-4.md#pylspci) - Simple parser for lspci -mmnn.
- [adafruit-circuitpython-connectionmanager](software-development-embedded-systems.md#adafruit-circuitpython-connectionmanager) - A urllib3.poolmanager/urllib3.connectionpool-like library for managing sockets and connections
- [extra-platforms](software-development-libraries-4.md#extra-platforms) - 🔎 Detect architectures, platforms, shells, terminals, CI systems and agents, grouped by family
- [ouster-sdk](scientific-engineering-2.md#ouster-sdk) - Ouster Sensor SDK
- [pyjoulescope-driver](scientific-engineering-2.md#pyjoulescope-driver) - Joulescope™ driver
- [ucxx-cu13](software-development-libraries-4.md#ucxx-cu13) - Python Bindings for the Unified Communication X library (UCX)
- [libucxx-cu13](software-development-libraries-4.md#libucxx-cu13) - Python Bindings for the Unified Communication X library (UCX)
- [doppler-dsp](scientific-engineering-2.md#doppler-dsp) - Practical, portable, performant digital signal processing.
- [pyrsmi](software-development-libraries-4.md#pyrsmi) - Python System Management Library for AMD GPUs
- [mpremote](software-development-embedded-systems.md#mpremote) - Tool for interacting remotely with MicroPython devices
- [pypemicro](scientific-engineering-2.md#pypemicro) - Python tool to control PEMicro Debug probes
- [xknx](home-automation.md#xknx) - An Asynchronous Library for the KNX protocol. Documentation: https://xknx.io/
- [pyocd-pemicro](scientific-engineering-2.md#pyocd-pemicro) - PyOCD debug probe plugin for PEMicro debug probes
- [RPi.GPIO](home-automation.md#rpigpio) - A module to control Raspberry Pi GPIO channels
- [python-vxi11](scientific-engineering-interface-engine-protocol-translator.md#python-vxi11) - Python VXI-11 driver for controlling instruments over Ethernet
- [membrowse](software-development-build-tools.md#membrowse) - Memory footprint analysis tools for embedded firmware
