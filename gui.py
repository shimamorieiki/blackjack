#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty
import main
import time

class TextWidget(Widget):
    text = StringProperty()    # プロパティの追加

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''
        g = main.Game()
        self.set_game(g)
        # self.ids["pl_card1"].source = self.game.resource_path("card_1.png")
        self.ingameBool = False


    def set_game(self,g):
        self.game = g

    def arrange(self,cards,boolpl):
        if boolpl:
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
                self.ids["pl_card2"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["pl_card3"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["pl_card4"].source = "./img/card_"+str(cards[2])+".png"
            elif len(cards) == 4:
                self.ids["pl_card2"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["pl_card3"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["pl_card4"].source = "./img/card_"+str(cards[2])+".png"
                self.ids["pl_card5"].source = "./img/card_"+str(cards[3])+".png"
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
                self.ids["dl_card2"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["dl_card3"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["dl_card4"].source = "./img/card_"+str(cards[2])+".png"
            elif len(cards) == 4:
                self.ids["dl_card2"].source = "./img/card_"+str(cards[0])+".png"
                self.ids["dl_card3"].source = "./img/card_"+str(cards[1])+".png"
                self.ids["dl_card4"].source = "./img/card_"+str(cards[2])+".png"
                self.ids["dl_card5"].source = "./img/card_"+str(cards[3])+".png"
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

    def scorepaint(self):
        plmax = self.game.pl.get_sum()
        dlmax = self.game.dl.get_sum()
        if plmax == 21:
            self.ids["pl_score"].text = "BlackJack"
        elif plmax > 21:
            self.ids["pl_score"].text = "Bust"
        else:
            self.ids["pl_score"].text = str(plmax)

        if dlmax == 21:
            self.ids["dl_score"].text = "BlackJack"
        elif dlmax > 21:
            self.ids["dl_score"].text = "Bust"
        else:
            self.ids["dl_score"].text = str(dlmax)

        if self.game.win_lose_gui(plmax,dlmax) == 1:
            self.ids["wltextLabel"].source = "./img/win.png"
            if plmax == 21:
                self.game.pl.set_tip_add(int(self.game.get_bet()*2.5))
            else:
                self.game.pl.set_tip_add(self.game.get_bet()*2)

            self.ids["hand_num"].text = str(self.game.pl.get_tip())

        elif self.game.win_lose_gui(plmax,dlmax) == 2:
            self.ids["wltextLabel"].source = "./img/lose.png"
        elif self.game.win_lose_gui(plmax,dlmax) == 3:
            self.ids["wltextLabel"].source = "./img/draw.png"
            self.game.pl.set_tip_add(self.game.get_bet())
            self.ids["hand_num"].text = str(self.game.pl.get_tip())

    def hit(self):# ボタンをクリック時
        if self.ingameBool == True:
            self.game.pl.set_hand(self.game.hit_gui())
            self.arrange(self.game.pl.get_hand(),True)
            self.ids["pl_score"].text = str(self.game.pl.score_gui())
            plmax = self.game.pl.get_sum()
            dlmax = self.game.dl.get_sum()

            if plmax >21:

                self.ids["pl_score"].text = "Bust"
                self.game.dl.set_hand(self.game.hit_gui())
                self.arrange(self.game.dl.get_hand(),False)
                self.ids["dl_score"].text = str(dlmax)
                self.scorepaint()
                self.ingameBool = False
            elif plmax  == 21:
                self.ids["pl_score"].text = "BlackJack"
                self.hit_d()
                dlmax = self.game.dl.get_sum()
                self.scorepaint()
                self.ingameBool = False

    def hit_d(self):

        plmax = self.game.pl.get_sum()
        dlmax = self.game.dl.get_sum()

        while dlmax < 17:
            if dlmax < plmax:
                self.game.dl.set_hand(self.game.hit_gui())
                self.arrange(self.game.dl.get_hand(),False)
            elif dlmax >= plmax:
                break

            dlmax = self.game.dl.get_sum()
            if dlmax == 21:
                self.ids["dl_score"].text = "BlackJack"
                break
            elif dlmax > 21:
                self.ids["dl_score"].text = "Bust"
                break
            else:
                self.ids["dl_score"].text = str(dlmax)

    def stand(self):
        if self.ingameBool == True:
            self.hit_d()
            self.scorepaint()
            self.ingameBool = False

    def deal(self):        # ボタンをクリック時
        if self.ingameBool == False:
            self.ingameBool = True
            self.game.clear()
            self.ids["wltextLabel"].source = "./img/scoreblank.png"
            self.ids["hand_num"].text = str(self.game.pl.get_tip())
            self.game.tip_bet_gui(int(self.ids["testSlider"].value))
            self.ids["hand_num"].text = str(self.game.pl.get_tip())

            self.game.pl.set_hand(self.game.hit_gui())
            self.game.pl.set_hand(self.game.hit_gui())

            self.game.dl.set_hand(self.game.hit_gui())

            self.arrange(self.game.pl.get_hand(),True)
            self.arrange(self.game.dl.get_hand(),False)

            plmax = self.game.pl.score_gui()
            dlmax = self.game.dl.score_gui()

            self.ids["dl_score"].text = str(dlmax)
            if plmax == "21":
                self.ids["pl_score"].text = "BlackJack"
                self.hit_d()
                self.scorepaint()
                self.ingameBool = False
            else:
                self.ids["pl_score"].text = str(plmax)

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'

    def build(self):

        return TextWidget()


if __name__ == '__main__':
    TestApp().run()
