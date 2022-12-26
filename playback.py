from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout

# from piece_selection import PieceSelection
from piece_service import plie_piece
from kivy.core.audio import SoundLoader

Builder.load_file("playback.kv")


class Playback(FloatLayout):
    play_enabled = BooleanProperty(True)
    stop_enabled = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(Playback, self).__init__(**kwargs)
        self.play_enabled = True
        self.stop_enabled = False
        self.sound = None

    def play_plie_piece(self):
        self.sound = SoundLoader.load(plie_piece.filename)
        self.sound.play()
        self.play_enabled = False
        self.stop_enabled = True

    def stop_audio(self):
        self.sound.stop()
        self.play_enabled = True
        self.stop_enabled = False

