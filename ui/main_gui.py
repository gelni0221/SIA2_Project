import tkinter as tk


class MainGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1360x768")
        self.root.title("Main Screen")

        self.main_text = tk.Label(self.root, text="Media and Entertainment", font=('Times New Roman', 50))
        self.main_text.pack(pady=50)

        self.widgets = tk.Frame(self.root)

        self.movies_button = tk.Button(self.widgets, text="Movies and TV Shows", font=('Times New Roman', 20), width=30, height=2)
        self.movies_button.pack(padx=10, pady=10)

        self.music_button = tk.Button(self.widgets, text="Music and Audio", font=('Times New Roman', 20), width=30, height=2)
        self.music_button.pack(padx=10)

        self.videogames_button = tk.Button(self.widgets, text="Video Games", font=('Times New Roman', 20), width=30, height=2)
        self.videogames_button.pack(padx=10, pady=10)

        self.widgets.pack()
        self.root.mainloop()


MainGUI()