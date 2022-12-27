from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader

from state.app_state import mem

Builder.load_file("screens/playback/playback.kv")


class Playback(FloatLayout):
    play_enabled = BooleanProperty(True)
    stop_enabled = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(Playback, self).__init__(**kwargs)
        self.play_enabled = True
        self.stop_enabled = False
        self.sound = None

    def play_plie_piece(self):
        filename = mem.selected_piece_filename
        print(f"Playing: {filename}")
        if not filename:
            # TODO: handle error
            print("no file selected")
        self.sound = SoundLoader.load(filename)
        self.sound.play()
        self.play_enabled = False
        self.stop_enabled = True

    def stop_audio(self):
        self.sound.stop()
        self.play_enabled = True
        self.stop_enabled = False

