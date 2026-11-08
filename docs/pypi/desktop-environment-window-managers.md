# Desktop Environment / Window Managers

[Index](README.md) · 1 packages in this topic, by downloads.

### pytest-qt

pytest support for PyQt and PySide applications

`pip install pytest-qt` · installs (wheel) · licence: MIT License · rank 3998 · last release 2025-07-01 · [PyPI](https://pypi.org/project/pytest-qt/)

<details><summary>README extract</summary>

pytest-qt is a pytest plugin that allows programmers to write tests
for PyQt5, PyQt6, and PySide6 applications.

The main usage is to use the `qtbot` fixture, responsible for handling `qApp`
creation as needed and provides methods to simulate user interaction,
like key presses and mouse clicks: ...

Features:
- qtbot fixture to simulate user interaction with `Qt` widgets.
- Automatic capture of `qDebug`, `qWarning` and `qCritical` messages;
- waitSignal and waitSignals functions to block test execution until specific
 signals are emitted. ...

Example:
```python
def test_hello(qtbot):
    widget = HelloWidget()
    qtbot.addWidget(widget)

    # click in the Greet button and make sure it updates the appropriate label
...

</details>

