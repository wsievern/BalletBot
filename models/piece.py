class Piece:
    def __init__(self, filename, display_name):
        self.filename = filename
        self.display_name = display_name

piece_collection = (
        Piece("data/plies/Chopin_ Waltz No. 7 in C-Sharp Minor, Op. 64 No. 2.mp3", "Waltz in C-Sharp Minor"),
        Piece("data/plies/Frédéric Chopin - Mazurka Op. 33, No. 4.mp3", "Mazurka Op. 33, No. 4"),
        Piece("data/plies/Frédéric Chopin - Waltz in A Minor, B.150.mp3", "Waltz in A Minor"),
    )