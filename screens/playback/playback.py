from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader

from state.app_state import mem

Builder.load_file("screens/playback/playback.kv")


class Playback(FloatLayout):
    play_enabled = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(Playback, self).__init__(**kwargs)
        # TODO: probably only need one boolean, can always use inverse of it
        self.play_enabled = True
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

    # TODO: rename to play_audio for consistency?
    def play_audio(self):
        filename = mem.selected_piece_filename
        print(f"Playing: {filename}")
        if not filename:
            # TODO: handle error
            print("no file selected")
        self.sound = SoundLoader.load(filename)
        self.sound.play()
        self.play_enabled = False

    def stop_audio(self):
        filename = mem.selected_piece_filename
        print(f"Playing: {filename}")
        # TODO: probably just need to check if song is playing to stop, filename not really relevant here
        if filename is not None:
            self.sound.stop()
            self.play_enabled = True


