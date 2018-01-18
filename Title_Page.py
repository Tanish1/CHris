from tkinter import *
import random



class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets_page_one()
        self.rolled_number = Label(self, text="")
        self.var = 0

    def create_widgets_page_one(self):
        self.label = Label(text="Welcome to  Chutes and Ladders!")
        self.label.grid(row = 2, column = 2)

        self.next_bttn = Button(self, text="Next", command=self.page_three)
        self.next_bttn.grid(row=1, column=1)

    def page_three(self):
        self.next_bttn.destroy()
        self.label.destroy()
        self.roll_button = Button(self, text = "Roll",command = self.dice_roll_number)

        self.roll_button.grid(row=7, column = 4)
        imageSmall = PhotoImage(file="Board.jpg")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=5, column=1, columnspan = 8)

        self.rolled_number = Label(self, text = "")
        self.rolled_number.grid(row = 7, column = 4)

    def dice_roll_number(self):
        dice_roll = random.randint(1,6)
        self.var += dice_roll
        self.move_player()
        print(self.player_pos)
        self.rolled_number["text"] = "You rolled a " + str(dice_roll)
        self.rolled_number["text"] = "You're at space " + str(self.var)
        imageSmall = PhotoImage(file="Photos/Dice" + str(dice_roll) +".gif")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=8, column=2)

    def move_player(self):
        self.board = []
        for i in range(100):
            self.board.append(cell())
        self.player_pos = self.var
        if self.player_pos == 1:
            self.player_pos = 38
            self.var = self.player_pos
        if self.player_pos == 4:
            self.player_pos = 14
            self.var = self.player_pos
        if self.player_pos == 9:
            self.player_pos = 31
            self.var = self.player_pos
        if self.player_pos == 16:
            self.player_pos = 6
            self.var = self.player_pos
        if self.player_pos == 21:
            self.player_pos = 42
            self.var = self.player_pos
        if self.player_pos == 36:
            self.player_pos = 44
            self.var = self.player_pos
        if self.player_pos == 47:
            self.player_pos = 26
            self.var = self.player_pos
        if self.player_pos == 49:
            self.player_pos = 11
            self.var = self.player_pos
        if self.player_pos == 51:
            self.player_pos = 67
            self.var = self.player_pos
        if self.player_pos == 56:
            self.player_pos = 53
            self.var = self.player_pos
        if self.player_pos == 62:
            self.player_pos = 19
            self.var = self.player_pos
        if self.player_pos == 64:
            self.player_pos = 60
            self.var = self.player_pos
        if self.player_pos == 71:
            self.player_pos = 91
            self.var = self.player_pos
        if self.player_pos == 80:
            self.player_pos = 100
            self.var = self.player_pos
        if self.player_pos == 87:
            self.player_pos = 24
            self.var = self.player_pos
        if self.player_pos == 93:
            self.player_pos = 73
            self.var = self.player_pos
        if self.player_pos == 95:
            self.player_pos = 75
            self.var = self.player_pos
        if self.player_pos == 98:
            self.player_pos = 78
            self.var = self.player_pos


class cell(object):
    def __init__(self):
        self.jump = False


blackground = Image.open("Photos/Board.gif", "r")
blue = Image.open("Photos/Blue.png", "r")
red = Image.open("Photos/Red.png", "r")





root = Tk()
app = Application(root)
root.geometry("400x600")
root.mainloop()