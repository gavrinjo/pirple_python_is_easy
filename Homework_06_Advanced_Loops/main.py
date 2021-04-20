import os


def drawGrid(row, col):

    # variable for checking if user input for grid size is smaller then actual terminal size
    row2 = row
    col2 = col

    # get terminal size
    size = os.get_terminal_size()

    # check if row number is greater then terminal line number
    # and set row number to fit the terminal screen
    if row > size[1] - 2:
        row = size[1] - 2

    # check if column number is greater then terminal column number
    # set column number to fit the terminal screen
    # and also made it even number
    if col > size[0] - 2:
        if (size[0] - 2) % 2 == 0:
            col = size[0] - 3
        else:
            col = size[0] - 2
    elif col % 2 == 0:
        col -= 1

    # nested for loop to draw a grid
    for j in range(row):
        for i in range(col):
            if j == min(range(row)) and i == min(range(col)):
                print("┌", end="")
            elif j == min(range(row)) and i == max(range(col)):
                print("┐")
            elif j == max(range(row)) and i == min(range(col)):
                print("└", end="")
            elif j == max(range(row)) and i == max(range(col)):
                print("┘")
            elif j == min(range(row)) and i % 2 == 0:
                print("┬", end="")
            elif j == max(range(row)) and i % 2 == 0:
                print("┴", end="")
            elif i == min(range(col)) and j > 0:
                print("├", end="")
            elif i == max(range(col)) and j > 0:
                print("┤")
            elif i % 2 == 0:
                print("┼", end="")
            else:
                print("─", end="")
    
    if size[0]-2 >= col2 and size[1]-2 >= row2:
        print(True) 
    else:
        print(False)


drawGrid(10, 700) 