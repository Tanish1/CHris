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
        self.roll_button.grid(row=6, column = 4)
        imageSmall = PhotoImage(file="Board.jpg")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=5, column=1, columnspan = 8)

        self.rolled_number = Label(self, text = "")
        self.rolled_number.grid(row = 7, column = 4)

    def dice_roll_number(self):
        dice_roll = random.randint(1,6)
        self.rolled_number["text"] = "You rolled a " + str(dice_roll)
        imageSmall = PhotoImage(file="Photos/ Dice"+ str(dice_roll) +".jpg")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=8, column=2)

    def init_board(self):
        board = []
        for i in range(100):
            board.append(cell())
        board[1].jump = True
        board[1].jumpto = 38
        board[4].jump = True
        board[4].jumpto = 14
        board[9].jump = True
        board[9].jumpto = 31
        board[16].jump = True
        board[16].jumpto = 6
        board[21].jump = True
        board[21].jumpto = 42
        board[36].jump = True
        board[36].jumpto = 44
        board[47].jump = True
        board[47].jumpto = 26
        board[49].jump = True
        board[49].jumpto = 11
        board[51].jump = True
        board[51].jumpto = 67
        board[56].jump = True
        board[56].jumpto = 53
        board[62].jump = True
        board[62].jumpto = 19
        board[64].jump = True
        board[64].jumpto = 60
        board[71].jump = True
        board[71].jumpto = 91
        board[80].jump = True
        board[80].jumpto = 100
        board[87].jump = True
        board[87].jumpto = 24
        board[93].jump = True
        board[93].jumpto = 73
        board[95].jump = True
        board[95].jumpto = 75
        board[98].jump = True
        board[98].jumpto = 78


class cell(object):
    def __init__(self):
        self.jump  = False


root = Tk()
app = Application(root)
root.geometry("400x600")
root.mainloop()
ds