from tkinter import *
import random
from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets_page_one()

        self.rolled_number = Label(self, text="")
        self.var1 = 0
        self.var2 = 0

        self.player_turn_var = 1
        self.player1_pos = 1
        self.player2_pos = 1

    def create_widgets_page_one(self):
        self.label = Label(text="Welcome to Chutes and Ladders!", font=("Times New Roman", 20))
        self.label.grid(row=2, column=1, columnspan = 2)

        self.next_bttn = Button(self, text="Next", command=self.page_three)
        self.next_bttn.grid(row=1, column=1)

    def page_three(self):
        self.label.destroy()
        self.next_bttn.destroy()
        self.player_turn = Label(self, text="")
        self.player_turn.grid(row=7, column=4)

        self.roll_button = Button(self, text="Roll", command=self.dice_roll_number)
        self.roll_button.grid(row=8, column=4)
        self.drawBoard()



    def drawBoard(self):
        boardImage = Image.open('Photos/Board.gif')
        player1Piece = Image.open('Blue.png')
        player2Piece = Image.open('Red.png')

        player1_y_value = int(int(10 - self.player1_pos / 10) * 42 + 1)

        player1_x_value = int(self.player1_pos % 20)
        if (player1_x_value >= 10) and (player1_x_value <= 20):
            player1_x_value = (20 - player1_x_value) * 40 + 20

        else:
            player1_x_value = self.player1_pos

        print(player1_x_value)

        boardImage.paste(player1Piece, (player1_x_value, player1_y_value), player1Piece)

        player2_y_value = int(int(10 - self.player2_pos / 10) * 42 + 1)

        player2_x_value = int(self.player2_pos % 20)
        if (player2_x_value >= 10) and (player2_x_value <= 20):
            player2_x_value = (20 - player2_x_value) * 38 + 20

        else:
            player2_x_value = self.player2_pos

        print(player2_x_value)

        boardImage.paste(player2Piece, (player2_x_value, player2_y_value), player2Piece)






        tkimage = ImageTk.PhotoImage(boardImage)
        panel1 = Label(self, image=tkimage)
        panel1.photo = tkimage
        panel1.grid(row=1, column=2, sticky=E, columnspan = 8)

        self.rolled_number = Label(self, text="")
        self.rolled_number.grid(row=9, column=4)

        self.player1_space = Label(self, text = "")
        self.player1_space.grid(row=10, column=4)

        self.winner = Label (self, text="")
        self.winner.grid(row=11, column=4)

        tkimage = ImageTk.PhotoImage(boardImage)

    def dice_roll_number(self):
        dice_roll = random.randint(1,6)
        if self.player_turn_var % 2 != 0:
            self.var1 += dice_roll
        else:
            self.var2 += dice_roll

        self.move_player()

        self.drawBoard()

        if self.player_turn_var % 2 != 0:
            self.player_turn["text"] = "Player 1's Turn"
        else:
            self.player_turn["text"] = "Player 2's Turn"

        self.rolled_number["text"] = "You rolled a " + str(dice_roll)

        if self.player_turn_var % 2 != 0:
            self.player1_space["text"] = "You're at space " + str(self.var1)
        else:
            self.player1_space["text"] = "You're at space " + str(self.var2)
        imageSmall = PhotoImage(file="Photos/Dice" + str(dice_roll) + ".gif")
        self.player_turn_var += 1
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=8, column=2, rowspan = 4)


        if self.var1 >= 100 or self.var2 >= 100:
            self.var1 = 100
            self.var2 = 100

            self.player1_space["text"] = "You passed space " + str(self.var1)
            self.winner["text"] = "Congrats you won!"
            self.roll_button.destroy()
            self.exit_button = Button(self, text = "Exit", command = quit)
            self.exit_button.grid(row=12, column = 8)


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


        self.player2_pos = self.var2
        if self.player2_pos == 1:
            self.player2_pos = 38
            self.var2 = self.player2_pos
        if self.player2_pos == 4:
            self.player2_pos = 14
            self.var2 = self.player2_pos
        if self.player2_pos == 9:
            self.player2_pos = 31
            self.var2 = self.player2_pos
        if self.player2_pos == 16:
            self.player2_pos = 6
            self.var2 = self.player2_pos
        if self.player2_pos == 21:
            self.player2_pos = 42
            self.var2 = self.player2_pos
        if self.player2_pos == 36:
            self.player2_pos = 44
            self.var2 = self.player2_pos
        if self.player2_pos == 47:
            self.player2_pos = 26
            self.var2 = self.player2_pos
        if self.player2_pos == 49:
            self.player2_pos = 11
            self.var2 = self.player2_pos
        if self.player2_pos == 51:
            self.player2_pos = 67
            self.var2 = self.player2_pos
        if self.player2_pos == 56:
            self.player2_pos = 53
            self.var2 = self.player2_pos
        if self.player2_pos == 62:
            self.player2_pos = 19
            self.var2 = self.player2_pos
        if self.player2_pos == 64:
            self.player2_pos = 60
            self.var2 = self.player2_pos
        if self.player2_pos == 71:
            self.player2_pos = 91
            self.var2 = self.player2_pos
        if self.player2_pos == 80:
            self.player2_pos = 100
            self.var2 = self.player2_pos
        if self.player2_pos == 87:
            self.player2_pos = 24
            self.var2 = self.player2_pos
        if self.player2_pos == 93:
            self.player2_pos = 73
            self.var1 = self.player2_pos
        if self.player2_pos == 95:
            self.player2_pos = 75
            self.var2 = self.player2_pos
        if self.player2_pos == 98:
            self.player2_pos = 78
            self.var2 = self.player2_pos



class cell(object):
    def __init__(self):
        self.jump = False

root = Tk()
app = Application(root)
root.geometry("415x600")
root.mainloop()