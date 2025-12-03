from PIL import Image, ImageTk
import tkinter as tk
import pygame


class Music_frame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        pygame.mixer.init()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.index = 0
        self.song_data = [
            {
                "Title": "Color Your Night",
                "Artist/Band": "Azumi Takahashi & Lotus Juice",
                "Album": "Persona 3 Reload Original Soundtrack",
                "Release Date": "April 24, 2024"
            },
            {
                "Title": "I Don't Care",
                "Artist/Band": "2NE1",
                "Album": "2NE1 (1st Mini Album/EP)",
                "Release Date": "July 1, 2009"
            },
            {
                "Title": "High Hopes",
                "Artist/Band": "Kodaline",
                "Album": "In a Perfect World",
                "Release Date": "March 15, 2013 (Single Release)"
            },
            {
                "Title": "Ikaw Ang Iibigin Ko",
                "Artist/Band": "Jos Garcia",
                "Album": "The Versatile",
                "Release Date": "2006 (First Released)"
            },
            {
                "Title": "Need 2",
                "Artist/Band": "Pinegrove",
                "Album": "Mixtape Two / Everything So Far ",
                "Release Date": "May 29, 2014 (Original Release)"
            }
        ]

        self.song_posters = ["song1_poster.jpg","song2_poster.jpg","song3_poster.jpg","song4_poster.jpg","song5_poster.jpg"]
        self.songs_mp3 = ["song1.mp3", "song2.mp3", "song3.mp3", "song4.mp3","song5.mp3"]
        self.parent = parent
        self.controller = controller
        self.configure(background="#17120f")

        # WHOLE FRAME OF ALL FRAMES
        self.full_container = tk.Frame(self, bg="#17120f")
        self.full_container.grid(column=0, row=0, sticky="nsew")

        self.full_container.grid_rowconfigure(0, weight=0)
        self.full_container.grid_rowconfigure(1, weight=1)
        self.full_container.grid_columnconfigure(0, weight=1)
        self.full_container.grid_columnconfigure(1, weight=1)

        #UPPER BUTTONS
        self.upper_frame = tk.Frame(self.full_container, bg="#17120f")
        self.upper_frame.grid(column=0, row=0, columnspan=2, sticky="ew")
        self.upper_frame.grid_propagate(False)
        self.upper_frame.config(width=1366, height=60)
        self.upper_frame.grid_columnconfigure(1, weight=1)

        self.back_button = tk.Button(self.upper_frame, text="Back", bg="#17120f", fg="white", width=8, height=2,
                                     command=lambda: self.controller.show_main_menu_frame())
        self.back_button.grid(column=0, row=0, sticky="w", padx=20, pady=20)

        # LEFT CONTAINER
        self.left_container = tk.Frame(self.full_container, bg="#17120f")
        self.left_container.grid(column=0, row=1, sticky='nsew', padx=20, pady=20)

        self.music_img = None
        self.music_poster = tk.Label(self.left_container)
        self.music_poster.pack(anchor="nw")

        self.title_content = tk.Label(self.left_container, text="", font=('Helvetica', 50),
                                      justify="left", bg="#17120f", fg="white")
        self.title_content.pack(anchor="nw")

        self.artist_content = tk.Label(self.left_container, text="", font=('Helvetica', 20),
                                       justify="left", bg="#17120f", fg="white")
        self.artist_content.pack(anchor="nw")

        self.album_content = tk.Label(self.left_container, text="", font=('Helvetica', 20),
                                      justify="left", bg="#17120f", fg="white")
        self.album_content.pack(anchor="nw")

        self.release_date_content = tk.Label(self.left_container, text="", font=('Helvetica', 20),
                                             justify="left", bg="#17120f", fg="white")
        self.release_date_content.pack(anchor="nw")

        self.prev_button = tk.Button(self.left_container, text="Prev", bg="#17120f", fg="white", width=8, height=2,command=lambda: self.prev_music())
        self.prev_button.pack(side="left", padx=10, pady=10)

        self.play_button = tk.Button(self.left_container, text="Play", bg="#17120f", fg="white", width=8, height=2, command=lambda: self.start_music(self.index))
        self.play_button.pack(side="left", padx=10, pady=10)

        self.next_button = tk.Button(self.left_container, text="Next", bg="#17120f", fg="white", width=8, height=2,command=lambda: self.next_music())
        self.next_button.pack(side="left", padx=10, pady=10)

        self.pause_button = tk.Button(self.left_container, text="Pause", bg="#17120f", fg="white", width=8, height=2,
                                     command=lambda: self.pause_music())
        self.pause_button.pack(anchor="nw",side="left", padx=10, pady=10)
        self.unpause_button = tk.Button(self.left_container, text="Unpause", bg="#17120f", fg="white", width=8, height=2,
                                      command=lambda: self.resume_music())
        self.unpause_button.pack(anchor="nw", side="left", padx=10, pady=10)
        self.load_music()

        # RIGHT CONTAINER
        self.right_container = tk.Frame(self.full_container, bg="#17120f")
        self.right_container.grid(column=1, row=1, sticky='nsew', padx=20, pady=20)
        self.right_container.grid_columnconfigure(0, weight=1)
        self.right_container.grid_rowconfigure(0, weight=1)
        self.load_musiclist()

    def load_music(self):
        self.music_img = Image.open(f"resources/{self.song_posters[self.index]}")
        self.img = self.music_img.resize((300, 300))
        self.poster_img = ImageTk.PhotoImage(self.img)
        self.music_poster.config(image=self.poster_img)
        self.music_poster.image = self.poster_img
        self.title_content.config(text=f"{self.song_data[self.index]['Title']}")
        self.artist_content.config(text=f"{self.song_data[self.index]['Artist/Band']}")
        self.album_content.config(text=f"{self.song_data[self.index]['Album']}")
        self.release_date_content.config(text=f"{self.song_data[self.index]['Release Date']}")

    def load_musiclist(self):
        song_count = len(self.songs_mp3)
        for i in range(song_count):
            btn = tk.Button(self.right_container,
                            text=f"{self.song_data[i]['Title']} - {self.song_data[i]['Artist/Band']}",
                            bg="#17120f", fg="white")
            btn.pack(fill="x", padx=10, pady=5)
            btn.config(command=lambda idx=i: [self.stop_music(), self.play_music(idx)])


    def play_music(self, index):
        self.index = index
        self.music_img = Image.open(f"resources/{self.song_posters[self.index]}")
        self.img = self.music_img.resize((300, 300))
        self.poster_img = ImageTk.PhotoImage(self.img)
        self.music_poster.config(image=self.poster_img)
        self.music_poster.image = self.poster_img
        self.title_content.config(text=f"{self.song_data[self.index]['Title']}")
        self.artist_content.config(text=f"{self.song_data[self.index]['Artist/Band']}")
        self.album_content.config(text=f"{self.song_data[self.index]['Album']}")
        self.release_date_content.config(text=f"{self.song_data[self.index]['Release Date']}")


    def next_music(self):
        if self.index < len(self.songs_mp3) - 1:
            self.index += 1
        elif self.index == len(self.songs_mp3) - 1:
            self.index = 0
        self.load_music()
        self.stop_music()

    def prev_music(self):
        if self.index > 0 < len(self.songs_mp3):
            self.index -= 1
        elif self.index == 0:
            self.index = len(self.songs_mp3) - 1
        self.load_music()
        self.stop_music()

    def start_music(self, index):
        self.index = index
        pygame.mixer.music.load(f"resources/{self.songs_mp3[self.index]}")
        pygame.mixer.music.play()


    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()
