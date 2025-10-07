import tkinter as tk

#creating window
root = tk.Tk()

#this is for thw width and length of the window ("W,H")
root.geometry("500x500")

#TITLE
root.title("My First GUI")

#THIS IS FOR TEXT
label = tk.Label(root, text="Hello World!", font=('Arial', 18))

#pack is to show an object or smth padx=width pady=height
label.pack(padx=20,pady=20)

#TEXTBOX
textbox = tk.Text(root, height=3,font=('Arial',16))
textbox.pack(padx=10,pady=10)

#ENTRY FOR INPUTTING
myentry = tk.Entry(root)
myentry.pack()

button = tk.Button(root, text="Click Me!", font=('Arial',18))
button.pack(padx=10, pady=10)



buttonframe = tk.Frame(root)
# buttonframe.columnconfigure(0,weight=1) THIS IS FOR THE OBJECTS TO STRETCH IN THE X AXIS
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial',16))
btn1.grid(row=0, column=0)
#sticky =tk.W+tk.E stretches the button kinda like in a calculator, they are close together
btn2 = tk.Button(buttonframe, text="2", font=('Arial',16))
btn2.grid(row=1, column=0,sticky =tk.W+tk.E)

# buttonframe.pack()
#fill='x' stretches the button
#you need to fill x and use sticky in order for it to work, you need both

buttonframe.pack(fill='x')


#to run the window
root.mainloop()


