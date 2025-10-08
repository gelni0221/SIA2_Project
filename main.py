# Account: admin Pass:pass


from tkinter import Tk
from ui.app_ui import App
# from db.database import init_db

def main():
    # init_db()  # ensures database and tables exist
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
