# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

"""
Name: Nathan and Yahir
Project: Tic-Tac-Toe
"""

import random

# This global variable, board, is the foundation of our program. It is a list of lists of strings. Since lists
# are mutable, this makes it easy to actually "alter" the board.
global board
board = [
    ["___", "|___|", "___"],
    ["___", "|___|", "___"],
    ["   ", "|   |", "   "]

]


# Function creating the board! Prints each list of strings and we use the join function to get rid
# of the list layout


def create_board():
    for i in range(len(board)):
        print("".join(board[i]))


# Function used to determine which player is going to go first

def player_turn():
    player_first = random.randint(1,2)
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


# This clear variable will be used to "reset" the console and just get rid of any previous iteration.
clear = "\n" * 100


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_board()
    print()

    create(0,0,"_X_")
    create_board()

    print()

    create(0,1,"|_O_|")
    create_board()
    
    print("balls")


"""
END OF PROGRAM
"""