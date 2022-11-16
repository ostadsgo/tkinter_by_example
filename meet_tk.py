import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello World!")

        # Widgets of Main Window
        self.label = ttk.Label(self, text="Choose one:")
        self.label.pack(fill=tk.BOTH, expand=True, padx=30, pady=50)
        hello_button = ttk.Button(self, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        goodbye_button = ttk.Button(self, text="Say Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        self.label.configure(text="Hello World!")

    def say_goodbye(self):
        self.label.configure(text="Goodbye\nClosing after 2 seconds...")
        self.after(2000, self.destroy)


def main():
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
