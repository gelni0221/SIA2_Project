import tkinter as tk

class LoginGUI:

    def __init__(self):
        self.root = tk.Tk()
        # self.root.geometry("1360x768")
        self.root.geometry("300x500")
        self.root.title("Login Screen")

        self.login_text = tk.Label(self.root, text="Log In", font=('Times New Roman',30))
        self.login_text.pack(pady=30)

        self.widgets = tk.Frame(self.root)

        self.user_label = tk.Label(self.widgets, text="Username", font=('Times New Roman',13))
        self.user_label.pack(anchor="w", padx=10, pady=10)

        self.user_entry = tk.Entry(self.widgets, font=('Times New Roman',13))
        self.user_entry.pack(anchor="w", padx=10)

        self.user_label = tk.Label(self.widgets, text="Password", font=('Times New Roman', 13))
        self.user_label.pack(anchor="w", padx=10, pady=10)

        self.pass_entry = tk.Entry(self.widgets, font=('Times New Roman', 13))
        self.pass_entry.pack(anchor="w", padx=10)

        self.login_button = tk.Button(self.widgets,text="Login" ,font=('Times New Roman', 13))
        self.login_button.pack(anchor="w", padx=10, pady=10)

        self.create_button = tk.Button(self.widgets, text="Create Account", font=('Times New Roman', 13))
        self.create_button.pack(anchor="w", padx=10)
        
        
        self.widgets.pack(fill="x")
        self.root.mainloop()

LoginGUI()