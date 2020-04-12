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
        self.ingameBool = False

    def set_game(self,g):
        self.game = g

    def arrange(self,cards,boolpl):
        if boolpl:
            print("pl"+str(len(cards)))
            print(cards)
            self.ids["pl_card1"].source = "./img/blank.png"
            self.ids["pl_card2"].source = "./img/blank.png"
            self.ids["pl_card3"].source = "./img/blank.png"
            self.ids["pl_card4"].source = "./img/blank.png"
            self.ids["pl_card5"].source = "./img/blank.png"
            self.ids["pl_card6"].source = "./img/blank.png"

            if len(cards) == 2:
                self.ids["pl_card3"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["pl_card4"].source = "./img/card_"+str(cards[1])+".png"
            elif len(cards) == 3:
                self.ids["pl_card1"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["pl_card2"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["pl_card3"].source = "./img/card_"+str(cards[2])+".png"
            elif len(cards) == 4:
                self.ids["pl_card1"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["pl_card2"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["pl_card3"].source = "./img/card_"+str(cards[2])+".png"
                self.ids["pl_card4"].source = "./img/card_"+str(cards[3])+".png"
            elif len(cards) == 5:
                self.ids["pl_card1"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["pl_card2"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["pl_card3"].source = "./img/card_"+str(cards[2])+".png"
                self.ids["pl_card4"].source = "./img/card_"+str(cards[3])+".png"
                self.ids["pl_card5"].source = "./img/card_"+str(cards[4])+".png"
            elif len(cards) == 6:
                self.ids["pl_card1"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["pl_card2"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["pl_card3"].source = "./img/card_"+str(cards[2])+".png"
                self.ids["pl_card4"].source = "./img/card_"+str(cards[3])+".png"
                self.ids["pl_card5"].source = "./img/card_"+str(cards[4])+".png"
                self.ids["pl_card6"].source = "./img/card_"+str(cards[5])+".png"

        else:
            print("dl"+str(len(cards)))
            print(cards)
            print("ループしてるのここ")
            self.ids["dl_card1"].source = "./img/blank.png"
            self.ids["dl_card2"].source = "./img/blank.png"
            self.ids["dl_card3"].source = "./img/blank.png"
            self.ids["dl_card4"].source = "./img/blank.png"
            self.ids["dl_card5"].source = "./img/blank.png"
            self.ids["dl_card6"].source = "./img/blank.png"

            if len(cards) == 1:
                self.ids["dl_card3"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["dl_card4"].source = "./img/card_back.png"
            elif len(cards) == 2:
                self.ids["dl_card3"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["dl_card4"].source = "./img/card_"+str(cards[1])+".png"
            elif len(cards) == 3:
                self.ids["dl_card1"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["dl_card2"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["dl_card3"].source = "./img/card_"+str(cards[2])+".png"
            elif len(cards) == 4:
                self.ids["dl_card1"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["dl_card2"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["dl_card3"].source = "./img/card_"+str(cards[2])+".png"
                self.ids["dl_card4"].source = "./img/card_"+str(cards[3])+".png"
            elif len(cards) == 5:
                self.ids["dl_card1"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["dl_card2"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["dl_card3"].source = "./img/card_"+str(cards[2])+".png"
                self.ids["dl_card4"].source = "./img/card_"+str(cards[3])+".png"
                self.ids["dl_card5"].source = "./img/card_"+str(cards[4])+".png"
            elif len(cards) == 6:
                self.ids["dl_card1"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["dl_card2"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["dl_card3"].source = "./img/card_"+str(cards[2])+".png"
                self.ids["dl_card4"].source = "./img/card_"+str(cards[3])+".png"
                self.ids["dl_card5"].source = "./img/card_"+str(cards[4])+".png"
                self.ids["dl_card6"].source = "./img/card_"+str(cards[5])+".png"


    def deal(self):        # ボタンをクリック時
        if self.ingameBool == False:
            self.ingameBool = True
            self.game.clear()
            self.ids["wltextLabel"].text = ""
            self.ids["hand_num"].text = str(self.game.pl.get_tip())
            self.game.tip_bet_gui(int(self.ids["testSlider"].value))
            self.ids["hand_num"].text = str(self.game.pl.get_tip())

            self.game.pl.set_hand(self.game.hit_gui())
            self.game.pl.set_hand(self.game.hit_gui())

            self.game.dl.set_hand(self.game.hit_gui())
            # self.game.dl.set_hand(self.game.hit_gui())

            self.arrange(self.game.pl.get_hand(),True)
            self.arrange(self.game.dl.get_hand(),False)

            self.ids["pl_score"].text = str(self.game.pl.score_gui())
            self.ids["dl_score"].text = str(self.game.dl.score_gui())


    def buttonClicked(self):# ボタンをクリック時
        print("ok")

    def hit(self):# ボタンをクリック時
        if self.ingameBool == True:
            self.game.pl.set_hand(self.game.hit_gui())
            self.arrange(self.game.pl.get_hand(),True)
            self.ids["pl_score"].text = str(self.game.pl.score_gui())
            score = self.game.pl.score_gui()

            if "/" in score:
                list = score.split(",")
                max = max(list)
                max = int(max)
            else:
                max = int(score)

            if max >21:
                plmax = self.game.pl.get_sum()
                print(plmax)
                dlmax = self.game.dl.get_sum()
                print(dlmax)
                self.ids["wltextLabel"].text = self.game.win_lose_gui(plmax,dlmax)
                self.ingameBool = False
            elif self.game.pl.score_gui()  == 21:
                plmax = self.game.pl.get_sum()
                print(plmax)
                dlmax = self.game.dl.get_sum()
                print(dlmax)
                self.ids["wltextLabel"].text = self.game.win_lose_gui(plmax,dlmax)
                self.ingameBool = False

    def hit_d(self):

        plmax = self.game.pl.get_sum()
        print(plmax)
        dlmax = self.game.dl.get_sum()
        print(dlmax)

        while dlmax < 17:
            if dlmax < plmax:
                self.game.dl.set_hand(self.game.hit_gui())
                self.arrange(self.game.dl.get_hand(),False)
                self.ids["dl_score"].text = str(self.game.dl.score_gui())
            elif dlmax >= plmax:
                break

            if dlmax > 22:
                break

            dlmax = self.game.dl.get_sum()


    def stand(self):
        if self.ingameBool == True:
            self.hit_d()
            plmax = self.game.pl.get_sum()
            print(plmax)
            dlmax = self.game.dl.get_sum()
            print(dlmax)
            self.ids["wltextLabel"].text = self.game.win_lose_gui(plmax,dlmax)
            self.ingameBool = False


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'

    def build(self):

        return TextWidget()


if __name__ == '__main__':
    TestApp().run()
