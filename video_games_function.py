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

        self.steam_url_persona = "https://store.steampowered.com/api/appdetails?appids=1687950"
        self.response_persona = requests.get(self.steam_url_persona)

        if self.response_persona.status_code == 200:
            self.data_persona = self.response_persona.json()
        self.appdata_persona = self.data_persona["1687950"]["data"]

        #header image
        self.header_image = self.appdata_persona['header_image']
        self.hd_response = requests.get(self.header_image)
        self.hd_img = Image.open(BytesIO(self.hd_response.content))
        self.hd_img = self.hd_img.resize((460,215), resample=Image.LANCZOS)
        self.tk_hd_img = ImageTk.PhotoImage(self.hd_img)
        self.hd_label = tk.Label(self.root, image=self.tk_hd_img, bd=0)
        self.hd_label.place(relx=1.0, y=50, anchor='ne', x=-40)

        #steam api texts
        self.title_label = tk.Label(self.root, bd=0, text=self.appdata_persona["name"], font=('Arial', 30),
                                    bg="#1A1A1A", fg="white")
        self.title_label.place(x=40, y=50)

        self.description_label = tk.Label(self.root, bd=0, text=self.appdata_persona["short_description"],
                                          font=('Arial', 12), bg="#1A1A1A", fg="white", wraplength=700, justify="left")
        self.description_label.place(x=40, y=120)

        self.release_label = tk.Label(self.root, bd=0,
                                      text=f"Release Date: {self.appdata_persona['release_date']['date']}",
                                      font=('Arial', 14), bg="#1A1A1A", fg="white")
        self.release_label.place(x=40, y=180)

        self.developer_label = tk.Label(self.root, bd=0,
                                        text=f"Developer: {', '.join(self.appdata_persona['developers'])}",
                                        font=('Arial', 14), bg="#1A1A1A", fg="white")
        self.developer_label.place(x=40, y=220)

        self.publisher_label = tk.Label(self.root, bd=0,
                                        text=f"Publisher: {', '.join(self.appdata_persona['publishers'])}",
                                        font=('Arial', 14), bg="#1A1A1A", fg="white")
        self.publisher_label.place(x=40, y=260)

        self.price_label = tk.Label(self.root, bd=0,
                                    text=f"Price: {self.appdata_persona['price_overview']['final_formatted']}",
                                    font=('Arial', 14), bg="#1A1A1A", fg="white")
        self.price_label.place(x=40, y=300)

        minimum_specs = self.remove(self.appdata_persona["pc_requirements"]["minimum"])
        recommended_specs = self.remove(self.appdata_persona["pc_requirements"]["recommended"])

        self.minimum_specs_label = tk.Label(self.root, bd=0, text=minimum_specs, font=('Arial', 12), bg="#1A1A1A",
                                            fg="white", wraplength=700, justify="left")
        self.minimum_specs_label.place(x=40, y=330)

        self.recommended_specs_label = tk.Label(self.root, bd=0, text=recommended_specs, font=('Arial', 12),
                                                bg="#1A1A1A", fg="white", wraplength=700, justify="left")
        self.recommended_specs_label.place(x=40, y=430)

        self.genres_label = tk.Label(self.root, bd=0,
                                     text=', '.join([a["description"] for a in self.appdata_persona["genres"]]),
                                     font=('Arial', 12), bg="#1A1A1A", fg="white", wraplength=700, justify="left")
        self.genres_label.place(x=40, y=520)

        self.website_label = tk.Label(self.root, bd=0, text=self.appdata_persona["website"], font=('Arial', 12),
                                      bg="#1A1A1A", fg="white", wraplength=700, justify="left")
        self.website_label.place(x=40, y=560)



        self.root.mainloop()

    def remove(self, raw_html):
        #removes video tags in the steam api
        cleaned = re.sub(r'<video.*?</video>', ' ', raw_html, flags=re.DOTALL)
        #this one the tags anything with <>
        cleaned = re.sub(r'<.*?>', ' ', cleaned)
        #this one with links
        cleaned = re.sub(r'http\S+', ' ', cleaned)
        return cleaned.strip()



test1 = VideoGames()
