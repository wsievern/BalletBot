import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

kivy.require('2.0.0')

Window.size = (500, 1000)


class BalletApp(MDApp):
    def build(self):
        self.root = Builder.load_file("screens/ballet.kv")
    pass


BalletApp().run()
