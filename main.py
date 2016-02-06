from kivy.app import App
from kivy.lang import Builder

# tracks the multitouch, make thing bigger and samller and moves thing
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
#Inputing text and updating the label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty

import random

class ScatterTextWidget(BoxLayout):

    text_colour = ListProperty([1,0,0,1])

    def change_label_colour(self, *args):
        colour = [random.random() for i in xrange(3)] + [1]
        self.text_colour = colour

presentation = Builder.load_file("SpApp.kv")

class SpApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    SpApp().run()
