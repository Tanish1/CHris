import tkinter
imageLarge = tkinter.PhotoImage(file="Chutes&Ladders1.gif")
w = tkinter.Label(image = imageLarge)
w.photo = imageLarge
w.grid(row = 5, column = 0)


root = tkinter.Tk()
root.mainloop()

