import kivy
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

kivy.require('2.0.0')

Window.size = (500, 1000)

LabelBase.register(name='GillSans',
                   fn_regular='data/fonts/gillsans.ttf')


class BalletApp(MDApp):
    def build(self):
        self.root = Builder.load_file("screens/ballet.kv")

    pass


BalletApp().run()
