from tkinter import *
import random

class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets_page_one()
        self.rolled_number = Label(self, text="")

    def create_widgets_page_one(self):
        self.label = Label(text="Welcome to  Chutes and Ladders!")
        self.label.grid(row = 2, column = 2)

        self.next_bttn = Button(self, text="Next", command=self.page_three)
        self.next_bttn.grid(row=1, column=1)

    def page_three(self):
        self.next_bttn.destroy()
        self.label.destroy()
        self.roll_button = Button(self, text = "Roll",command = self.dice_roll_number)
        self.roll_button.grid(row=100, column = 4)
        imageSmall = PhotoImage(file="Board.jpg")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=5, column=1, columnspan = 8)
        self.rolled_number = Label(text = "")
        self.rolled_number.grid(row = 6, column = 4)

    def dice_roll_number(self):
        dice_roll = random.randint(1,7)
        self.rolled_number["text"] = dice_roll

    def dice(self):
        imageSmall = PhotoImage(file="Dice"+ str(self.dice_roll_number) +".gif")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=5, column=1)




root = Tk()
app = Application(root)
root.geometry("400x600")
root.mainloop()
ds