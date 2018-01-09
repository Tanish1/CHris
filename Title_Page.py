from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def page_one(self):
        self.label = Label(text="Welcome to  Chutes and Ladders!")
        self.label.grid(row = 2, column = 2)

        self.next_bttn = Button(self, text="Next", command=self.page_two)
        self.next_bttn.grid(row=1, column=1)

    def page_two(self):
        self.label["text"]= "IT WORKED"
        self.next_bttn.destroy()


root = Tk()
app = Application(root)
root.geometry("400x400")
root.mainloop()
