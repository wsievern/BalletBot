from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import time
from kivy.uix.button import Button
from kivy.uix.label import Label

Builder.load_file("tap_tempo.kv")

class TapTempo(FloatLayout):
    def __init__(self, **kwargs):
        super(TapTempo, self).__init__(**kwargs)
        self.time_list = []
        self.tempo = 0
        tap_tempo = Button(
            text="Tap Tempo",
            size_hint=(.25, .125),
            pos=(20, 300))
        tap_tempo.bind(on_press=self.key_pressed)
        self.add_widget(tap_tempo)
        self.display_tempo = Label(
                text=str(self.tempo),
                size_hint=(.25, .125),
                pos=(200, 300))
        self.add_widget(self.display_tempo)

    def tap_estimate(self):
        self.tempo = 0
        # global time_list #, scale
        self.time_list.append(time.time())
        list_len = len(self.time_list)
        print(self.time_list)
        n = 6
        if list_len > 1:
            # If two time far away from each other
            # throw away the former times, only left the last one
            if self.time_list[-1] - self.time_list[-2] > 2:
                self.time_list = self.time_list[-1:]
            else:
                if list_len < n:
                    interval = (self.time_list[-1] - self.time_list[0]) / (list_len - 1)
                    self.tempo = int(60 / interval)
                else:
                    interval = (self.time_list[-1] - self.time_list[-n]) / (n - 1)
                    self.tempo = int(60 / interval)
                # scale.set(tempo)
        else:
            # Keep tapping
            pass
            # print(time_list)

    def key_pressed(self, instance):
        '''global ON
        if event.char == ' ':
            ON = not ON
        elif event.char == 't':'''
        self.tap_estimate()
        #print(self.tempo)
        self.display_tempo.text = (str(self.tempo))

    '''def tempo_tap(self):
        print("tapped")'''
