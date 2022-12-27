# filename, displayname


class Piece:

    def __init__(self, filename, displayname, bpm):
        self.filename = filename
        self.displayname = displayname
        self.bpm = bpm

    def set_piece(self, filename, displayname, bpm):
        self.filename = filename
        self.displayname = displayname
        self.bpm = bpm
        print(str(self.filename) + " selected!")
        print(str(self.bpm))


plie_piece = Piece(None, None, None)


class PieceCollection:
    pieces = ()


class PieceCollection1(PieceCollection):
    pieces = (
        Piece("BalletBot Music/Plies/Chopin_ Waltz No. 7 in C-Sharp Minor, Op. 64 No. 2.mp3", "Waltz in C-Sharp Minor", 70),
        Piece("BalletBot Music/Plies/Frédéric Chopin - Mazurka Op. 33, No. 4.mp3", "Mazurka Op. 33, No. 4", 80),
        Piece("BalletBot Music/Plies/Frédéric Chopin - Waltz in A Minor, B.150.mp3", "Waltz in A Minor", 90),
        Piece("BalletBot Music/Plies/Chopin_ Waltz No. 7 in C-Sharp Minor, Op. 64 No. 2.mp3", "Waltz in C-Sharp Minor", 100)
    )


class PieceService:
    piece_collection = PieceCollection1
