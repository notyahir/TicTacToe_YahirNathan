
"""
Name: Nathan and Yahir
Project: Tic-Tac-Toe
"""

from tkinter import *
import random
import tkinter

"""
BOARD BASE
"""

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

# These variables are used to check whether the board will have these marks on the board. Used for win condition
moveX = "  X  "
moveO = "  O  "
moveX_middle = "|  X  |"
moveO_middle = "|  O  |"

list_of_marksX = [moveX, moveX_middle]
list_of_marksO = [moveO, moveO_middle]


# Function creating the board! Prints each list of strings and we use the join function to get rid
# of the list layout


def create_board() -> object:
    for i in range(len(board)):
        print("".join(board[i]))

"""
START OF GAME AND WIN CONDITIONS OF X AND O
"""

x=0
def player_turn():
    global x
    player_first = random.choice([True, False])

    if player_first and x==0:
        print("Welcome user! Player 1 will be O and Player 2 will be X.")
        print("To start, Player 1 just click position to place your O on the tk.")
        print("And Player 2, just click on a position to place your X on the tk.")
        print("The game will continue switching sides UNTIL a clear winner is decided.")

        print()

        print("Good Luck!")
        print("Player 1 (O) will go first")
        x += 1
        print()

    elif player_first == False and x==0:  # (If playerFirst == False is the only other option)
        print("Welcome user! Player 1 will be O and Player 2 will be X.")
        print("To start, Player 1 just click position to place your O on the tk.")
        print("And Player 2, just click on a position to place your X on the tk.")
        print("The game will continue switching sides UNTIL a clear winner is decided.")

        print()

        print("Good Luck!")
        print("Player 2 (X) will go first")
        x+=1
        print()
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

def create(x, y, test):
    # Calling the global board function since this is what we want to alter.
    global board
    board[x][y] = test

def determineWinner():
    global board, list_of_marksO, list_of_marksX
    if (board[0][0] in list_of_marksX) and (board[0][1] in list_of_marksX) and (board[0][2] in list_of_marksX):
        print("PLAYER X WON! GAMEOVER!")
    elif (board[2][0] in list_of_marksX) and (board[2][1] in list_of_marksX) and (board[2][2] in list_of_marksX):
        print("PLAYER X WON! GAMEOVER!")
    elif (board[4][0] in list_of_marksX) and (board[4][1] in list_of_marksX) and (board[4][2] in list_of_marksX):
        print("PLAYER X WON! GAMEOVER!")
    elif (board[0][0] in list_of_marksX) and (board[2][0] in list_of_marksX) and (board[4][0] in list_of_marksX):
        print("PLAYER X WON! GAMEOVER!")
    elif (board[0][1] in list_of_marksX) and (board[2][1] in list_of_marksX) and (board[4][1] in list_of_marksX):
        print("PLAYER X WON! GAMEOVER!")
    elif (board[0][2] in list_of_marksX) and (board[2][2] in list_of_marksX) and (board[4][2] in list_of_marksX):
        print("PLAYER X WON! GAMEOVER!")
    elif (board[0][0] in list_of_marksX) and (board[2][1] in list_of_marksX) and (board[4][2] in list_of_marksX):
        print("PLAYER X WON! GAMEOVER!")
    elif (board[0][2] in list_of_marksX) and (board[2][1] in list_of_marksX) and (board[4][0] in list_of_marksX):
        print("PLAYER X WON! GAMEOVER!")


    elif (board[0][0] in list_of_marksO) and (board[0][1] in list_of_marksO) and (board[0][2] in list_of_marksO):
        print("PLAYER O WON! GAMEOVER!")
    elif (board[2][0] in list_of_marksO) and (board[2][1] in list_of_marksO) and (board[2][2] in list_of_marksO):
        print("PLAYER O WON! GAMEOVER!")
    elif (board[4][0] in list_of_marksO) and (board[4][1] in list_of_marksO) and (board[4][2] in list_of_marksO):
        print("PLAYER O WON! GAMEOVER!")
    elif (board[0][0] in list_of_marksO) and (board[2][0] in list_of_marksO) and (board[4][0] in list_of_marksO):
        print("PLAYER O WON! GAMEOVER!")
    elif (board[0][1] in list_of_marksO) and (board[2][1] in list_of_marksO) and (board[4][1] in list_of_marksO):
        print("PLAYER O WON! GAMEOVER!")
    elif (board[0][2] in list_of_marksO) and (board[2][2] in list_of_marksO) and (board[4][2] in list_of_marksO):
        print("PLAYER O WON! GAMEOVER!")
    elif (board[0][0] in list_of_marksO) and (board[2][1] in list_of_marksO) and (board[4][2] in list_of_marksO):
        print("PLAYER O WON! GAMEOVER!")
    elif (board[0][2] in list_of_marksO) and (board[2][1] in list_of_marksO) and (board[4][0] in list_of_marksO):
        print("PLAYER O WON! GAMEOVER!")


'''
PLAYER MOVES CYCLES, POSITIONS OF X AND O ON BOARD
'''

#switches between players code of X and O throughout the game
turn = player_turn()

def turnply1():
    global turn
    return not turn


def position_move(val):
    global turn
    if val == "topL":
        print("Top Left Move!")
        if turn == False:
            create(0, 0, "  X  ")
            create_board()
            print()
            turn = turnply1()
        elif turn == True:
            create(0, 0, "  O  ")
            create_board()
            print()
            turn = turnply1()
        print()
        determineWinner()

    elif val == "topM":
        print("Top Middle Move!")
        print()

        if turn == False:
            create(0, 1, "|  X  |")
            create_board()
            print()
            turn = turnply1()
        elif turn == True:
            create(0, 1, "|  O  |")
            create_board()
            print()
            turn = turnply1()
        determineWinner()

    elif val == "topR":
        print("Top Right Move!")
        print()

        if not turn:
            create(0, 2, "  X  ")
            create_board()
            print()
            turn = turnply1()
        elif turn:
            create(0, 2, "  O  ")
            create_board()
            print()
            turn = turnply1()
        determineWinner()

    elif val == "midL":
        print("Middle Left Move!")
        print()

        if turn == False:
            create(2, 0, "  X  ")
            create_board()
            print()
            turn = turnply1()


        elif turn == True:
            create(2, 0, "  O  ")
            create_board()
            print()
            turn = turnply1()
        determineWinner()

    elif val == "midM":
        print("Middle Middle Move!")
        print()

        if turn == False:
            create(2, 1, "|  X  |")
            create_board()
            print()
            turn = turnply1()



        elif turn == True:
            create(2, 1, "|  O  |")
            create_board()
            print()
            turn = turnply1()
        determineWinner()

    elif val == "midR":
        print("Middle Right Move!")
        print()

        if turn == False:
            create(2, 2, "  X  ")
            create_board()
            print()
            turn = turnply1()

        elif turn == True:
            create(2, 2, "  O  ")
            create_board()
            print()
            turn = turnply1()
        determineWinner()

    elif val == "botL":
        print("Bottom Left Move!")
        print()
        if turn == False:
            create(4, 0, "  X  ")
            create_board()
            print()
            turn = turnply1()


        elif turn == True:
            create(4, 0, "  O  ")
            create_board()
            print()
            turn = turnply1()
        determineWinner()


    elif val == "botM":
        print("Bottom Middle Move!")
        print()

        if turn == False:
            create(4, 1, "|  X  |")
            create_board()
            print()
            turn = turnply1()


        elif turn == True:
            create(4, 1, "|  O  |")
            create_board()
            print()
            turn = turnply1()
        determineWinner()

    elif val == "botR":
        print("Bottom Right Move!")
        print()

        if turn == False:
            create(4, 2, "  X  ")
            create_board()
            print()
            turn = turnply1()


        elif turn == True:
            create(4, 2, "  O  ")
            create_board()
            print()
            turn = turnply1()
        determineWinner()


'''
BOARD BUTTON BINDING CREATION: STARTING HERE
'''

root = Tk()
root.configure(background="black")
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

'''
PROJECT START
'''

# Press the green button in the gutter to run the script.
#Intro to project
if __name__ == '__main__':
    create_board()
    root.mainloop()


"""

YAHIR FINISHED HIS DEVELOPMENT ON THIS PROJECT ON March 8, 2022
NATHAN FINISHED HIS DEVELOPMENT ON THIS PROJECT ON March 10, 2022

"""
