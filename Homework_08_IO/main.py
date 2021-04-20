from pathlib import Path
import os


def replace_line(file_name, option):    # NOTE replace/append line
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
        if option == "C":
            string = input("Enter a new entry\n")
            lines.append(string)
        elif option == "D":
            while True:
                n = int(input("Enter line to replace\n"))
                if n > max(range(len(lines))):
                    print("Invalid line number!!")
                    print_file(Path(f))
                    pass
                else:
                    break
            string = input("Enter a new entry\n")
            lines[n] = string

    with open(file_name, 'w', encoding="utf-8") as out:
        for line in lines:
            out.writelines(f"{line}\n")


def remove_line(file_name):     # NOTE remove line
    with open(file_name, "r") as file:
        lines = file.readlines()

        while True:
            n = int(input("Enter line to delete\n"))
            if n > max(range(len(lines))):
                print("Invalid line number!!")
                print_file(Path(f))
                pass
            else:
                break

        lines.remove(lines[n])
        with open(file_name, 'w', encoding="utf-8") as out:
            out.writelines(lines)
            out.truncate()


def print_file(file_name):      # NOTE print out file content
    with open(file_name, "r") as file:
        for pos, line in enumerate(file):
            print(f"{str(pos).rjust(3, ' ')}| {line}", end="")
        print("\n--END--\n")


while True:

    print(" A) Create or Edit file")
    print(" X) Exit")
    c = input("\nChose what to do...\n").upper()
    if c == "A":
        f = input("Enter a filename!\n\n")
        if Path.exists(Path(f)):
            print("\nFilename already exists!\n")
            while True:
                print(" A) Read the file")
                print(" B) Delete the file and start over")
                print(" C) Append the file")
                print(" D) Replace a single line")
                print(" V) Remove a single line")
                # print(" Y) Clear screen")
                print(" X) Previous menu")

                opt = input("\nChose what to do...\n").upper()

                if opt == "A":
                    print_file(Path(f))
                elif opt == "B":
                    os.remove(f)
                    break
                elif opt == "C" or opt == "D":
                    replace_line(Path(f), opt)
                    print_file(Path(f))
                elif opt == "V":
                    remove_line(Path(f))
                    print_file(Path(f))
                elif opt == "Y":
                    os.system("cls" if os.name == "nt" else "clear")
                elif opt == "X":
                    break
                else:
                    print("Invalid option!!\n")
            pass

        else:
            print("\nCreating new file...")
            with open(f, "w", encoding="utf-8") as nf:
                s = input("enter a new entry...\n\n")
                nf.write(s)
            print("\nNew file created and saved...")

    elif c == "X":
        break
    else:
        print("Invalid option!!\n")
