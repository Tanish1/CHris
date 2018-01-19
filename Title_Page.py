from tkinter import *
import random
from PIL import Image, ImageTk
import sys


class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets_page_one()
        self.rolled_number = Label(self, text="")
        self.var1 = 0
        self.var2 = 0
        self.player1_x_value = 5
        self.player1_y_value = 385
        self.player2_x_value = -500
        self.player2_y_value = 385

    def create_widgets_page_one(self):
        self.label = Label(text="Welcome to  Chutes and Ladders!")
        self.label.grid(row = 2, column = 2)

        self.next_bttn = Button(self, text="Next", command=self.page_three)
        self.next_bttn.grid(row=1, column=1)

    def page_three(self):
        self.next_bttn.destroy()
        self.label.destroy()
        self.roll_button = Button(self, text="Roll", command =self.dice_roll_number)
        self.roll_button.grid(row=6, column = 4)

        head = Image.open('Photos/Board.gif')
        hand = Image.open('Blue.png')

        second_hand = Image.open('Photos/Board.gif')
        second_hand = Image.open('Blue.png')

        head.paste(hand, (self.player1_x_value, self.player1_y_value), hand)

        second_hand.paste(second_hand, (self.player2_x_value, self.player2_y_value), second_hand)
        # Convert the Image object into a TkPhoto object

        tkimage = ImageTk.PhotoImage(head)
        second_tkimage = ImageTk.PhotoImage(second_hand)
        panel1 = Label(self, image=tkimage)
        panel1.photo = tkimage
        panel1.grid(row=1, column=2, sticky=E, columnspan = 8)

        panel2 = Label(self, image=second_tkimage)
        panel2.photo = second_tkimage
        panel2.grid(row=1, column=1, sticky=E, columnspan=8)

        self.rolled_number = Label(self, text = "")
        self.rolled_number.grid(row = 8, column = 4)

        self.player1_space = Label(self, text = "")
        self.player1_space.grid(row = 9, column = 4)

        self.winner = Label (self, text = "")
        self.winner.grid(row = 10, column = 4)

    def dice_roll_number(self):
        dice_roll = random.randint(1,6)
        self.var1 += dice_roll
        self.move_player()
        print(self.player1_pos)
        self.rolled_number["text"] = "You rolled a " + str(dice_roll)
        self.player1_space["text"] = "You're at space " + str(self.var1)
        imageSmall = PhotoImage(file="Photos/Dice" + str(dice_roll) +".gif")
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=8, column=2, rowspan = 4)
        if self.var1 >= 100 or self.var2 >= 100:
            self.var1 = 100
            self.var2 = 100
            self.player1_space["text"] = "You passed space " + str(self.var1)
            self.winner["text"] = "Congrats you won!"

    def move_player(self):
        self.board = []
        for i in range(100):
            self.board.append(cell())
        self.player1_pos = self.var1
        if self.player1_pos == 1:
            self.player1_pos = 38
            self.var1 = self.player1_pos
        if self.player1_pos == 4:
            self.player1_pos = 14
            self.var1 = self.player1_pos
        if self.player1_pos == 9:
            self.player1_pos = 31
            self.var1 = self.player1_pos
        if self.player1_pos == 16:
            self.player1_pos = 6
            self.var1 = self.player1_pos
        if self.player1_pos == 21:
            self.player1_pos = 42
            self.var1 = self.player1_pos
        if self.player1_pos == 36:
            self.player1_pos = 44
            self.var1 = self.player1_pos
        if self.player1_pos == 47:
            self.player1_pos = 26
            self.var1 = self.player1_pos
        if self.player1_pos == 49:
            self.player1_pos = 11
            self.var1 = self.player1_pos
        if self.player1_pos == 51:
            self.player1_pos = 67
            self.var1 = self.player1_pos
        if self.player1_pos == 56:
            self.player1_pos = 53
            self.var1 = self.player1_pos
        if self.player1_pos == 62:
            self.player1_pos = 19
            self.var1 = self.player1_pos
        if self.player1_pos == 64:
            self.player1_pos = 60
            self.var1 = self.player1_pos
        if self.player1_pos == 71:
            self.player1_pos = 91
            self.var1 = self.player1_pos
        if self.player1_pos == 80:
            self.player1_pos = 100
            self.var1 = self.player1_pos
        if self.player1_pos == 87:
            self.player1_pos = 24
            self.var1 = self.player1_pos
        if self.player1_pos == 93:
            self.player1_pos = 73
            self.var1 = self.player1_pos
        if self.player1_pos == 95:
            self.player1_pos = 75
            self.var1 = self.player1_pos
        if self.player1_pos == 98:
            self.player1_pos = 78
            self.var1 = self.player1_pos


class cell(object):
    def __init__(self):
        self.jump = False


blackground = Image.open("Photos/Board.gif", "r")
blue = Image.open("Photos/Blue.png", "r")
red = Image.open("Photos/Red.png", "r")






root = Tk()
app = Application(root)
root.geometry("415x600")
root.mainloop()