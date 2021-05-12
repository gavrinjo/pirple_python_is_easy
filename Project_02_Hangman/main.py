import string
import os

# NOTE - new project Hangman game

#  123456789
# 1┌─────┐
# 2│     │
# 3│     @
# 4│   ┌─╫─┐
# 5│    ┌╨┐
# 6│    ┘ └
# 7┴──────
# ┴┌┐┘└

active_chars = list(string.ascii_uppercase)
inactive_chars = list()
attempts = 0  # NOTE - tries left
game = False


def header():
    title = [
        " _   _                  ___  ___            ",
        "| | | |                 |  \\/  |            ",
        "| |_| | __ _ _ __   __ _| .  . | __ _ _ __  ",
        "|  _  |/ _` | '_ \\ / _` | |\\/| |/ _` | '_ \\ ",
        "| | | | (_| | | | | (_| | |  | | (_| | | | |",
        "\\_| |_/\\__,_|_| |_|\\__, \\_|  |_/\\__,_|_| |_|",
        "                    __/ |                   ",
        "                   |___/                    "
    ]

    for st in title:
        print(st.center(100, " "))


def draw_hangman(tl):

    print("┌".ljust(5, "─") + "┐")
    print("│".ljust(5, " ") + "│")
    print("│".ljust(5, " ") +
          f"{'O' if tl < 6 else ' '}"
          )
    print("│".ljust(3, " ") +
          f"{'└─' if tl < 4 else '  '}" +
          f"{'╫' if tl < 5 else ' '}" +
          f"{'─┘' if tl < 3 else '  '}"
          )
    print("│".ljust(4, " ") +
          f"{'┌' if tl < 2 else ' '}" +
          f"{'╨' if tl < 5 else ' '}" +
          f"{'┐' if tl < 1 else ' '}"
          )
    print("│".ljust(4, " ") +
          f"{'┘' if tl < 2 else ' '}" + " " +
          f"{'└' if tl < 1 else ' '}"
          )
    print("┴".ljust(7, "─"))


"""for i in range(len(active_chars)):
    if i <= 11:
        print(active_chars[i], end=" ")
    elif i == 12:
        print(active_chars[i])
    else:
        print(active_chars[i], end=" ")"""


"""while game:
    pass"""
os.system("cls" if os.name == "nt" else "clean")
header()
secret_word = input()

os.system("cls" if os.name == "nt" else "clean")
header()
draw_hangman(attempts)

