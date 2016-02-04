from kivy.app import App

# tracks the multitouch, make thing bigger and samller and moves thing
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
#Inputing text and updating the label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class SpApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(font_size=150,
                      size_hint_y=None,
                      height=200,
                      text='Defalut')
        f = FloatLayout()        # three Widgets
        s = Scatter()
        l = Label(text= "Defalut!",
                  font_size=150)

        t.bind(text=l.setter('text'))
        #Binding texinput and label

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(t)
        b.add_widget(f)
        return b

if __name__ == "__main__":
    SpApp().run()
