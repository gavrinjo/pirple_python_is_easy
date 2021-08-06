import re

"""

Info about my favorite song. AC/DC - 'You Shook Me All Night Long'
All information are took from Wikipedia.

Also i took a liberty to make a dictionary and do a for loop iterate through 'key', 'value' pairs.

'You Shook Me All Night Long' is a song by Australian hard rock band AC/DC, from the album Back in Black.
The song also reappeared on their later album Who Made Who.
It is AC/DC's first single with Brian Johnson as the lead singer, replacing Bon Scott who died of alcohol poisoning in February 1980.
It reached number 35 on the USA's Hot 100 pop singles chart in 1980.
The single was re-released internationally in 1986, following the release of the album Who Made Who.
The re-released single in 1986 contains the B-side(s): B1. "She's Got Balls" (Live, Bondi Lifesaver '77); B2. "You Shook Me All Night Long" (Live '83 – 12-inch maxi-single only).
In January 2018, as part of Triple M's "Ozzest 100", the 'most Australian' songs of all time, "You Shook Me All Night Long" was ranked number 63
"""

# !here is dictionary with for loop.
# !Initially i was too lazy to type print for every variable :)

dictionary = {
    "song":"You Shook Me All Night Long",
    "artist": "AC/DC",
    "album": "Back in Black and Who Made Who",
    "released": "19 August 1980",
    "recorded": 1980,
    "genre": "Hard rock",
    "durationInSeconds": 212,
    "label": "Atlantic",
    "songwriter": "Angus Young, Malcolm Young, Brian Johnson",
    "producer": 'Robert John "Mutt" Lange',
    }

for key, value in dictionary.items():
    print(f"{key} = {value}")


def guess_attrib(key, value):
    if key in dictionary:
        if value.isnumeric():
            value = int(value)
        if dictionary[key].lower() == value:
            print("correct".upper())
            print(f"{key.capitalize()} = {dictionary[key]}")
        else:
            print("wrong answer!!")
    else:
        print("wrong answer!!")


if __name__ == '__main__':

    a = input("write a key\n")
    b = input("write key value\n").lower()

    guess_attrib(a, b)
