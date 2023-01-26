from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (750, 750)

kv = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: sp(100)
        
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: e1
                min: -360.
                max: 360.
            Label:
                text: 'Закрыть с 0 = {}'.format(e1.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: e2
                min: -360.
                max: 360.
                value: 360
            Label:
                text: 'Закрыть с 360 = {}'.format(e2.value)

    BoxLayout:
        size_hint_y: None
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: wm
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Растянуть по горизонтали. = {}'.format(wm.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: hm
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Растянуть по вертикали. = {}'.format(hm.value)
        Button:
            text: 'Вернуть исходное'
            on_press: wm.value = 1; hm.value = 1

    FloatLayout:
        canvas:
            Color:
                rgb: 1, 1, 1
            Ellipse:
                pos: 100, 100
                size: 300 * wm.value, 300 * hm.value
                source: 'mavic-2-enterprise-side.jpg'
                angle_start: e1.value
                angle_end: e2.value

'''


class Первое_приложениеApp(App):
    def build(self):
        return Builder.load_string(kv)


Первое_приложениеApp().run()