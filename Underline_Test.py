try:
    import Tkinter as tk
    import tkFont
except ModuleNotFoundError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.count = 0
        l = tk.Label(text="Hello, world")
        l.pack()
        # clone the font, set the underline attribute,
        # and assign it to our widget
        f = tkFont.Font(l, l.cget("font"))
        f.configure(underline = True)
        l.configure(font=f)
        self.root.mainloop()


if __name__ == "__main__":
    app = App()