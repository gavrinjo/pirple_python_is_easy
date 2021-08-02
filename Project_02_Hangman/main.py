import string
import os
from pynput import keyboard


# NOTE - new project Hangman game

#  123456789
# 1┌─────┐
# 2│     │
# 3│     @
# 4│   ┌─╫─┐
# 5│    ┌╨┐
# 6│    ┘ └
# 7┴──────


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


def char_list(main, used, rest):
    if rest is not None:
        rest = []
    for char in main:
        if char in used:
            char_replace = char.replace(char, "_")
            rest.append(char_replace)
        else:
            rest.append(char)
    return rest


# os.system("cls" if os.name == "nt" else "clean")

main_alphabet = list(string.ascii_uppercase)
used_alphabet = []
rest_alphabet = []
attempts = 6  # NOTE - tries left

secret_word = input("unesi: ")


while attempts > 0:
    header()
    for char in char_list(main_alphabet, used_alphabet, rest_alphabet):
        print(char, end=" ")
    print()
    draw_hangman(attempts)
    letter = input("unesi slovo: ")
    used_alphabet.append(letter.upper())
    attempts -= 1
