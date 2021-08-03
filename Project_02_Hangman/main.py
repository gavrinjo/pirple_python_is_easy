import string
import os
import random


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


def play(no):
    alphabet = list(string.ascii_uppercase)
    numbers = list(string.digits)
    main_alphabet = alphabet + numbers
    rest_alphabet = main_alphabet.copy()

    if no == 1:
        f = open("words.txt", "r")
        words = f.read().splitlines()
        secret_phrase = list(random.choice(words).upper())
    else:
        secret_phrase = list(input("secret phrase: ").upper())

    temp_phrase = secret_phrase.copy()

    os.system("cls" if os.name == "nt" else "clear")

    for i, w in enumerate(secret_phrase):
        if w in main_alphabet:
            temp_phrase[i] = "_"

    attempts = 6  # NOTE - tries left

    while attempts > 0:
        os.system("cls" if os.name == "nt" else "clear")
        header()
        draw_hangman(attempts)
        print("".join(rest_alphabet))
        print("".join(temp_phrase))

        letter = input("your input: ").upper()

        for i, w in enumerate(main_alphabet):
            if w in letter:
                rest_alphabet[i] = "_"

        for i, w in enumerate(secret_phrase):
            if w == letter:
                temp_phrase[i] = secret_phrase[i]

        if letter in secret_phrase:
            pass
        else:
            attempts -= 1

        if secret_phrase == temp_phrase:
            print()
            print(f'you did it!! "{"".join(temp_phrase)}" is correct phrase')
            print()
            break
        else:
            print()
            print(f'you lost!! "{"".join(secret_phrase)}" is correct phrase')
            print()


if __name__ == '__main__':
    print("1: for one player vs. computer mode")
    print("2: for two players mode")
    players = int(input("Enter: "))
    play(players)
