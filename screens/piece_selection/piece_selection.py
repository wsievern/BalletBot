from kivy.lang import Builder
from kivy.properties import OptionProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from functools import partial

from screens.tap_tempo.tap_tempo import TapTempo
from state.app_state import mem
from models.piece import piece_collection

Builder.load_file("screens/piece_selection/piece_selection.kv")


class PieceSelection(BoxLayout):
    orientation = OptionProperty('vertical')

    def __init__(self, **kwargs):
        super(PieceSelection, self).__init__(**kwargs)

        for piece in piece_collection:
            piece_button = Button(text=piece.displayname)
            callback = partial(self.update_selected_piece, piece.filename, piece.displayname, piece.bpm)
            piece_button.bind(on_press=callback)
            self.add_widget(piece_button)

    def update_selected_piece(self, filename, displayname, bpm, _):
        # Second arg is "button", unused variables should be "_"
        print(f"Setting selected piece to: {filename}, bpm = {bpm}")
        mem.selected_piece_filename = filename
        mem.selected_piece_displayname = displayname
        mem.selected_piece_bpm = bpm
        TapTempo.update_bpm_slider(TapTempo, bpm)
