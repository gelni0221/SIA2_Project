
import tkinter as tk

class Main_frame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)

        self.parent = parent
        self.controller = controller

        self.configure(background="#17120f")


        self.main_text = tk.Label(self, text="Media and Entertainment", font=('Helvetica', 50), bg="#17120f",
                                  fg="white")
        self.main_text.pack(pady=50)


        self.movies_button = tk.Button(self, text="Movies and TV Shows", font=('Helvetica', 20), width=30,
                                       height=2, relief="ridge", bg="#a4151e", fg="white", cursor="hand2",
                                       command=self.controller.show_movie_frame)
        self.movies_button.pack(padx=10, pady=10)

        self.music_button = tk.Button(self, text="Music and Audio", font=('Helvetica', 20), width=30, height=2,
                                      relief="ridge", bg="#a4151e", fg="white", cursor="hand2",
                                      command=self.controller.show_music_frame)
        self.music_button.pack(padx=10)

        self.video_games_button = tk.Button(self, text="Video Games", font=('Helvetica', 20), width=30,
                                            height=2, relief="ridge", bg="#a4151e", fg="white", cursor="hand2",
                                            command=self.controller.show_game_frame)
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



