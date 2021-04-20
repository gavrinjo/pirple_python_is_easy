def grid():
    for row in range(7):
        if row % 2 != 0:
            for col in range(13):
                if col % 4 == 0:
                    if col == max(range(13)):
                        print("│")
                    else:
                        print("│", end="")
                else:
                    print(" ", end="")
        else:
            for col in range(13):
                if col % 4 != 0:
                    print("─", end="")
                else:
                    print("┼", end="")
            print("")


grid()