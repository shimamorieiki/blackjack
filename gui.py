#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty
import main

class TextWidget(Widget):
    text = StringProperty()    # プロパティの追加

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''
        g = main.Game()
        self.set_game(g)

    def set_game(self,g):
        self.game = g

    def deal(self):        # ボタンをクリック時
        print("Tip:"+ str(self.game.pl.get_tip()))


    def buttonClicked(self):# ボタンをクリック時
        print("ok")


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'

    def build(self):

        return TextWidget()


if __name__ == '__main__':
    TestApp().run()
