from PIL import Image, ImageTk
import tkinter as tk
import requests
from io import BytesIO
import re

class VideoGames:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1600x900")
        self.root.configure(bg="#1A1A1A")
        self.index = 0

        self.steam_urls = ["https://store.steampowered.com/api/appdetails?appids=435150",
                           "https://store.steampowered.com/api/appdetails?appids=1687950",
                           "https://store.steampowered.com/api/appdetails?appids=1222690",
                           "https://store.steampowered.com/api/appdetails?appids=307690",
                           "https://store.steampowered.com/api/appdetails?appids=753640"]
        self.steam_ids = ["435150","1687950","1222690","307690","753640"]
        #EVERYTHING IN THE INIT IS JUST PLACES AND THE WIDGETS, THERE IS NO TEXT OR IMAGE IT IS ON THE FUNCTION THAT WILL USE CONFIG
        self.tk_hd_img = None
        self.hd_label = tk.Label(self.root, bd=0, bg="#1A1A1A")
        self.hd_label.place(relx=1.0, y=50, anchor='ne', x=-40)

        self.title_label = tk.Label(self.root, bd=0, text="", font=('Arial', 30),
                                    bg="#1A1A1A", fg="white")
        self.title_label.place(x=40, y=50)

        self.description_label = tk.Label(self.root, bd=0, text="",
                                          font=('Arial', 12), bg="#1A1A1A", fg="white",
                                          wraplength=700, justify="left")
        self.description_label.place(x=40, y=120)

        self.release_label = tk.Label(self.root, bd=0, text="",
                                      font=('Arial', 14), bg="#1A1A1A", fg="white")
        self.release_label.place(x=40, y=180)

        self.developer_label = tk.Label(self.root, bd=0, text="",
                                        font=('Arial', 14), bg="#1A1A1A", fg="white")
        self.developer_label.place(x=40, y=220)

        self.publisher_label = tk.Label(self.root, bd=0, text="",
                                        font=('Arial', 14), bg="#1A1A1A", fg="white")
        self.publisher_label.place(x=40, y=260)

        self.price_label = tk.Label(self.root, bd=0, text="",
                                    font=('Arial', 14), bg="#1A1A1A", fg="white")
        self.price_label.place(x=40, y=300)

        self.minimum_specs_label = tk.Label(self.root, bd=0, text="",
                                            font=('Arial', 12), bg="#1A1A1A",
                                            fg="white", wraplength=700, justify="left")
        self.minimum_specs_label.place(x=40, y=330)

        self.recommended_specs_label = tk.Label(self.root, bd=0, text="",
                                                font=('Arial', 12),
                                                bg="#1A1A1A", fg="white",
                                                wraplength=700, justify="left")
        self.recommended_specs_label.place(x=40, y=430)

        self.genres_label = tk.Label(self.root, bd=0, text="",
                                     font=('Arial', 12), bg="#1A1A1A",
                                     fg="white", wraplength=700, justify="left")
        self.genres_label.place(x=40, y=530)

        self.website_label = tk.Label(self.root, bd=0, text="",
                                      font=('Arial', 12),
                                      bg="#1A1A1A", fg="white",
                                      wraplength=700, justify="left")
        self.website_label.place(x=40, y=560)
        self.next_button = tk.Button(self.root, text="Next", font=('Arial', 18),bg="#1A1A1A",fg="white",command=self.next_game)

        self.next_button.place(relx=1.0, y=300, anchor='ne', x=-40)
        self.next_button = tk.Button(self.root, text="Prev", font=('Arial', 18), bg="#1A1A1A", fg="white",command=self.prev_game)
        self.next_button.place(relx=1.0, y=300, anchor='ne', x=-140)

        self.load_game(self.index)
        self.root.mainloop()


    def load_game(self,index):
        self.response = requests.get(self.steam_urls[index])

        if self.response.status_code == 200:
            self.data = self.response.json()
            self.appdata = self.data[self.steam_ids[index]]["data"]


            self.header_image = self.appdata['header_image']
            self.hd_response = requests.get(self.header_image)
            self.hd_img = Image.open(BytesIO(self.hd_response.content))
            self.hd_img = self.hd_img.resize((460, 215), resample=Image.LANCZOS)
            self.tk_hd_img = ImageTk.PhotoImage(self.hd_img)
            self.hd_label.config(image=self.tk_hd_img)
            self.hd_label.image = self.tk_hd_img

            self.title_label.config(text=self.appdata["name"])

            self.description_label.config(text=self.appdata["short_description"])


            self.release_label.config(text=f"Release Date: {self.appdata['release_date']['date']}")
            # ADDS COMMA TO EVERY ITEM IN THE SELF.APPDATA LIST
            self.developer_label.config(text=f"Developer: {', '.join(self.appdata['developers'])}")
            self.publisher_label.config(text=f"Publisher: {', '.join(self.appdata['publishers'])}")

            self.price_label.config(text=f"Price: {self.appdata['price_overview']['final_formatted']}")

            minimum_specs = self.remove(self.appdata["pc_requirements"]["minimum"])
            recommended_specs = self.remove(self.appdata["pc_requirements"]["recommended"])

            self.minimum_specs_label.config(text=minimum_specs)
            self.recommended_specs_label.config(text=recommended_specs)

            self.genres_label.config(text=', '.join([a["description"] for a in self.appdata["genres"]]),)
            self.website_label.config(text="")
            self.website_label.config(text=self.appdata["website"])


    def remove(self, raw_html):
        #removes video tags in the steam api
        cleaned = re.sub(r'<video.*?</video>', ' ', raw_html, flags=re.DOTALL)
        #this one the tags anything with <>
        cleaned = re.sub(r'<.*?>', ' ', cleaned)
        #this one with links
        cleaned = re.sub(r'http\S+', ' ', cleaned)
        return cleaned.strip()

    def next_game(self):
        #len(self.steam_urls) - 1 THIS MEANS THE HIGHEST INDEX OF THE LIST SELF.STEAM_URLS
        if self.index < len(self.steam_urls) - 1:
            self.index += 1
            self.load_game(self.index)
        elif self.index == len(self.steam_urls) - 1:
            self.index = 0
            self.load_game(self.index)

    def prev_game(self):
        if self.index > 0:
            self.index -= 1
            self.load_game(self.index)
        elif self.index == 0:
            self.index = len(self.steam_urls) - 1
            self.load_game(self.index)

#NEED TO ADD VIDEO TOO MP4 ATLEAST OR USE HTML VIEWER AND PUT THE LINK OF THE VIDEO MAYBE?


test1 = VideoGames()
