from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button

class Btn(Button):
    pass

class app(App):
    def build(self):
        self.load_kv("style.kv")
        return Btn()




if __name__ == '__main__':

    app().run()