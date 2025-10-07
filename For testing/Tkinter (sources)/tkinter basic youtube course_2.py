import tkinter as tk
from tkinter import messagebox
class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial',18))
        self.label.pack(padx=10,pady=10)

        #HEIGHT is to control the visible size of the text area.
        self.textbox = tk.Text(self.root,height=5,font=('Arial',16))
        self.textbox.pack(padx=10, pady=10)

        #IntVar() is a Tkinter (sources) variable class that stores an integer and can automatically update when the widget state changes.
        #basically it is 0 when UNCHECKED AND 1 IF IT IS CHECKED, YOU PUT THIS INTO A CHECKBUTTON
        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox",font=('Arial',16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        #THE command=self.show_message should not be command=self.show_message()
        #THIS SHOULD JUST PASS THE PARAMETER NOT TO CALL THE FUNCTION ITSELF
        #BECAUSE THIS command=self.show_message() CALLS THE FUNCTION NOW EVEN THOUGH THE BUTTON IS
        #STILL NOT PREPARED BECAUSE YOU ARE STILL CREATING THE BUTTON, AND THE GUI ITSELF
        #TLDR YOU ARE CALLING THE FUNCTION WHILE THE GUI IS STILL LOADING SO IT DOESNT WORK
        self.button = tk.Button(self.root, text="Show Message", font=('Arial',18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()


    def show_message(self):
        if self.check_state.get() == 0:
            #get('1.0', tk.END) THE REASON FOR THIS IS BECAUSE IN TKINTER YOU NEED TO
            # SAY WHERE YOU NEED TO GET THE TEXT FIRST, FROM BEGINNING TO THE END
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message= self.textbox.get('1.0', tk.END))
MyGUI()

#basically if checkstate is 0 then print the message from the textbox into the console but
#if it s checked and it is 1 then it will show in a messagebox