import string

# NOTE - new project Hangman game

#
# ┌─────┐
# │   __@__
# │     █
# │    / \
# │
# ┴──────
#

active_chars = list(string.ascii_uppercase)
inactive_chars = list()

for i in range(len(active_chars)):
    if i <= 11:
        print(active_chars[i], end=" ")
    elif i == 12:
        print(active_chars[i])
    else:
        print(active_chars[i], end=" ")
