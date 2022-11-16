import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello World!")

        # Widgets of Main Window
        label = ttk.Label(self, text="Hello World!")
        label.pack(fill=tk.BOTH, expand=True, padx=30, pady=50)


def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()