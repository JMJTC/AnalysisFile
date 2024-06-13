import tkinter as tk
from login import LoginWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
