from tkinter import *
import random
import PIL
from PIL import Image


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
        self.roll_button.grid(row=6, column = 4)
        imageSmall = PhotoImage(file="Board.jpg")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=5, column=1, columnspan = 8)

        self.rolled_number = Label(self, text = "")
        self.rolled_number.grid(row = 7, column = 4)

    def dice_roll_number(self):
        dice_roll = random.randint(1,6)
        self.var += dice_roll
        print(int(self.var))
        self.rolled_number["text"] = "You rolled a " + str(dice_roll)
        imageSmall = PhotoImage(file="Photos/Dice" + str(dice_roll) +".gif")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=8, column=2)


    def init_board(self):
        self.board = []
        for i in range(100):
            self.board.append(cell())
        self.board[1].jump = True
        self.board[1].jumpto = 38
        self.board[4].jump = True
        self.board[4].jumpto = 14
        self.board[9].jump = True
        self.board[9].jumpto = 31
        self.board[16].jump = True
        self.board[16].jumpto = 6
        self.board[21].jump = True
        self.board[21].jumpto = 42
        self.board[36].jump = True
        self.board[36].jumpto = 44
        self.board[47].jump = True
        self.board[47].jumpto = 26
        self.board[49].jump = True
        self.board[49].jumpto = 11
        self.board[51].jump = True
        self.board[51].jumpto = 67
        self.board[56].jump = True
        self.board[56].jumpto = 53
        self.board[62].jump = True
        self.board[62].jumpto = 19
        self.board[64].jump = True
        self.board[64].jumpto = 60
        self.board[71].jump = True
        self.board[71].jumpto = 91
        self.board[80].jump = True
        self.board[80].jumpto = 100
        self.board[87].jump = True
        self.board[87].jumpto = 24
        self.board[93].jump = True
        self.board[93].jumpto = 73
        self.board[95].jump = True
        self.board[95].jumpto = 75
        self.board[98].jump = True
        self.board[98].jumpto = 78

    def move_player(self):
        self.player_pos = self.board[self.var]
        if self.board[self.var].jump == True:
            self.board[self.var] = self.board[self.var].jumpto
        if self.player_pos == 1:
            self.player_pos = 38
        if self.player_pos == 4:
            self.player_pos = 14
        if self.player_pos == 9:
            self.player_pos = 31
        if self.player_pos == 16:
            self.player_pos = 6
        if self.player_pos == 21:
            self.player_pos = 42
        if self.player_pos == 36:
            self.player_pos = 44
        if self.player_pos == 47:
            self.player_pos = 26
        if self.player_pos == 49:
            self.player_pos = 11
        if self.player_pos == 51:
            self.player_pos = 67
        if self.player_pos == 56:
            self.player_pos = 53
        if self.player_pos == 62:
            self.player_pos = 19
        if self.player_pos == 64:
            self.player_pos = 60
        if self.player_pos == 71:
            self.player_pos = 91
        if self.player_pos == 80:
            self.player_pos = 100
        if self.player_pos == 87:
            self.player_pos = 24
        if self.player_pos == 93:
            self.player_pos = 73
        if self.player_pos == 95:
            self.player_pos = 75
        if self.player_pos == 98:
            self.player_pos = 78

class cell(object):
    def __init__(self):
        self.jump = False


blackground = Image.open("Photos/Board.gif")
blue = Image.open("Photos/Blue.png")
red = Image.open("Photos/Red.png")





root = Tk()
app = Application(root)
root.geometry("400x600")
root.mainloop()