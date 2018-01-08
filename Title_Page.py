from tkinter import *
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(text = "Welcome to  Chutes and Ladders!").grid(row = 2, column = 2)

root = Tk()
app = Application(root)
root.geometry("400x400")
root.mainloop()


