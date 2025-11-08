import tkinter as tk

class Login_frame(tk.Frame):

    def __init__(self,parent, controller):
        super().__init__(parent, bg="#f5f5f5")

        self.parent = parent
        self.controller = controller

        self.login_text = tk.Label(self, text="Log In", font=('THelvetica', 30), bg="#f5f5f5")
        self.login_text.pack(pady=20, padx=20)



        self.user_label = tk.Label(self, text="Username", font=('Helvetica', 13))
        self.user_label.pack(anchor="w", padx=10, pady=10)

        self.user_entry = tk.Entry(self, font=('Helvetica', 13))
        self.user_entry.pack(fill="x", padx=10)

        self.user_label = tk.Label(self, text="Password", font=('Helvetica', 13))
        self.user_label.pack(anchor="w", padx=10, pady=10)

        self.pass_entry = tk.Entry(self, font=('Helvetica', 13), show="*")
        self.pass_entry.pack(fill="x", padx=10)

        self.login_button = tk.Button(self, text="Login", font=('Helvetica', 13), bg="#a4151e", fg="white",
                                      cursor="hand2", relief="flat", command= lambda: self.controller.handle_login(self.user_entry.get(), self.pass_entry.get()))
        self.login_button.pack(fill="x", padx=10, pady=10)