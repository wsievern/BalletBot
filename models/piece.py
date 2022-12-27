class Piece:
    def __init__(self, filename, display_name, bpm):
        self.filename = filename
        self.display_name = display_name
        self.bpm = bpm

piece_collection = (
        Piece("data/plies/Chopin_ Waltz No. 7 in C-Sharp Minor, Op. 64 No. 2.mp3", "Waltz in C-Sharp Minor", 70),
        Piece("data/plies/Frederic Chopin - Mazurka Op. 33, No. 4.mp3", "Mazurka Op. 33, No. 4", 80),
        Piece("data/plies/Frederic Chopin - Waltz in A Minor, B.150.mp3", "Waltz in A Minor", 90),
        Piece("data/plies/Chopin_ Waltz No. 7 in C-Sharp Minor, Op. 64 No. 2.mp3", "Waltz in C-Sharp Minor", 100),
    )