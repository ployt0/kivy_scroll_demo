import os
import sys

from kivy.app import App
from kivy.uix.widget import Widget


class MainUI(Widget):
    pass


class MainApp(App):
    def __init__(self, input_dir: str, **kwargs):
        super().__init__(**kwargs)
        self.input_dir = input_dir

    def build(self):
        return MainUI()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
    else:
        input_dir = os.getcwd()
    MainApp(input_dir).run()