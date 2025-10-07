from tkinter import *

# Create the main window
window = Tk()
window.title("Layout Manager Topic")
window.minsize(width=500, height=500)

# ----------- Using pack() -----------
label_pack = Label(window, text="This is packed", bg="lightblue", padx=10, pady=10)
label_pack.pack(pady=10)

# ----------- Using place() -----------
label_place = Label(window, text="This is placed", bg="lightgreen", padx=10, pady=10)
label_place.place(x=200, y=100)

# ----------- Using grid() -----------
frame = Frame(window)
frame.pack(pady=20)

label_grid_1 = Label(frame, text="Grid 1", bg="lightyellow", width=15)
label_grid_2 = Label(frame, text="Grid 2", bg="lightcoral", width=15)
label_grid_3 = Label(frame, text="Grid 3", bg="lightgray", width=15)

label_grid_1.grid(row=0, column=0, padx=5, pady=5)
label_grid_2.grid(row=0, column=1, padx=5, pady=5)
label_grid_3.grid(row=1, column=0, columnspan=2, pady=5)

# Run the application
window.mainloop()

# Explanation:
# pack() is used to place widgets one after another (top by default).
#
# place() lets you position widgets absolutely with x and y coordinates.
#
# grid() arranges widgets in a table-like structure (rows and columns).