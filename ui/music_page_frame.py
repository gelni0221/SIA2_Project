from PIL import Image, ImageTk
import tkinter as tk


class Music_frame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)


        self.parent = parent
        self.controller = controller
        self.configure(background="#17120f")

        # UPPER BUTTONS
        self.upper_frame = tk.Frame(self)
        self.upper_frame.grid(column=1, row=1, columnspan=2)

        self.back_button = tk.Button(self.upper_frame, text="Back", bg="#17120f", fg="white",
                                     command=lambda: self.controller.show_main_menu_frame())
        self.back_button.pack()

        self.prev_button = tk.Button(self.upper_frame, text="Prev", bg="#17120f", fg="white",
                                     )
        self.prev_button.pack()

        self.next_button = tk.Button(self.upper_frame, text="next", bg="#17120f", fg="white",
                                     )
        self.next_button.pack()



        # LEFT SIDE DETAILS
        self.left_frame = tk.Frame(self)
        self.left_frame.grid(column=1, row=2)

        # Display
        self.movie_poster = tk.Label(self.left_frame)
        self.movie_poster.image = ""
        self.movie_poster.pack(anchor="nw")

        self.title_content = tk.Label(self.left_frame, text="Im the Song Title", font=('Helvetica', 50),
                                      justify="left", bg="#17120f", fg="white")
        self.title_content.pack(anchor="nw")

        self.artist_content = tk.Label(self.left_frame, text="Im the Musician", font=('Helvetica', 20),
                                      justify="left", bg="#17120f", fg="white")
        self.artist_content.pack(anchor="nw")

        self.album_content = tk.Label(self.left_frame, text="Im the album", font=('Helvetica', 20),
                                      justify="left", bg="#17120f", fg="white")
        self.album_content.pack(anchor="nw")

        # Music controls here



        # RIGHT SIDE DETAILS
        self.right_frame = tk.Frame(self)
        self.right_frame.grid(column=2, row=2)

        





