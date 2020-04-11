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

    def arrange(self,cards,boolpl):
        if boolpl:
            print("pl"+str(len(cards)))
            print(cards)
            self.ids["pl_card1"].source = ""
            self.ids["pl_card2"].source = ""
            self.ids["pl_card3"].source = ""
            self.ids["pl_card4"].source = ""
            self.ids["pl_card5"].source = ""
            self.ids["pl_card6"].source = ""

            if len(cards) == 2:
                self.ids["pl_card3"].source = "./img/card_club_"+str(cards[0]%13+1)+".png"
                self.ids["pl_card4"].source = "./img/card_club_"+str(cards[1]%13+1)+".png"
            elif len(cards) == 3:
                self.ids["pl_card1"].source = "./img/card_club_"+str(cards[0]%13+1)+".png"
                self.ids["pl_card2"].source = "./img/card_club_"+str(cards[1]%13+1)+".png"
                self.ids["pl_card3"].source = "./img/card_club_"+str(cards[2]%13+1)+".png"
            elif len(cards) == 4:
                self.ids["pl_card1"].source = "./img/card_club_"+str(cards[0]%13+1)+".png"
                self.ids["pl_card2"].source = "./img/card_club_"+str(cards[1]%13+1)+".png"
                self.ids["pl_card3"].source = "./img/card_club_"+str(cards[2]%13+1)+".png"
                self.ids["pl_card4"].source = "./img/card_club_"+str(cards[3]%13+1)+".png"
            elif len(cards) == 5:
                self.ids["pl_card1"].source = "./img/card_club_"+str(cards[0]%13+1)+".png"
                self.ids["pl_card2"].source = "./img/card_club_"+str(cards[1]%13+1)+".png"
                self.ids["pl_card3"].source = "./img/card_club_"+str(cards[2]%13+1)+".png"
                self.ids["pl_card4"].source = "./img/card_club_"+str(cards[3]%13+1)+".png"
                self.ids["pl_card5"].source = "./img/card_club_"+str(cards[4]%13+1)+".png"
            elif len(cards) == 6:
                self.ids["pl_card1"].source = "./img/card_club_"+str(cards[0]%13+1)+".png"
                self.ids["pl_card2"].source = "./img/card_club_"+str(cards[1]%13+1)+".png"
                self.ids["pl_card3"].source = "./img/card_club_"+str(cards[2]%13+1)+".png"
                self.ids["pl_card4"].source = "./img/card_club_"+str(cards[3]%13+1)+".png"
                self.ids["pl_card5"].source = "./img/card_club_"+str(cards[4]%13+1)+".png"
                self.ids["pl_card6"].source = "./img/card_club_"+str(cards[5]%13+1)+".png"

        else:
            print("dl"+str(len(cards)))

    def deal(self):        # ボタンをクリック時
        self.game.clear()
        self.ids["hand_num"].text = str(self.game.pl.get_tip())
        self.game.tip_bet_gui(int(self.ids["testSlider"].value))
        self.ids["hand_num"].text = str(self.game.pl.get_tip())

        self.game.pl.set_hand(self.game.hit_gui())
        self.game.pl.set_hand(self.game.hit_gui())

        self.game.dl.set_hand(self.game.hit_gui())
        self.game.dl.set_hand(self.game.hit_gui())

        self.arrange(self.game.pl.get_hand(),True)
        self.arrange(self.game.dl.get_hand(),False)

        self.ids["pl_score"].text = str(self.game.pl.score_gui())


    def buttonClicked(self):# ボタンをクリック時
        print("ok")

    def hit(self):# ボタンをクリック時
        self.game.pl.set_hand(self.game.hit_gui())
        self.arrange(self.game.pl.get_hand(),True)
        self.ids["pl_score"].text = str(self.game.pl.score_gui())

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'

    def build(self):

        return TextWidget()


if __name__ == '__main__':
    TestApp().run()
