import time
import librosa
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import OptionProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from functools import partial
from models.sound import Sound
from screens.playback.playback import Playback
from state.app_state import mem
from models.piece import piece_collection

Builder.load_file("screens/piece_selection/piece_selection.kv")


class PieceSelection(BoxLayout):
    orientation = OptionProperty('vertical')
    piece_duration = 0

    def __init__(self, **kwargs):
        super(PieceSelection, self).__init__(**kwargs)

    def populate_piece_list(self):
        # delete buttons (except action bar) from layout if pieces were previously loaded
        while len(self.children) > 1:
            self.remove_widget(self.children[0])

        for piece in piece_collection:
            # if a tempo was tapped on previous screen, only load pieces near that tempo
            app = App.get_running_app()
            tempo = app.root.ids.tap_tempo.tempo
            if tempo > 0 and piece.bpm in range(tempo - 16, tempo + 16):
                piece_button = Button(text=piece.displayname)
                callback = partial(self.update_selected_piece, piece.filename, piece.displayname, piece.bpm, piece.info)
                piece_button.bind(on_press=callback)
                self.add_widget(piece_button)
            # if tempo wasn't tapped, load all pieces in current piece_collection
            elif tempo == 0:
                piece_button = Button(text=piece.displayname)
                callback = partial(self.update_selected_piece, piece.filename, piece.displayname, piece.bpm, piece.info)
                piece_button.bind(on_press=callback)
                self.add_widget(piece_button)
            else:
                pass

    def update_selected_piece(self, filename, displayname, bpm, info, _):
        # Second arg is "button", unused variables should be "_"
        print(f"Setting selected piece to: {filename}, bpm = {bpm}")
        mem.selected_piece_filename = filename
        mem.selected_piece_displayname = displayname
        mem.selected_piece_bpm = bpm
        mem.selected_piece_info = info
        Playback.s1 = Sound.from_file(mem.selected_piece_filename, sr=44100)
        # if a tempo was tapped, update bpm slider with tapped tempo
        app = App.get_running_app()
        tempo = app.root.ids.tap_tempo.tempo
        if tempo > 0:
            Playback.update_bpm_slider(bpm, tempo)
        else:
            Playback.update_bpm_slider(bpm, bpm)

    def update_piece_selection_text(self, widget):
        # updates "Select Piece" text on button on previous screen
        if mem.selected_piece_displayname:
            widget.text = mem.selected_piece_displayname

    def populate_piece_info(self, widget):
        if mem.selected_piece_info:
            widget.text = mem.selected_piece_info

    def update_time_remaining(self, widget):
        if mem.selected_piece_filename:
            PieceSelection.piece_duration = librosa.get_duration(y=Playback.s1.y, sr=44100)
            widget.text = time.strftime('%M:%S', time.gmtime(PieceSelection.piece_duration))
            # also sets progress_slider max value
            app = App.get_running_app()
            app.root.ids.playback.ids.progress_bar.max = PieceSelection.piece_duration

