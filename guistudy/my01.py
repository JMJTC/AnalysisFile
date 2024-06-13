from tkinter import *
from tkinter import messagebox


def hello():
    messagebox.showinfo("Message", "Hello World")
    print("Hello World")


class Application(Frame):
    """一个经典的GUI程序"""

    def __init__(self, master=None):
        """初始化"""
        super().__init__(master)  # 创建Frame
        self.button02 = None
        self.button01 = None
        self.master = master  # 创建主窗口
        self.pack()  # 自动调整窗口
        self.createWidgets()

    def createWidgets(self):
        """创建组件"""
        self.button01 = Button(self)
        self.button01["text"] = "Hello World"
        self.button01.pack()
        self.button01["command"] = hello

        # 创建一个退出按钮
        self.button02 = Button(self, text="Exit", command=root.destroy)
        self.button02["text"] = "Exit"
        self.button02.pack()


root = Tk()
root.geometry("400x200+200+200")
root.title("Hello World")
app = Application(master=root)

root.mainloop()
