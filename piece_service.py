# filename, displayname


class Piece:

    def __init__(self, filename, displayname):
        self.filename = filename
        self.displayname = displayname


plie_piece = Piece(None, None)


class PieceCollection:
    pieces = ()


class PieceCollection1(PieceCollection):
    pieces = (
        Piece("BalletBot Music/Plies/Chopin_ Waltz No. 7 in C-Sharp Minor, Op. 64 No. 2.mp3", "Waltz in C-Sharp Minor"),
        Piece("BalletBot Music/Plies/Frédéric Chopin - Mazurka Op. 33, No. 4.mp3", "Mazurka Op. 33, No. 4"),
        Piece("BalletBot Music/Plies/Frédéric Chopin - Waltz in A Minor, B.150.mp3", "Waltz in A Minor"),
        Piece("BalletBot Music/Plies/Chopin_ Waltz No. 7 in C-Sharp Minor, Op. 64 No. 2.mp3", "Waltz in C-Sharp Minor")
    )


class PieceService:
    piece_collection = PieceCollection1
