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
        self.header_image = "https://images.steamusercontent.com/ugc/2019355369832417157/0589A1EE3E6E97247D21B72A5DBB8E25ECAC171F/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"
        self.capsule_image = "https://cdn.cloudflare.steamstatic.com/steam/apps/1687950/capsule_184x69.jpg"
        self.background = "https://store.akamai.steamstatic.com/images/storepagebackground/app/1687950?t=1733297467"

        # self.bg_response = requests.get(self.background)
        # self.bg_img = Image.open(BytesIO(self.bg_response.content))
        # self.bg_img = self.bg_img.resize((1920,1080), resample=Image.LANCZOS)
        # self.tk_bg_img = ImageTk.PhotoImage(self.bg_img)
        # self.bg_label = tk.Label(self.root, image= self.tk_bg_img, bd=0)
        # self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.hd_response = requests.get(self.header_image)
        self.hd_img = Image.open(BytesIO(self.hd_response.content))
        self.hd_img = self.hd_img.resize((616,353), resample=Image.LANCZOS)
        self.tk_hd_img = ImageTk.PhotoImage(self.hd_img)
        self.hd_label = tk.Label(self.root, image=self.tk_hd_img, bd=0)
        self.hd_label.place(relx=1.0, y=50, anchor='ne', x=-40)
        self.title_label = tk.Label(self.root, bd=0, text="Persona 5 Royal",font=('Arial', 30), bg="#1A1A1A", fg="white" )
        self.title_label.place(x=40, y=50)

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
