from kivy.app import App

from kivy.uix.scatter import Scatter
# tracks the multitouch, make thing bigger and samller and moves thing
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class SpApp(App):
    def build(self):
        f = FloatLayout()        # three Widgets
        s = Scatter()
        l = Label(text= "Tenzin!",
                  font_size=150)

        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == "__main__":
    SpApp().run()
