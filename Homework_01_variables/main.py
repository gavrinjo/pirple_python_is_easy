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


song = "You Shook Me All Night Long" #song name (string)
artist = "AC/DC" #song artist (string)
album = "Back in Black and Who Made Who" #albums (string)
released = "19 August 1980" #initial release (string)
recorded = 1980 #year recorded (integer)
genre = "Hard rock" #genre (string)
durationInSeconds = 212 #duration in seconds (integer)
label = "Atlantic" #released on label (string)
songwriter = "Angus Young, Malcolm Young, Brian Johnson" #writers (string)
producer = 'Robert John "Mutt" Lange' #producer (string)

print(song)
print(artist)
print(album)
print(released)
print(recorded)
print(genre)
print(durationInSeconds)
print(label)
print(songwriter)
print(producer)


"""
here is dictionary with for loop.
Initially i was too lazy to type print for every variable :)
"""
"""
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
    print(key.upper(), "=", value)
"""