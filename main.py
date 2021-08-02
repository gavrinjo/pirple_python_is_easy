

import string
import re

tl = 0

main_alphabet = list(string.ascii_uppercase)
used_alphabet = []
rest_alphabet = []
word = input("secret word: ").upper()
pw = word
for i in pw:
    if i in main_alphabet:
        pw = re.sub(i, "_", pw, flags=re.IGNORECASE)
pz = word


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


while tl < 5:
    letter = input("unesi slovo: ").upper()
    used_alphabet.append(letter.upper())
    for char in char_list(main_alphabet, used_alphabet, rest_alphabet):
        print(char, end="")
    print()

    for i in range(len(word)):
        if word[i] in used_alphabet:
            k = pw[i].replace(pw[i], word[i])
            re.sub(pw[i], word[i], pw, flags=re.IGNORECASE)
    print()
    print(pw)
    print(word)
    print(pz)

    tl += 1

