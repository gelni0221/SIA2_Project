from PIL import Image, ImageTk
import tkinter as tk
import requests
from io import BytesIO

url = "https://sm.ign.com/t/ign_nordic/review/p/persona-5-/persona-5-review_htue.1280.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img = img.resize((450, 675),resample=Image.LANCZOS)


root = tk.Tk()
tk_img = ImageTk.PhotoImage(img)

label = tk.Label(root, image=tk_img)
label.pack()
root.mainloop()




