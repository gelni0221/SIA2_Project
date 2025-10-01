from tkinter import *
from tkinter.ttk import Combobox

#Tkinter is a GUI
#provides variety of widgets

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

#label
my_label = Label(text="I am a Label", font=("Arial",24,"bold"))
#.pack is used to display the label inside the window
#default the text is center
my_label.pack()
# my_label.pack(side= "left")

#You can override it
my_label["text"] = "This is new Text"
#You can override it different approach
my_label.config(text="This is a new text by keyword arguments")


def button_clicked():
    my_label.config(text="This is a new text by button function i created")

button = Button(text="click me", command= button_clicked)
button.pack()





#this is the one that will activate the window or our code
window.mainloop()