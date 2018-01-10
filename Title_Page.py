from tkinter import *
import random

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

    def page_three(self):
        self.next_bttn.destroy()
        imageSmall = PhotoImage(file="Board.JPG")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=5, column=1)

    def dice_roll_number(self):
        dice_roll = random.randint(1,7)

    def dice(self):
        imageSmall = PhotoImage(file="Dice"+ str(self.dice_roll_number) +".gif")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=5, column=1)




root = Tk()
app = Application(root)
root.geometry("400x600")
root.mainloop()