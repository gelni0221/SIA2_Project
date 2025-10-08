import tkinter as tk


class MainGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="#17120f")
        self.root.geometry("1360x768")
        self.root.title("Main Screen")

        self.main_text = tk.Label(self.root, text="Media and Entertainment", font=('Helvetica', 50), bg="#17120f",fg = "white")
        self.main_text.pack(pady=50)

        self.widgets = tk.Frame(self.root, bg="#e2e4de")

        self.movies_button = tk.Button(self.widgets, text="Movies and TV Shows", font=('Helvetica', 20), width=30, height=2, relief="ridge", bg="#a4151e",fg = "white", cursor="hand2")
        self.movies_button.pack(padx=10, pady=10)

        self.music_button = tk.Button(self.widgets, text="Music and Audio", font=('Helvetica', 20), width=30, height=2, relief="ridge", bg="#a4151e",fg = "white", cursor="hand2")
        self.music_button.pack(padx=10)

        self.video_games_button = tk.Button(self.widgets, text="Video Games", font=('Helvetica', 20), width=30, height=2, relief="ridge", bg="#a4151e",fg = "white", cursor="hand2")
        self.video_games_button.pack(padx=10, pady=10)

        #function for button hovering
        #main
        def on_enter(e):e.widget.config(bg="#c2393e")
        #hover
        def on_leave(e):e.widget.config(bg="#a4151e")

        self.music_button.bind("<Enter>", on_enter)
        self.music_button.bind("<Leave>", on_leave)
        self.video_games_button.bind("<Enter>", on_enter)
        self.video_games_button.bind("<Leave>", on_leave)
        self.movies_button.bind("<Enter>", on_enter)
        self.movies_button.bind("<Leave>", on_leave)

        self.widgets.pack()
        self.root.mainloop()


MainGUI()