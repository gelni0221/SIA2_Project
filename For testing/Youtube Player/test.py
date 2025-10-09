from tkinter import Tk
from tkhtmlview import HTMLLabel

root = Tk()
root.title("YouTube Player")

video_id = "dQw4w9WgXcQ"
html_code = f"""
<iframe width="560" height="315"
src="https://www.youtube.com/embed/{video_id}"
frameborder="0" allowfullscreen></iframe>
"""

label = HTMLLabel(root, html=html_code)
label.pack(padx=20, pady=20)

root.mainloop()