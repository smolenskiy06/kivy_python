
from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


from kivy.lang import Builder

from kivy.core.window import Window


#Window.size = (720, 1280)
Window.size = (380,453)


KV = ("""
<Prin>
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'mavic-2-enterprise-side.jpg'

        Label:
            id: label
            pos: 0, 100
	        size: 100, 50
	        color: .8,.9,0,1
	        font_size: 32
            
            
  
    
        Button:
            text: 'ВПЕРЕД'
            size_hint: None, None
            size_hint: 0.5, 0.1
            pos_hint: {'center_x': .5, 'center_y': .5}
            padding: 10, 0
            on_press: root.start()
   
        

""")




class Prin(BoxLayout):
    Builder.load_string(KV)

    def __init__(self, **kwargs):
        super(Prin, self).__init__(**kwargs)

    def start(self):
        self.ids.label.text = "Кнопка нажата"

    def on_press_button(self):
        print('Вы нажали на кнопку!')

class ПЕРВОЕ_ПРИЛОЖЕНИЕApp(App):
    def build(self):
        return Prin()



if __name__ == "__main__":
    app = ПЕРВОЕ_ПРИЛОЖЕНИЕApp()
    app.run()