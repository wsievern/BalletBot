from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import time
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from functools import partial
# import librosa as lr
# import numpy as np
# import matplotlib.pyplot as plt
# from glob import glob


# Builder.load_file("screens/tap_tempo/tap_tempo.kv")


class TapTempo(FloatLayout):
    #slider_val = NumericProperty(50)

    def __init__(self, **kwargs):
        super(TapTempo, self).__init__(**kwargs)
        self.time_list = []
        self.tempo = 0
        tap_tempo = Button(
            text="TAP TEMPO",
            size_hint=(.25, .1),
            pos=(50, 600),
            font_name=('/Users/willsievern/Documents/GitHub/BalletBot/gillsans.ttf')
            # I have a feeling I'm calling this font incorrectly
        )
        tap_tempo.bind(on_press=self.key_pressed)
        self.add_widget(tap_tempo)
        self.display_tempo = Label(
            text=str(self.tempo),
            size_hint=(.25, .125),
            pos=(150, 275),
            font_name=('/Users/willsievern/Documents/GitHub/BalletBot/gillsans.ttf')
        )
        self.add_widget(self.display_tempo)

        self.bpm_slider = Slider(
            min=0,
            max=100,
            value=50,
            orientation="vertical",
            size_hint_y=.4,
            pos_hint={'center_x': .6, 'center_y': .4},
            padding=12,
            value_track=True,
            sensitivity='handle',
            step=1

        )
        callback = partial(self.on_slider_value, self.bpm_slider)
        self.bpm_slider.bind(on_touch_move=callback)
        self.add_widget(self.bpm_slider)

        self.display_slider_value = Label(text=str(50))
        self.add_widget(self.display_slider_value)

    def on_slider_value(self, widget, _, *args):
        self.display_slider_value.text = (str(widget.value))




    def update_bpm_slider(self, x):
        self.bpm_slider.min = (x / 2)
        self.bpm_slider.max = (x * 2)
        self.bpm_slider.value = x
        #self.display_slider_value.text = str(mem.selected_piece_bpm)
        # if self.tempo is not 0:
        # self.bpm_slider.value = self.tempo
        # self.slider_val = self.tempo

    def tap_estimate(self):
        self.tempo = 0
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
                    self.tempo = int(60 / interval)
                else:
                    interval = (self.time_list[-1] - self.time_list[-n]) / (n - 1)
                    self.tempo = int(60 / interval)
        else:
            pass

    def key_pressed(self, instance):
        self.tap_estimate()
        self.display_tempo.text = (str(self.tempo))




'''y, sr = lr.load(mem.selected_piece_filename)
y_fast = lr.effects.time_stretch(y, 2.0)
time = np.arange(0,len(y_fast))/sr
fig, ax = plt.subplots()
ax.plot(time,y_fast)
ax.set(xlabel='Time(s)',ylabel='sound amplitude')
plt.show()

y_slow = lr.effects.time_stretch(y, 0.5)
time = np.arange(0,len(y_slow))/sr
fig, ax = plt.subplots()
ax.plot(time,y_slow)
ax.set(xlabel='Time(s)',ylabel='sound amplitude')
plt.show()'''
