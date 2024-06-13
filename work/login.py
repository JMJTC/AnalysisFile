import tkinter as tk
from tkinter import messagebox
from file_analysis import FileAnalysisWindow
from PIL import ImageTk

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("用户登录")
        self.master.geometry("900x660")
        # 背景画布
        canvas = tk.Canvas(self.master, width=900, height=500)
        image_file = ImageTk.PhotoImage(file="jmj.jpg")
        image = canvas.create_image(125, 0, anchor="nw", image=image_file)
        canvas.pack()
        self.create_widgets()

    def create_widgets(self):

        name_lable = tk.Label(self.master, text="UserName:", font=15)
        password_lable = tk.Label(self.master, text="Password:", font=15)
        name_lable.place(x=300, y=510)
        password_lable.place(x=300, y=550)

        # 用户名，用户密码输入框
        nameval = tk.StringVar()
        passwordval = tk.StringVar()
        self.username_entry = tk.Entry(self.master, textvariable=nameval, font=12)
        self.password_entry = tk.Entry(self.master, textvariable=passwordval, show="*", font=12)
        self.username_entry.place(x=400, y=515)
        self.password_entry.place(x=400, y=555)

        # self.username_entry = tk.Entry(self.master)
        # self.password_entry = tk.Entry(self.master, show="*")
        #
        # self.username_entry.grid(row=0, column=1)
        # self.password_entry.grid(row=1, column=1)

        sign_up_button=tk.Button(self.master, text="登录", command=self.login)
        sign_up_button.place(x=470, y=600)

    def login(self):
        username =self.username_entry.get()
        password = self.password_entry.get()

        if username == "陶宇" and password == "666666":  # Replace with actual validation
            self.master.destroy()
            root = tk.Tk()
            app = FileAnalysisWindow(root, username, password)
            root.protocol("WM_DELETE_WINDOW", app.on_closing)  # Ensure proper closing
            root.mainloop()
        else:
            messagebox.showerror("登录失败", "用户名或密码错误")

    def on_closing(self):
        self.master.destroy()
