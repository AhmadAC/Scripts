#for Python 3.11.0 on Windows, install kivy with the following commands:
#python -m pip install kivy --pre --no-deps --index-url  https://kivy.org/downloads/simple/
#python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Canvas, Line
from kivy.uix.widget import Widget

class TriangleApp(App):
    def build(self):
        widget = Widget()
        return widget

    def on_start(self):
        window_width = Window.width
        window_height = Window.height

        with self.root.canvas:
            self.canvas = Canvas()
            points = [
                window_width / 2 + 80, window_height / 2,
                window_width / 2, window_height / 2 - 50,
                window_width / 2, window_height / 2 + 50
            ]
            Line(points=points, width=2, close=True)

if __name__ == '__main__':
    TriangleApp().run()
