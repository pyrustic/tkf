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
