<!-- Cover -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/tkf/cover.png" alt="Figure" width="970">
    <p align="center">
    <i> </i>
    </p>
</div>

# TkF
**Lightweight Tkinter-based framework to build Python apps**

This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).

[Installation](#installation) | [Documentation](https://github.com/pyrustic/tkf/tree/master/docs/modules#readme) | [Latest](https://github.com/pyrustic/tkf/tags)

**Table of contents**
- [Overview](#overview)
- [Demo](#demo)
- [Installation](#installation)
- [External learning resources](#external-learning-resources)
- [Gaspium](#gaspium)

# Overview
This package includes several other packages and above all exposes `tkf.App`, the main class of the framework.

## Main class
The main class `tkf.App` allows you to:
- display the first view of the application;
- activate the theme of your choice;
- define the width and height of the app window;
- center the application window on the screen;
- make the application window full screen;
- restart the application;
- stop the application;
- et cetera.

### Example
This is an example of usage of `tkf.App`:

<details>
  <summary>Click to expand or collapse </summary>

```python
import tkinter as tk
from tkf import App
from cyberpunk_theme import Cyberpunk


def get_view(app):
    """This is a view function"""
    root = app.root
    # Body
    body = tk.Frame(root)
    # Label 'Hello Friend'
    label = tk.Label(body, text="Hello Friend")
    label.pack(pady=10)
    # Button 'Quit'
    button = tk.Button(body, text="Quit", command=app.exit)
    button.pack(pady=10)
    # Return the body of this view
    return body


# An instance of tkf.App
app = App()

# Size
app.geometry = "300x100"

# Title
app.title = "Example"

# Cyberpunk is a dark theme
app.theme = Cyberpunk()

# A view is either a function that returns a Tkinter widget
# or a Viewable (see the library Viewable)
app.view = get_view

# Center the window on the screen
app.center()

# Start the app (mainloop !)
app.start()


```

</details>

And this is what it looks like:

<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/tkf/example.png" alt="Figure" width="314">
    <p align="center">
    <i> Example </i>
    </p>
</div>


> Read more about the class [tkf.App](https://github.com/pyrustic/tkf/blob/master/docs/modules/content/tkf.__init__/classes.md).


## Batteries included
These are the packages included in TkF:

### Libraries
|Name | Description|
|---|---|
|[Shared](https://github.com/pyrustic/shared) |  Library to store, expose, read, and edit `collections` of data|
|[TkStyle](https://github.com/pyrustic/tkstyle) | Library to create `styles` and `themes` for Python apps|
|[Litemark](https://github.com/pyrustic/litemark) | Lightweight `Markdown` dialect for Python apps|
|[Megawidget](https://github.com/pyrustic/megawidget) | Collection of `megawidgets` to build graphical user interfaces for Python apps|
|[Viewable](https://github.com/pyrustic/viewable) | Class to implement a GUI view with `lifecycle`|
|[Threadom](https://github.com/pyrustic/threadom) | Tkinter-compatible `multithreading`|
|[Suggestion](https://github.com/pyrustic/suggestion) | Democratizing `auto-complete`(suggest) for Python desktop applications|
|[Kurl](https://github.com/pyrustic/kurl) | Konnection URL: `HTTP requests` in Python with an implementation of `conditional request` and a `responses caching` system|
|[Litedao](https://github.com/pyrustic/litedao) | Library to perform intuitive interaction with `SQLite` database|
|[Probed](https://github.com/pyrustic/probed) | Probed `collections` for Python|

> **Note**: The libraries listed above can be downloaded from `PyPI` and installed individually for use as is in new or existing projects without having to use the `TkF` framework.

### Themes
|Name | Description|
|---|---|
|[Cyberpunk-Theme](https://github.com/pyrustic/cyberpunk-theme) | A modern `dark theme` for Python apps|
|[Winter-Theme](https://github.com/pyrustic/winter-theme) | A modern `light theme` for Python apps|

> **Note**: The themes listed above can be downloaded from `PyPI` and installed individually for use as is in new or existing projects without having to use the `TkF` framework.

### Command line tools
|Name | Description|
|---|---|
|[Backstage](https://github.com/pyrustic/backstage) | `CLI` tool to manage, test, build, and release your Python `projects`|

> **Note**: The tools listed above can be downloaded from `PyPI` and installed individually for use as is in new or existing projects without having to use the `TkF` framework.

# Demo
Here is a demo that you can copy and paste and run as is:

<details>
  <summary>Click to expand or collapse </summary>

```python
import tkinter as tk
from tkf import App
from viewable import Viewable
from megawidget import Toast
from cyberpunk_theme import Cyberpunk
from cyberpunk_theme.widget.button import get_button_red_style, get_button_blue_style


class Hello(Viewable):
    """Graphical equivalent of a Hello World"""
    def __init__(self, app):
        super().__init__()
        self._app = app
        self._root = app.root
        self._btn_max = None

    def _build(self):
        """This method is part of the view lifecycle"""
        self._body = tk.Frame(self._root)
        self._root.geometry("500x300")
        # Label
        label = tk.Label(self._body, text="Hello Friend !")
        label.pack(expand=1, fill=tk.BOTH)
        # Footer
        footer = tk.Frame(self._body)
        footer.pack(side=tk.BOTTOM, fill=tk.X, padx=2, pady=2)
        # Button Maximize
        self._btn_max = tk.Button(footer, text="Maximize",
                                  command=self._on_click_btn_max)
        self._btn_max.pack(side=tk.RIGHT, padx=(2, 0))
        # Button Crash
        btn_crash = tk.Button(footer, text="Crash",
                              command=self._on_click_btn_crash)
        btn_crash.pack(side=tk.RIGHT)
        # Styling
        button_red_style = get_button_red_style()
        button_blue_style = get_button_blue_style()
        button_red_style.target(btn_crash)
        button_blue_style.target(self._btn_max)

    def _on_click_btn_max(self):
        self._app.maximize()
        self._btn_max.destroy()

    def _on_click_btn_crash(self):
        toast = Toast(self._body, message="This app is going to crash...")
        toast.wait_window()
        self._app.crash_resistant = False
        raise Exception("Deliberately raised exception !")


def main():
    # The App
    app = App()
    # Set the title
    app.title = "demo"
    # Resizable
    app.resizable = (True, True)
    # Set the theme
    app.theme = Cyberpunk()
    # Set the view
    app.view = Hello
    # Center the window on the screen
    app.center()
    # Lift off !
    app.start()


if __name__ == "__main__":
    main()

```

</details>

And this is what it looks like:

<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/tkf/demo.png" alt="Figure" width="514">
    <p align="center">
    <i> Demo </i>
    </p>
</div>


# Installation
`TkF` is `cross platform` and versions under `1.0.0` will be considered `Beta` at best. It is built on [Ubuntu](https://ubuntu.com/download/desktop) with [Python 3.8](https://www.python.org/downloads/) and should work on `Python 3.5` or newer.

## For the first time

```bash
pip install tkf
```

## Upgrade
```bash
$ pip install tkf --upgrade --upgrade-strategy eager

```


# External learning resources
Some interesting links below to get started with `Python`, `Tkinter` and `SQLite`.

## Introduction to Python
- [python-guide](https://docs.python-guide.org/intro/learning/)
- [python tutorial](https://www.python-course.eu/python3_course.php)
- freeCodeCamp on [Youtube](https://www.youtube.com/watch?v=rfscVS0vtbw)

## Introduction to Tkinter
- [tkdocs](https://tkdocs.com/)
- [tkinter tutorial](https://www.python-course.eu/python_tkinter.php)
- freeCodeCamp on [Youtube](https://www.youtube.com/watch?v=YXPyB4XeYLA)

## Introduction to SQLite
- [sqlitetutorial](https://www.sqlitetutorial.net/)
- freeCodeCamp on [Youtube](https://www.youtube.com/watch?v=byHcYRpMgI4)

`Note:` I am not affiliated with any of these entities. A simple web search brings them up.

# Gaspium
`Gaspium` is a high-productivity framework for building [GASP](https://github.com/pyrustic/gaspium/blob/master/docs/whitepaper.md) applications. Under the hood, `Gaspium` uses `TkF`. If `TkF` is C, `Gaspium` would be Python.

Discover [Gaspium](https://github.com/pyrustic/gaspium) !
