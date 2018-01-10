from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets_page_one()

    def create_widgets_page_one(self):
        self.label = Label(text="Welcome to  Chutes and Ladders!")
        self.label.grid(row = 2, column = 2)

        self.next_bttn = Button(self, text="Next", command=self.page_three)
        self.next_bttn.grid(row=1, column=1)


    def page_two(self):
        self.next_bttn.destroy()
        imageSmall = PhotoImage(file="Board.gif")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=5, column=1)



    def board_spaces(self):
        user_space = 0
        second_user_space = 0
        #dictionary
root = Tk()
app = Application(root)
root.geometry("400x600")
root.mainloop()