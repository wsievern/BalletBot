import time

import numpy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty, Clock, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from models.sampler import Sampler
from state.app_state import mem

Builder.load_file("screens/playback/playback.kv")

sampler = Sampler(sr=44100)


class Playback(FloatLayout):
    play_enabled = BooleanProperty(True)
    s1 = None

    def __init__(self, **kwargs):
        super(Playback, self).__init__(**kwargs)
        self.play_enabled = True
        self.time_elapsed = 0
        self.event = None
        # self.piece_length = 0

    def play_audio(self):
        filename = mem.selected_piece_filename
        print(f"Playing: {filename}")
        if not filename:
            print("no file selected")
            pass
        else:
            # keeping the mp3 sample rates at 44100 dramatically speeds up load times
            # moved the sound loading to piece_selection.py
            from screens.piece_selection.piece_selection import PieceSelection
            self.piece_length = PieceSelection.piece_duration * (Playback.s1.stretch_factor ** -1)
            sampler.play(Playback.s1)
            self.event = Clock.schedule_interval(self.advance_time, 1)
            self.play_enabled = False

    def stop_audio(self):
        filename = mem.selected_piece_filename
        print(f"Stopping: {filename}")
        sampler.remove(Playback.s1)
        self.event.cancel()
        self.ids.time_elapsed.text = "00:00"
        self.time_elapsed = 0
        self.ids.progress_bar.value = 0
        self.play_enabled = True

    def timestretch_audio(self, widget1, widget2, *args):
        if Playback.s1 is not None:
            Playback.s1.stretch_factor = (widget1.value * (mem.selected_piece_bpm ** -1))
            # This feels like it shouldn't belong here! But for some reason
            # I get an error when I run this import statement at the top of the page
            from screens.piece_selection.piece_selection import PieceSelection
            self.piece_length = PieceSelection.piece_duration * (Playback.s1.stretch_factor ** -1)
            self.ids.progress_bar.max = self.piece_length
            if self.event:
                print(self.time_elapsed)
                time_elapsed_for_calc = self.time_elapsed * (Playback.s1.stretch_factor ** -1)
                widget2.text = time.strftime('%M:%S', time.gmtime(self.piece_length - time_elapsed_for_calc))
                self.time_elapsed = time_elapsed_for_calc
                # widget3.text = time.strftime('%M:%S', time.gmtime(self.time_elapsed * Playback.s1.stretch_factor))
            else:
                widget2.text = time.strftime('%M:%S', time.gmtime(self.piece_length))

    def update_bpm_slider(x, y):
        app = App.get_running_app()
        app.root.ids.playback.ids.bpm_slider.min = (x * .5)
        app.root.ids.playback.ids.bpm_slider.max = (x * 2)
        app.root.ids.playback.ids.bpm_slider.value = y
        app.root.ids.playback.ids.display_slider_value.text = str(
            round(y * (mem.selected_piece_bpm ** -1), 1)) + "x : " + (str(round(y, 0)) + " BPM")

    def display_bpm_slider_value(self, widget, *args):
        self.ids.display_slider_value.text = str(round(widget.value * (mem.selected_piece_bpm ** -1), 1)) + "x : " + (
                    str(round(widget.value, 0)) + " BPM")

    def adjust_volume(self, widget, *args):
        Playback.s1.volume = widget.value


    def advance_time(self, dt):
        self.time_elapsed += 1
        self.ids.time_elapsed.text = time.strftime('%M:%S', time.gmtime(self.time_elapsed))
        self.ids.progress_bar.value += 1
        self.ids.time_remaining.text = time.strftime('%M:%S', time.gmtime(self.piece_length - self.time_elapsed))
        if self.ids.time_remaining.text == "00:00":
            self.stop_audio()
