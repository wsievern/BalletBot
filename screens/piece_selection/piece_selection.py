from kivy.lang import Builder
from kivy.properties import OptionProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from functools import partial

from state.app_state import mem
from models.piece import piece_collection

Builder.load_file("screens/piece_selection/piece_selection.kv")


class PieceSelection(BoxLayout):
    orientation = OptionProperty('vertical')

    def __init__(self, **kwargs):
        super(PieceSelection, self).__init__(**kwargs)

        for piece in piece_collection:
            piece_button = Button(text=piece.display_name)
            callback = partial(self.update_selected_piece_filename, piece.filename)
            piece_button.bind(on_press=callback)
            self.add_widget(piece_button)

    def update_selected_piece_filename(self, filename, _):
        # Second arg is "button", unused variables should be "_"
        print(f"Setting selected piece to: {filename}")
        mem.selected_piece_filename = filename