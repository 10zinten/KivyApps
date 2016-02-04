from kivy.app import App
from kivy.uix.button import Button

class SpApp(App):
    def build(self):
        return Button(text= "hello!",
                      background_color= (2,1,0,1),
                      font_size=150)

if __name__ == "__main__":
    SpApp().run()
