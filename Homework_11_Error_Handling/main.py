
from random import randint

print("simple guess game, with error handling")


def input_validation():
    valid_input = False
    while valid_input is False:
        try:
            guess = int(input("guess a number: "))
        except ValueError:
            print("enter a Integer!!")
            valid_input = False
        else:
            valid_input = True
            return guess


def play():
    secret_number = randint(100, 999)
    number_of_guesses = 5
    while number_of_guesses > 0:
        num = input_validation()
        if num < secret_number:
            print(f"to low: {num}")
        elif num > secret_number:
            print(f"to high: {num}")
        else:
            print(f"That is correct!! {num}")
            break

        number_of_guesses -= 1
        if number_of_guesses == 0:
            print("you lost!!")
            print(f"correct number is {secret_number}")


if __name__ == '__main__':
    play()
