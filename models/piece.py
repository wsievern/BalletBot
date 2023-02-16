class Piece:
    def __init__(self, filename, displayname, bpm, info):
        self.filename = filename
        self.displayname = displayname
        self.bpm = bpm
        self.info = info

piece_collection = (
        Piece("/Users/willsievern/Documents/GitHub/BalletBot/data/plies/Chopin_ Waltz No. 7 in C-Sharp Minor, "
              "Op. 64 No. 2.mp3", "Waltz in C-Sharp Minor", 70, "3/4, Moderato"),
        Piece("/Users/willsievern/Documents/GitHub/BalletBot/data/plies/Frederic Chopin - Mazurka Op. 33, No. 4.mp3", "Mazurka Op. 33, No. 4", 80, "3/4, Moderato"),
        Piece("/Users/willsievern/Documents/GitHub/BalletBot/data/plies/Frederic Chopin - Waltz in A Minor, B.150.mp3", "Waltz in A Minor", 90, "3/4, Moderato"),
        Piece("/Users/willsievern/Documents/GitHub/BalletBot/data/plies/Blue Danube No. 3 & 4, 145 BPM.mp3", "On the Beautiful Blue Danube, no. 3-4", 145, "3/4, Moderato"),
        Piece("/Users/willsievern/Documents/GitHub/BalletBot/data/plies/Blue Danube No. 5 + Coda, 155 BPM.mp3", "On the Beautiful Blue Danube, no. 5 + Coda", 155, "3/4, Moderato")
    )