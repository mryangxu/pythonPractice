# 引入tkinter中的所有
from tkinter import *
import tkinter.messagebox as messagebox

# 从Frame派生一个类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel = Label(self, text='hello, world!')
        self.nameInput = Entry(self)
        self.nameInput.pack()
        # self.helloLabel.pack()
        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()
        # self.quitButton = Button(self, text='quit', command=self.quit)
        # self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'hello, %s' % name)

app = Application()

# 设置窗口标题
app.master.title('Hello World')

# 主消息循环
app.mainloop()