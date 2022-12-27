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
        '''if plie_piece.displayname is not None:
            plie_piece_title_label = Label(text=str(plie_piece.displayname),
                                           pos_hint={'center_x': 0.5, 'center_y': .96},
                                           size_hint=(1, 1),
                                           font_size=30
                                           )

            self.add_widget(plie_piece_title_label)
            plie_piece_bpm_label = Label(text=str(plie_piece.bpm),
                                         pos_hint={'center_x': 0.5, 'center_y': .96},
                                         size_hint=(1, 1),
                                         font_size=30
            )
            self.add_widget(plie_piece_bpm_label)'''


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
        if plie_piece.filename is None:
            pass
        else:
            self.sound.stop()
            self.play_enabled = True
            self.stop_enabled = False


