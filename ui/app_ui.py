
from controllers.auth_controller import login
from tkinter import messagebox
import tkinter as tk

class App:

    def __init__(self,root):
        self.root = root
        self.root.geometry("300x400")
        self.root.configure(bg="#f5f5f5")
        self.root.title("Login Screen")

        self.login_text = tk.Label(self.root, text="Log In", font=('THelvetica',30), bg="#f5f5f5")
        self.login_text.pack(pady=20, padx=20)

        self.widgets = tk.Frame(self.root, bg="#f5f5f5")
        self.widgets.pack(pady=20, padx=10, fill="both", expand=True)

        self.user_label = tk.Label(self.widgets, text="Username", font=('Helvetica',13))
        self.user_label.pack(anchor="w", padx=10, pady=10)

        self.user_entry = tk.Entry(self.widgets, font=('Helvetica',13))
        self.user_entry.pack(fill="x", padx=10)

        self.user_label = tk.Label(self.widgets, text="Password", font=('Helvetica', 13))
        self.user_label.pack(anchor="w", padx=10, pady=10)

        self.pass_entry = tk.Entry(self.widgets, font=('Helvetica', 13),show="*")
        self.pass_entry.pack(fill="x", padx=10)

        self.login_button = tk.Button(self.widgets,text="Login" ,font=('Helvetica', 13), bg="#a4151e",fg = "white", cursor="hand2", relief= "flat", command=self.handle_login)
        self.login_button.pack(fill="x", padx=10, pady=10)


        self.root.mainloop()

    def handle_login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        if login(username,password):
            self.show_main_menu()
            messagebox.showinfo("Success!","Log In Successful")
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    def show_main_menu(self):
        self.widgets.pack_forget()
        self.login_text.pack_forget()
        self.root.configure(bg="#17120f")
        self.root.geometry("1360x768")
        self.root.title("Main Screen")

        self.main_text = tk.Label(self.root, text="Media and Entertainment", font=('Helvetica', 50), bg="#17120f",
                                  fg="white")
        self.main_text.pack(pady=50)

        self.widgets = tk.Frame(self.root, bg="#e2e4de")

        self.movies_button = tk.Button(self.widgets, text="Movies and TV Shows", font=('Helvetica', 20), width=30,
                                       height=2, relief="ridge", bg="#a4151e", fg="white", cursor="hand2")
        self.movies_button.pack(padx=10, pady=10)

        self.music_button = tk.Button(self.widgets, text="Music and Audio", font=('Helvetica', 20), width=30, height=2,
                                      relief="ridge", bg="#a4151e", fg="white", cursor="hand2")
        self.music_button.pack(padx=10)

        self.video_games_button = tk.Button(self.widgets, text="Video Games", font=('Helvetica', 20), width=30,
                                            height=2, relief="ridge", bg="#a4151e", fg="white", cursor="hand2")
        self.video_games_button.pack(padx=10, pady=10)

        # function for button hovering
        # main
        def on_enter(e): e.widget.config(bg="#c2393e")

        # hover
        def on_leave(e): e.widget.config(bg="#a4151e")

        self.music_button.bind("<Enter>", on_enter)
        self.music_button.bind("<Leave>", on_leave)
        self.video_games_button.bind("<Enter>", on_enter)
        self.video_games_button.bind("<Leave>", on_leave)
        self.movies_button.bind("<Enter>", on_enter)
        self.movies_button.bind("<Leave>", on_leave)

        self.widgets.pack()


