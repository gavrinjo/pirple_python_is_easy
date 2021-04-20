import os
from termcolor import colored, cprint


#  01234567890123456789012345678
# 0┌───┬───┬───┬───┬───┬───┬───┐
# 1│ X │ X │ O │ X │ X │ X │ O │
# 2├───┼───┼───┼───┼───┼───┼───┤
# 3│ X │ O │ X │ X │ X │ X │ O │
# 4├───┼───┼───┼───┼───┼───┼───┤
# 5│ X │ O │ X │ X │ X │ X │ O │
# 6├───┼───┼───┼───┼───┼───┼───┤
# 7│ X │ O │ X │ X │ X │ X │ O │
# 8├───┼───┼───┼───┼───┼───┼───┤
# 9│ X │ O │ X │ X │ X │ X │ O │
# 0├───┼───┼───┼───┼───┼───┼───┤
# 1│ X │ X │ X │ X │ X │ X │ O │
# 2└───┴───┴───┴───┴───┴───┴───┘


game = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
]


def win_check(src):

    # horizontal check
    for row in range(len(src)):
        for col in range(len(src)-2):
            h = set(src[row][col:col+4])
            if len(h) == 1 and " " not in h:
                return 1

    # vertical check
    for row in range(len(src)-3):
        for col in range(len(src[row])):
            v = {src[row][col], src[row + 1][col], src[row + 2][col], src[row + 3][col]}
            if len(v) == 1 and src[row][col] != " ":
                return 1

    # diagonal check
    for row in range(len(src)-3):
        for col in range(len(src)-2):
            d1 = {src[row][col], src[row + 1][col + 1], src[row + 2][col + 2], src[row + 3][col + 3]}
            d2 = {src[row][col + 3], src[row + 1][col + 2], src[row + 2][col + 1], src[row + 3][col]}
            if len(d1) == 1 and src[row][col] != " ":
                return 1
            if len(d2) == 1 and src[row][col + 3] != " ":
                return 1
    return 0


def board(src):
    print("   ", end="")
    for c in range(len(src[0])):
        if c == max(range(len(src[0]))):
            print(f"│ {c + 1} │")
            print("───" + "┌" + "───┬" * c + "───┐")
        else:
            print(f"│ {c + 1} ", end="")
    for i in range(len(src)):
        print(f" {i+1} ", end="")
        for j in range(len(src[i])):
            if j == max(range(len(src[i]))):
                if src[i][j] == "X":
                    text = colored(src[i][j].replace("X", u"\u2B24"), "blue")
                    print(f"│ {text} │")
                elif src[i][j] == "O":
                    text = colored(src[i][j].replace("O", u"\u2B24"), "red")
                    print(f"│ {text} │")
                else:
                    print(f"│ {src[i][j]} │")
                if i != max(range(len(src))):
                    print("───" + "┼───" * (j+1) + "┤")
            else:
                if src[i][j] == "X":
                    text = colored(src[i][j].replace("X", u"\u2B24"), "blue")
                    print(f"│ {text} ", end="")
                elif src[i][j] == "O":
                    text = colored(src[i][j].replace("O", u"\u2B24"), "red")
                    print(f"│ {text} ", end="")
                else:
                    print(f"│ {src[i][j]} ", end="")

            if i == max(range(len(src))) and j == max(range(len(src[i]))):
                print("───" + "└───" + "┴───" * j + "┘")


def play():
    marker = "X"
    count = 0
    os.system("cls" if os.name == "nt" else "clear")
    board(game)
    while True:
        rows = len(game)
        if marker == "X":
            cprint("Blue turn!", "blue")
        else:
            cprint("Red turn!", "red")

        while True:
            place_y = int(input("select column: ")) - 1
            if place_y <= (max(range(len(game))) + 1):
                break
            else:
                print(f"maximum column number is {len(game) + 1}")

        for row in range(rows):
            if game[row][place_y] != " ":
                game[row-1][place_y] = marker
                count += 1
                break
            elif game[row][place_y] == " " and row == 5:
                game[row][place_y] = marker
                count += 1
                break

        os.system("cls" if os.name == "nt" else "clear")
        board(game)

        if count >= 7:
            if win_check(game) > 0:
                if marker == "X":
                    cprint("Blue has won the game!!", "blue")
                else:
                    cprint("Red has won the game!!", "red")
                break

        if count == (max(range(len(game))) + 1) * (max(range(len(game[0]))) + 1):
            print("a draw")
            break

        if marker == "X":
            marker = "O"
        else:
            marker = "X"


if __name__ == "__main__":
    play()

