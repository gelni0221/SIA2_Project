import tkinter as tk
from tkinter import messagebox
class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        #CODE FOR THE MENUBAR DI KO NA PINANOOD MASYADO DI NAMAN ATA KAILANGAN E
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)
        #----------------------------


        self.label = tk.Label(self.root, text="Your Message", font=('Arial',18))
        self.label.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root,height=5,font=('Arial',16))
        self.textbox.bind("<KeyPress>",self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox",font=('Arial',16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial',18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial',18), command= self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        #THIS IS THE CODE TO GET THE CLOSE BUTTON ABOVE
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


    def show_message(self):
        if self.check_state.get() == 0:

            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message= self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        #THIS IS TO SEE WHEN YOU PRESS A BUTTON IT WILL SHOW THE KEYSYMBOL AND STATE OF THE KEY
        #THIS IS TO GET THAT KEYSYM AND STATE SO THAT YOU CAN USE IT TO BIND SOME FUNCTION TO YOUR
        #BUTTONS WHEN YOU PRESS THEM
        # print(event.keysym)
        # print(event.state)
        #THIS IS CTRL+ENTER
        if event.state == 44 and event.keysym == "Return":
            self.show_message()

#THIS IS FOR PROMPT WHEN CLOSING A WINDOW , SHOWS A MESSAGEBOX AND AN OPTION FOR YES OR NO
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
#FUNXTION FOR THE CLEARING TEXTBOX
    def clear(self):
        self.textbox.delete('1.0', tk.END)
MyGUI()
