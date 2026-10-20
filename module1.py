from Tkinter import *

class MyApp:                         ### (1)
    def __init__(self, myParent):
        self.myParent = myParent
        self.myParent.minsize(290, 700)
        self.myContainer1 = Frame(self.myParent)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1["text"]= "Hello, World!"
        self.button1["background"] = "green"
        self.button1.bind("<Button-1>", self.button1Click)
        self.button1.pack()

        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="Off to join the circus!") ### (2)
        self.button2.configure(background="tan")
        self.button2.bind("<Button-1>", self.button2Click)
        self.button2.pack()


        self.button3 = Button(self.myContainer1)
        self.button3.configure(text="Join me?", background="cyan")  ### (3)
        self.button3.pack(side=LEFT)

        self.button4 = Button(self.myContainer1, text="Goodbye!", background="red") ### (4)
        self.button4.pack( side=LEFT)


    def button1Click(self, event):    ### (3)
        if self.button1["background"] == "green": ### (4)
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"

    def button2Click(self, event):  ### (5)
        self.myParent.destroy()     ### (6)




root = Tk()
myapp = MyApp(root)  ### (2)
root.mainloop()      ### (3)


