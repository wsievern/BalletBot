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
            piece_button = Button(text=PieceCollection1.pieces[i].displayname)
            piece_data = (
                PieceCollection1.pieces[i].filename,
                PieceCollection1.pieces[i].displayname,
                PieceCollection1.pieces[i].bpm
            )
            piece_button.bind(
                on_press=lambda widget,
                appname=piece_data[0],
                appname2=piece_data[1],
                appname3=piece_data[2]: plie_piece.set_piece(appname, appname2, appname3)
            )
            self.add_widget(piece_button)

    '''def load_plie_piece(self, filename):
        self.plie_piece = filename
        assert isinstance(self.plie_piece, object)
        plie_piece.filename = self.plie_piece'''
