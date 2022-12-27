from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.label import Label


class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push(self, screen_name):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition.direction = "left"
            self.current = screen_name

    def pop(self):
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]
            del self.screen_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name

    '''def play_audio(self):
        self.sound = Piece.loaded_piece
        #self.song_title = self.song_list[random.randrange(0, self.song_count)]
        #print(self.song_title)
        #self.sound = SoundLoader.load('{}/{}'.format(self.music_dir, self.song_title))
        self.sound.play()
        self.play_enabled = False
        self.stop_enabled = True'''

    def display_title(self):
        layout = MDRelativeLayout(md_bg_color=[0, 0.5, 1, 1])
        self.songlabel = Label(pos_hint={'center_x': 0.5, 'center_y': .96},
                               size_hint=(1, 1),
                               font_size=30)
        layout.add_widget(self.songlabel)
        self.songlabel.text = "===== Playing ~ ====="
        return layout
