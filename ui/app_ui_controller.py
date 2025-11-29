
from controllers.auth_controller import login
from tkinter import messagebox
import tkinter as tk
from ui.movie_page_frame import Movie_frame
from ui.login_frame import Login_frame
from ui.main_frame import Main_frame
from ui.music_page_frame import Music_frame
from ui.videogames_frame import game_frame


class App:

    def __init__(self,root):
        self.root = root
        self.root.geometry("300x400")
        self.root.configure(bg="#f5f5f5")
        self.root.title("Login Screen")

        self.login_frame = Login_frame(self.root, self)
        self.main_frame = Main_frame(self.root, self)
        self.movie_frame = Movie_frame(self.root, self)
        self.music_frame = Music_frame(self.root, self)
        self.game_frame = game_frame(self.root, self)

        # self.show_login_frame()
    #   test
        self.show_main_menu_frame()

    def handle_login(self, username, password):
        if login(username, password):
            self.show_main_menu_frame()
            messagebox.showinfo("Success!", "Log In Successful")
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    def show_login_frame(self):
        self.login_frame.pack(pady=20, padx=10, fill="both", expand=True)


    # integrated main menu frame
    def show_main_menu_frame(self):
        self.login_frame.pack_forget()
        self.movie_frame.pack_forget()
        self.music_frame.pack_forget()
        self.game_frame.pack_forget()
        self.main_frame.pack()
        self.root.configure(bg="#17120f")
        self.root.geometry("1360x768")
        self.root.title("Main Screen")


    def show_movie_frame(self):
        self.main_frame.pack_forget()
        self.movie_frame.pack(fill="both", expand=True)
    def show_music_frame(self):
        self.main_frame.pack_forget()
        self.music_frame.pack()
    def show_game_frame(self):
        self.main_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)


