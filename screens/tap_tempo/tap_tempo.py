from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import BoundedNumericProperty
from kivy.uix.floatlayout import FloatLayout
import time
from kivy.uix.button import Button
from kivy.uix.label import Label
from state.app_state import mem

Builder.load_file("screens/tap_tempo/tap_tempo.kv")


class TapTempo(FloatLayout):
    tempo = BoundedNumericProperty(0, min=0, max=300)

    def __init__(self, **kwargs):
        super(TapTempo, self).__init__(**kwargs)
        self.time_list = []
        self.app = App.get_running_app()
        tap_tempo = Button(
            text="TAP TEMPO",
            size_hint=(.25, .1),
            pos_hint={'center_x': .8, 'center_y': .7},
            font_name='GillSans'
        )
        tap_tempo.bind(on_press=self.key_pressed)
        self.add_widget(tap_tempo)
        self.display_tempo = Label(
            text=str(0),
            size_hint=(.25, .125),
            pos_hint={'center_x': .725, 'center_y': .62},
            font_size= 20,
            font_name='GillSans'
        )
        self.add_widget(self.display_tempo)
        reset = Button(
            text="RESET",
            size_hint=(.125, .04),
            pos_hint={'center_x': .865, 'center_y': .62},
            font_name='GillSans'

        )
        reset.bind(on_press=self.reset_tempo)
        self.add_widget(reset)

    def tap_estimate(self):
        self.time_list.append(time.time())
        list_len = len(self.time_list)
        print(self.time_list)
        n = 6
        if list_len > 1:
            if self.time_list[-1] - self.time_list[-2] > 2:
                self.time_list = self.time_list[-1:]
            else:
                if list_len < n:
                    interval = (self.time_list[-1] - self.time_list[0]) / (list_len - 1)
                    TapTempo.tempo = int(60 / interval)
                else:
                    interval = (self.time_list[-1] - self.time_list[-n]) / (n - 1)
                    TapTempo.tempo = int(60 / interval)
        else:
            pass

    def key_pressed(self, instance):
        self.tap_estimate()
        if len(self.time_list) > 1:
            self.display_tempo.text = (str(TapTempo.tempo))
        if len(self.time_list) > 2 and TapTempo.tempo < self.app.root.ids.playback.ids.bpm_slider.max:
            self.app.root.ids.playback.ids.bpm_slider.value = TapTempo.tempo
            self.app.root.ids.playback.ids.display_slider_value.text = str(round(TapTempo.tempo * (mem.selected_piece_bpm ** -1), 1)) + "x : " + (str(round(TapTempo.tempo, 0)))

    def reset_tempo(self, instance):
        if TapTempo.tempo != 0:
            TapTempo.tempo = 0
            self.display_tempo.text = str(0)
            if mem.selected_piece_bpm is not None:
                App.get_running_app().root.ids.playback.ids.display_slider_value.text = '1x : ' + str(mem.selected_piece_bpm)
                self.app.root.ids.playback.ids.bpm_slider.value = mem.selected_piece_bpm
            else:
                App.get_running_app().root.ids.playback.ids.display_slider_value.text = '1x'
        elif mem.selected_piece_bpm is not None:
            App.get_running_app().root.ids.playback.ids.display_slider_value.text = '1x : ' + str(
                mem.selected_piece_bpm)
            self.app.root.ids.playback.ids.bpm_slider.value = mem.selected_piece_bpm
        else:
            pass
