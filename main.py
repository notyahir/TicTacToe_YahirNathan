# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

"""
Name: Nathan and Yahir
Project: Tic-Tac-Toe
"""

import random
from tkinter import *
import tkinter

# This global variable, board, is the foundation of our program. It is a list of lists of strings. Since lists
# are mutable, this makes it easy to actually "alter" the board.
global board
board = [
    ["     ", "|     |", "     "], # 0 - Score
    ["_____", "|_____|", "_____"], # 1
    ["     ", "|     |", "     "], # 2 - Score
    ["_____", "|_____|", "_____"], # 3
    ["     ", "|     |", "     "], # 4 - Score
    ["     ", "|     |", "     "]  # 5

]


# Function creating the board! Prints each list of strings and we use the join function to get rid
# of the list layout


def create_board():
    for i in range(len(board)):
        print("".join(board[i]))


# Function used to determine which player is going to go first

print("hello world")
def player_turn():
    player_first = random.randint(1, 2)
    if player_first == 1:
        print("The player will go first")
    else: # (If playerFirst == 2 is the only other option)
        print("The computer will go first")
    return player_first


# Will make the game commence!
def game_run():
    game_running = True

    # Creates the board using the create_board function
    create_board()
    print()

    player_turn()

    while game_running:
        if player_turn() == 1:
            pass


# This function modifies the tic-tac-toe board by allowing us to add the user buttons
def create(x,y,test):
   #Calling the global board function since this is what we want to alter.
   global board

   board[x][y] = test

def position_move(val):
    if val == "topL":
        print("Top Left Move!")
        print()

        create(0, 0, "  X  ")
        create_board()
        print()
    elif val == "topM":
        print("Top Middle Move!")
        print()

        create(0, 1, "|  O  |")
        create_board()
        print()
    elif val == "topR":
        print("Top Right Move!")
        print()

        create(0, 2, "  X  ")
        create_board()
        print()
    elif val == "midL":
        print("Middle Left Move!")
        print()

        create(2, 0, "  O  ")
        create_board()
        print()
    elif val == "midM":
        print("Middle Middle Move!")
        print()

        create(2, 1, "|  X  |")
        create_board()
        print()
    elif val == "midR":
        print("Middle Right Move!")
        print()

        create(2,2,"  O  ")
        create_board()
        print()
    elif val == "botL":
        print("Bottom Left Move!")
        print()

        create(4,0,"  X  ")
        create_board()
        print()
    elif val == "botM":
        print("Bottom Middle Move!")
        print()

        create(4,1,"|  O  |")
        create_board()
        print()
    elif val == "botR":
        print("Bottom Right Move!")
        print()

        create(4, 2, "  X  ")
        create_board()
        print()

'''
BOARD BUTTON BINDING CREATION: STARTING HERE
'''
root = Tk()
root.configure(background="dark blue")
gridRoot = Entry(root)

topL = tkinter.Button(root, text="topL", command=lambda:position_move("topL"))
topL.grid(row=0,column=0)

topM = tkinter.Button(root, text="topM", command=lambda:position_move("topM"))
topM.grid(row=0,column=1)

topR = tkinter.Button(root, text="topR", command=lambda:position_move("topR"))
topR.grid(row=0,column=2)

# middle creation buttons
midL = tkinter.Button(root, text="midL", command=lambda:position_move("midL"))
midL.grid(row=1,column=0)

midM = tkinter.Button(root, text="midM", command=lambda:position_move("midM"))
midM.grid(row=1,column=1)

midR = tkinter.Button(root, text="midR", command=lambda:position_move("midR"))
midR.grid(row=1,column=2)

botL = tkinter.Button(root, text="botL", command=lambda:position_move("botL"))
botL.grid(row=2,column=0)

botM = tkinter.Button(root, text="botM", command=lambda:position_move("botM"))
botM.grid(row=2,column=1)

botR = tkinter.Button(root, text="botR", command=lambda:position_move("botR"))
botR.grid(row=2,column=2)









# This clear variable will be used to "reset" the console and just get rid of any previous iteration.
clear = "\n" * 100


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_board()
    print()

    print("balls")

    root.mainloop()

"""
END OF PROGRAM
"""