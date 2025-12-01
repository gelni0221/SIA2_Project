from os.path import split

from PIL import Image, ImageTk
import tkinter as tk
from models.movie import get_next_movie,get_prev_movie
from tkvideo.tkvideo import tkvideo

# Frames/Sub window
class Movie_frame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,padx=110,pady=40)

        self.parent = parent
        self.controller = controller
        self.configure(background="#17120f")

        self.movie_id = 0


        # UPPER HEADER
        self.back_button = tk.Button(self, text="Back", bg="#17120f", fg="white",
                                     command=lambda: self.controller.show_main_menu_frame())
        self.back_button.grid(column=1, row=1,sticky="w")

        self.prev_button = tk.Button(self, text="Prev", bg="#17120f", fg="white",
                                     command=self.prev_movie)
        self.prev_button.grid(column=3, row=1,sticky="e")

        self.next_button = tk.Button(self, text="next", bg="#17120f", fg="white",
                                     command=self.next_movie)
        self.next_button.grid(column=4, row=1,sticky="e")



        # DETAILS FRAME (LEFT SIDE)
        self.details_frame = tk.Frame(self)
        self.details_frame.configure(background="#17120f")
        self.details_frame.grid(column=1, row=2 ,ipadx=70, pady=30, sticky="nw")


        self.title_content = tk.Label(self.details_frame,wraplength=700, text="Im the Movie Title",font=('Helvetica', 50),justify="left",bg="#17120f",fg="white")
        self.title_content.pack(anchor="w")

        self.small_details_frame = tk.Frame(self.details_frame)
        self.small_details_frame.configure(background="#17120f")
        self.small_details_frame.pack(anchor="nw", padx=5)

        self.date_content = tk.Label(self.small_details_frame,font=("",10), text="2020",bg="#17120f",fg="white")
        self.date_content.pack(side="left")

        self.rating_content = tk.Label(self.small_details_frame,font=("",10), text="Rating", bg="#17120f", fg="white")
        self.rating_content.pack(side="left")

        self.duration_content = tk.Label(self.small_details_frame,font=("",10), text="Duration", bg="#17120f", fg="white")
        self.duration_content.pack(side="left")


        self.description_content = tk.Label(self.details_frame,font=("",13),wraplength=700,justify="left",text="The evening air shimmered with the scent of rain and earth. Lanterns flickered along the narrow cobblestone street, their light bending in the puddles like liquid gold. A lone musician strummed a slow, haunting tune — the kind that made passersby pause, just for a heartbeat, before melting back into the rhythm of the night.", bg="#17120f", fg="white")
        self.description_content.pack(anchor="nw")

        self.director_details_frame = tk.Frame(self.details_frame)
        self.director_details_frame.configure(background="#17120f")
        self.director_details_frame.pack(anchor="w")

        self.director_header = tk.Label(self.director_details_frame,font=("",13), text="Director:", bg="#17120f", fg="white")
        self.director_header.pack(side="left")

        self.director_content = tk.Label(self.director_details_frame,font=("",13), text="Jake Arcinal", bg="#17120f", fg="white")
        self.director_content.pack(side="left")



        self.writer_details_frame = tk.Frame(self.details_frame)
        self.writer_details_frame.configure(background="#17120f")
        self.writer_details_frame.pack(anchor="w")

        self.writer_header = tk.Label(self.writer_details_frame,font=("",13), text="Writers:", bg="#17120f", fg="white")
        self.writer_header.pack(side="left")

        self.writer_content = tk.Label(self.writer_details_frame,font=("",13),wraplength=700, text="Jake Arcinal", bg="#17120f", fg="white")
        self.writer_content.pack(side="left")



        self.actor_details_frame = tk.Frame(self.details_frame)
        self.actor_details_frame.configure(background="#17120f")
        self.actor_details_frame.pack(anchor="nw")

        self.actor_header = tk.Label(self.actor_details_frame,font=("",13), text="Actors:", bg="#17120f", fg="white")
        self.actor_header.pack(side="left")

        self.actor_content = tk.Label(self.actor_details_frame,font=("",13),wraplength=700, text="Jake Arcinal", bg="#17120f", fg="white")
        self.actor_content.pack(side="left")



        self.genre_details_frame = tk.Frame(self.details_frame)
        self.genre_details_frame.configure(background="#17120f")
        self.genre_details_frame.pack(anchor="w")

        self.genre_header = tk.Label(self.genre_details_frame,font=("",13), text="Genre:", bg="#17120f", fg="white")
        self.genre_header.pack(side="left")

        self.genre_content = tk.Label(self.genre_details_frame,font=("",13), text="epic", bg="#17120f", fg="white")
        self.genre_content.pack(side="left")


        # RIGHT SIDE POSTER
        self.movie_poster = tk.Label(self)
        self.movie_poster.image = ""
        self.movie_poster.grid(column=2, row=2, columnspan=3, rowspan=2, sticky="e")

        # TRAILER SECTION
        self.video_frame = tk.Label(self)

        # Load first content
        self.next_movie()


    def load_movie(self, content):
        self.title_content.config(text=content["title"])

        self.date_content.config(text=content["date"])

        full_rating = f"★{content['rating']}/10"

        self.rating_content.config(text=full_rating)

        full_duration = f"{content['duration']} mins"

        self.duration_content.config(text=full_duration)

        self.description_content.config(text=content["description"])

        full_director = content["director"].replace("[", "").replace("]", "").replace('"', "")

        self.director_content.config(text=full_director)

        full_writer = content["writer"].replace("[", "").replace("]", "").replace('"', "")

        self.writer_content.config(text=full_writer)

        full_actor = content["actor"].replace("[", "").replace("]", "").replace('"', "")

        self.actor_content.config(text=full_actor)

        full_genre = content["genre"].replace("[", "").replace("]", "").replace('"', "")

        self.genre_content.config(text=full_genre)


        self.img = Image.open(f"resources/{content['poster']}")
        self.img = self.img.resize((290, 483))

        # Convert for Tkinter
        self.photo = ImageTk.PhotoImage(self.img)
        self.movie_poster.config(image=self.photo)
        self.movie_poster.image = self.photo

        self.video_frame.destroy()
        self.video_frame = tk.Label(self)
        self.video_frame.grid(column=1, row=3, columnspan=1, sticky="w")
        self.trailer_path = f"resources/{content['video']}"  # replace with your file
        self.player = tkvideo(self.trailer_path, self.video_frame, loop=1, size=(640, 360))
        self.player.play()



    def next_movie(self):
        self.content = get_next_movie(self.movie_id)
        if not self.content:
            self.movie_id = 0
            self.content = get_next_movie(self.movie_id)
        self.load_movie(self.content)
        self.movie_id = self.content["id"]

    def prev_movie(self):
        self.content = get_prev_movie(self.movie_id)
        if not self.content:
            self.movie_id = 0
            self.content = get_next_movie(self.movie_id)
        self.load_movie(self.content)
        self.movie_id = self.content["id"]




