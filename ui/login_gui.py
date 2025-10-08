import tkinter as tk

class LoginGUI:

    def __init__(self):
        self.root = tk.Tk()
        # self.root.geometry("1360x768")
        self.root.geometry("300x400")
        self.root.configure(bg="#f5f5f5")
        self.root.title("Login Screen")

        self.login_text = tk.Label(self.root, text="Log In", font=('THelvetica',30), bg="#f5f5f5")
        self.login_text.pack(pady=20, padx=20)
        self.widgets = tk.Frame(self.root, bg="#f5f5f5")

        self.user_label = tk.Label(self.widgets, text="Username", font=('Helvetica',13))
        self.user_label.pack(anchor="w", padx=10, pady=10)

        self.user_entry = tk.Entry(self.widgets, font=('Helvetica',13))
        self.user_entry.pack(fill="x", padx=10)

        self.user_label = tk.Label(self.widgets, text="Password", font=('Helvetica', 13))
        self.user_label.pack(anchor="w", padx=10, pady=10)

        self.pass_entry = tk.Entry(self.widgets, font=('Helvetica', 13))
        self.pass_entry.pack(fill="x", padx=10)

        self.login_button = tk.Button(self.widgets,text="Login" ,font=('Helvetica', 13), bg="#a4151e",fg = "white", cursor="hand2", relief= "flat" )
        self.login_button.pack(fill="x", padx=10, pady=10)

        self.widgets.pack(pady=20, padx=10,fill="both", expand=True)
        self.root.mainloop()

LoginGUI()