import tkinter

'''
实现登陆界面的跳转
'''
def enter():
    root=tkinter.Tk()
    root.title('信息界面')
    root['width'] = 400
    root['height'] = 400
    label1=tkinter.Label(root,text='请登陆')
    babel_button=tkinter.Button(root,text='登陆',command=root.destroy)
    label1.place(x=100,y=100)
    babel_button.place(x=100,y=200)
    root.mainloop()

if __name__ == '__main__':
    #先调用enter界面，使用完界面后，就毁掉这个界面，然后再继续运行下面的程序，调用下一个界面
    enter()
    #下面就是下一个界面
    admin=tkinter.Tk()
    admin['width']=400
    admin['height']=400
    admin.title('欢迎进入管理员登陆界面')
    label1=tkinter.Label(admin,text='信息界面',height=3)
    label1.place(x=100,y=100)
    admin.mainloop()