from kivy.lang import Builder
from kivy.properties import OptionProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from piece_service import PieceCollection1, plie_piece

Builder.load_file("piece_selection.kv")


class PieceSelection(BoxLayout):
    orientation = OptionProperty('vertical')

    def __init__(self, **kwargs):
        super(PieceSelection, self).__init__(**kwargs)

        for i in range(len(PieceCollection1.pieces)):
            pb = Button(text=PieceCollection1.pieces[i].displayname)
            pb.bind(on_press=lambda x: self.load_plie_piece(PieceCollection1.pieces[i].filename))
            self.add_widget(pb)

    def load_plie_piece(self, filename):
        self.plie_piece = filename
        assert isinstance(self.plie_piece, object)
        plie_piece.filename = self.plie_piece


