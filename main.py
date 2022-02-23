# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


global board
board = [
    ["___", "|___|", "___"],
    ["___", "|___|", "___"],
    ["   ", "|   |", "   "]

]


def create_board2():
    j=0
    for i in range(3):
        if j != 2:
            print("    |    |    ")
            print("____|____|____")
        else:
            print("    |    |    ")
            print("    |    |    ")
        j+=1


def create_board():
    for row in board:
        for slot in row:
            print(f"{slot}", end="")
        print()


def create_board3():
    print(board)
def create(x,y,test):
   global board
   board[x][y] = test

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Helo world")
    create_board()
    print()
    '''
    create_board2()
    print()
    '''


    create(0,0,"_X_")
    create_board()

    print()

    create(0,1,"|_O_|")
    create_board()
    
    print("balls")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
