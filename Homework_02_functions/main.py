"""
[TODO]

Let's return to the music example from assignment one.
Pick 3 of the attributes you listed. For our example we're going to say "Genre", "Artist" and "Year".
Create a new Python file and create 3 functions with the same name as those attributes.
So in this example we'd have one function named "genre" another named "artist" and another called "year".

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


def Artist(data):
    print(data)


def Album(data):
    print(data)


def Song(data):
    print(data)


def Bool(data):
    if data:
        print(True)
    else:
        print(False)

Artist(artist)
Album(album)
Song(song)

Bool(released)
