import tkinter as tk
# from tkinter import *
# from tkinter.ttk import Combobox


def say_hello():
    label.config(text="Hello, Tkinter !")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter (sources) App")
root.geometry("300x150")

# Create a label
label = tk.Label(root, text="Click the button below:")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack(pady=5)
button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
