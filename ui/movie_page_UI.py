
import tkinter as tk

# Frames/Sub window
class Movie_frame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,padx=100,pady=70)

        self.parent = parent
        self.controller = controller
        self.configure(background="#17120f")

        self.back_button = tk.Button(self, text="Back", bg="#17120f", fg="white",
                                     command=lambda: self.controller.show_main_menu_frame())
        self.back_button.grid(column=1, row=1,sticky="w")

        self.prev_button = tk.Button(self, text="Prev", bg="#17120f", fg="white",
                                     command=lambda: self.controller.show_main_menu_frame())
        self.prev_button.grid(column=3, row=1)

        self.next_button = tk.Button(self, text="next", bg="#17120f", fg="white",
                                     command=lambda: self.controller.show_main_menu_frame())
        self.next_button.grid(column=4, row=1)

        self.title_content = tk.Label(self,text="Im the Movie Title",font=('Helvetica', 50),bg="#17120f",fg="white")
        self.title_content.grid(column=1, row=2,padx=(0,10),sticky="w")

        self.small_details_frame = tk.Frame(self)
        self.small_details_frame.configure(background="#17120f")
        self.small_details_frame.grid(column=1, row=3,pady=(0,50),sticky="w")

        self.date_content = tk.Label(self.small_details_frame,font=("",10), text="2020",bg="#17120f",fg="white")
        self.date_content.pack(side="left")

        self.rating_content = tk.Label(self.small_details_frame,font=("",10), text="Rating", bg="#17120f", fg="white")
        self.rating_content.pack(side="left")

        self.duration_content = tk.Label(self.small_details_frame,font=("",10), text="Duration", bg="#17120f", fg="white")
        self.duration_content.pack(side="left")


        self.description_content = tk.Label(self,font=("",13),wraplength=700,justify="left",text="The evening air shimmered with the scent of rain and earth. Lanterns flickered along the narrow cobblestone street, their light bending in the puddles like liquid gold. A lone musician strummed a slow, haunting tune — the kind that made passersby pause, just for a heartbeat, before melting back into the rhythm of the night.", bg="#17120f", fg="white")
        self.description_content.grid(column=1, row=4, pady=(0,30), sticky="w")

        self.director_details_frame = tk.Frame(self)
        self.director_details_frame.configure(background="#17120f")
        self.director_details_frame.grid(column=1, row=5, pady=(0,10), sticky="w")

        self.director_header = tk.Label(self.director_details_frame,font=("",13), text="Director:", bg="#17120f", fg="white")
        self.director_header.pack(side="left")

        self.director_content = tk.Label(self.director_details_frame,font=("",13), text="Jake Arcinal", bg="#17120f", fg="white")
        self.director_content.pack(side="left")



        self.writer_details_frame = tk.Frame(self)
        self.writer_details_frame.configure(background="#17120f")
        self.writer_details_frame.grid(column=1, row=6, pady=(0, 10), sticky="w")

        self.writer_header = tk.Label(self.writer_details_frame,font=("",13), text="Writers:", bg="#17120f", fg="white")
        self.writer_header.pack(side="left")

        self.writer_content = tk.Label(self.writer_details_frame,font=("",13), text="Jake Arcinal", bg="#17120f", fg="white")
        self.writer_content.pack(side="left")



        self.actor_details_frame = tk.Frame(self)
        self.actor_details_frame.configure(background="#17120f")
        self.actor_details_frame.grid(column=1, row=7, pady=(0, 10), sticky="w")

        self.actor_header = tk.Label(self.actor_details_frame,font=("",13), text="Actors:", bg="#17120f", fg="white")
        self.actor_header.pack(side="left")

        self.actor_content = tk.Label(self.actor_details_frame,font=("",13), text="Jake Arcinal", bg="#17120f", fg="white")
        self.actor_content.pack(side="left")



        self.genre_details_frame = tk.Frame(self)
        self.genre_details_frame.configure(background="#17120f")
        self.genre_details_frame.grid(column=1, row=8, pady=(0, 10), sticky="w")

        self.genre_header = tk.Label(self.genre_details_frame,font=("",13), text="Genre:", bg="#17120f", fg="white")
        self.genre_header.pack(side="left")

        self.genre_content = tk.Label(self.genre_details_frame,font=("",13), text="epic", bg="#17120f", fg="white")
        self.genre_content.pack(side="left")







class Other_frame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)

        self.parent = parent
        self.controller = controller

        self.text = tk.Label(self, text="Im the Other window")
        self.text.pack()

        self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_main_menu_frame())
        self.back_button.pack()



