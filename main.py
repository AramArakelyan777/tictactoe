from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x297")
root.title("Tic Tac Toe")

clicked = True
count = 0


def click(b):
    global clicked, count
    if clicked == True and b['text'] == "":
        b['text'] = 'X'
        clicked = False
        count += 1
        win()
    elif clicked == False and b['text'] == "":
        b['text'] = 'O'
        clicked = True
        count += 1
        win()
    else:
        messagebox.showerror("Error", "That spot is already occupied.")


b1 = Button(root, text="", width=9, height=5, command=lambda: click(b1))
b2 = Button(root, text="", width=9, height=5, command=lambda: click(b2))
b3 = Button(root, text="", width=9, height=5, command=lambda: click(b3))
b4 = Button(root, text="", width=9, height=5, command=lambda: click(b4))
b5 = Button(root, text="", width=9, height=5, command=lambda: click(b5))
b6 = Button(root, text="", width=9, height=5, command=lambda: click(b6))
b7 = Button(root, text="", width=9, height=5, command=lambda: click(b7))
b8 = Button(root, text="", width=9, height=5, command=lambda: click(b8))
b9 = Button(root, text="", width=9, height=5, command=lambda: click(b9))
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def win():
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" or b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        messagebox.showinfo("Thats it", "The player X won.")
        winner = True
        disable()
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" or b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        messagebox.showinfo("Thats it", "The player O won.")
        winner = True
        disable()
    elif count == 9:
        messagebox.showinfo("Thats it", "It's a tie.")
        disable()


root.mainloop()
