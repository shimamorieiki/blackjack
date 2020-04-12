# ここから動くことが判明したのでBJのアプリを作ってみる

import random
import gui


class Player():
    """docstring for Player."""

    def __init__(self):
        self.hand = []
        self.name = "pl"
        self.tip = 5000

    def set_hand(self,n):
        self.hand.append(n)

    def get_hand(self):
        return self.hand

    def get_name(self):
        return self.name

    def score(self):
        return sum(self.hand)

    def score_gui(self):
        score = []
        sum = 0
        sum2 = 0
        count1 = 0
        for i in range(0,len(self.hand)):

            if self.hand[i]%13 == 0 or self.hand[i]%13 >= 11:
                sum = sum + 10
                sum2 = sum2 + 10
            elif self.hand[i]%13 == 1:
                count1 = count1 + 1
            else:
                sum = sum + self.hand[i]%13
                sum2 = sum2 + self.hand[i]%13

        if count1 == 0:
            pass
        elif count1 == 1:
            sum = sum + 1
            sum2 = sum2 +11
        elif count1 == 2:
            sum = sum + 2
            sum2 = sum2 +12
        elif count1 == 3:
            sum = sum + 3
            sum2 = sum2 +13
        elif count1 == 4:
            sum = sum + 4
            sum2 = sum2 +14

        if sum == sum2:
            return str(sum)
        elif sum2 > 21:
            return str(sum)
        elif sum2 == 21:
            return str(sum2)
        elif sum2 > 0:
            return str(sum)+"/"+str(sum2)
        else:
            return str(sum)

    def get_sum(self):
        score = self.score_gui()
        if '/' in score:
            list = score.split("/")
            max = int(list[1])
        else:
            max = int(score)
        return max


    def clear(self):
        self.hand = []

    def get_tip(self):
        return self.tip

    def set_tip_add(self,n):
        self.tip = self.tip + n

    def set_tip_minus(self,n):
        self.tip = self.tip - n


class Dealer(Player):
    """docstring for Dealer."""

    def __init__(self):
        super()
        self.hand = []
        self.name = "dealer"

    def hit_d(self,pl_score):
        while sum(self.hand)<17:
            if sum(self.hand)<pl_score:
                set_hand()
                print(self.get_hand())
                print(self.get_name() + " の得点は " + str(self.score()))

            if sum(self.hand) >= pl_score or sum(self.hand) > 22:
                break

        return self.hand




class Game():
    """docstring for Game"""

    def __init__(self):
        c = list(range(1,53))
        random.shuffle(c)
        self.card =  c
        print(self.card)
        self.dl = Dealer()
        self.pl = Player()
        self.bet = 100

    def get_bet(self):
        return self.bet

    def set_bet(self,n):
        self.bet = n

    def hit(self):
        #ここまではどうにかしてトランプの情報が残ってるからうまく画像に反映させたい
        if len(self.card) >= 10:
            return self.card.pop(0)%13+1
        else:
            print("残りカードが少なくなってきた")
            print(self.card)
            c = list(range(52))
            random.shuffle(c)
            self.card.extend(c)
            print("カードを追加しました")
            print(self.card)
            return self.card.pop(0)%13+1

    def hit_gui(self):
        #ここまではどうにかしてトランプの情報が残ってるからうまく画像に反映させたい
        if len(self.card) >= 10:
            return self.card.pop(0)
        else:
            print("残りカードが少なくなってきた")
            print(self.card)
            c = list(range(1,52))
            random.shuffle(c)
            self.card.extend(c)
            print("カードを追加しました")
            print(self.card)
            return self.card.pop(0)


    def win_lose(self):
        score = sum(self.pl.get_hand())
        dealer_score = sum(self.dl.get_hand())

        if dealer_score >=22:
            print("Dealer Bust")

        if score > 21 and dealer_score > 21:
            print("You Lose1")

        elif score < 22 and dealer_score > 21:
            print("You Win11")
            self.pl.set_tip_add(self.get_bet()*2)
        elif score < 22 and score > dealer_score:
            print("You Win2")
            self.pl.set_tip_add(self.get_bet()*2)
        elif score == dealer_score:
            print("Draw3")
            self.pl.set_tip_add(self.get_bet())
        else:
            print("You Lose4")

    def win_lose_gui(self,s,ds):
        score = s
        dealer_score = ds

        if dealer_score >=22:
            return 1

        if score > 21 and dealer_score > 21:
            return 2

        elif score < 22 and dealer_score > 21:
            return 1
            self.pl.set_tip_add(self.get_bet()*2)
        elif score < 22 and score > dealer_score:
            return 1
            self.pl.set_tip_add(self.get_bet()*2)
        elif score == dealer_score:
            return 3
            self.pl.set_tip_add(self.get_bet())
        else:
            return 2


    def clear(self):
        self.pl.clear()
        self.dl.clear()

    def tip_bet(self):
        if x == None:
            self.set_bet(100)
            self.pl.set_tip_minus(100)
        elif abs(int(x)) < self.pl.get_tip():
            self.set_bet(abs(int(x)))
            self.pl.set_tip_minus(abs(int(x)))
        else:
            print("現在の最大額 "+ str(self.pl.get_tip()) +" をベットします")
            self.set_bet(self.pl.get_tip())
            self.pl.set_tip_minus(self.pl.get_tip())


    def tip_bet_gui(self,n):
        # if x == None:
        #     self.set_bet(100)
        #     self.pl.set_tip_minus(100)
        # el
        if n < self.pl.get_tip():
            self.set_bet(n)
            self.pl.set_tip_minus(n)
        else:
            print("現在の最大額 "+ str(self.pl.get_tip()) +" をベットします")
            self.set_bet(self.pl.get_tip())
            self.pl.set_tip_minus(self.pl.get_tip())

    def deal(self):

        print("Tip:"+ str(self.pl.get_tip()))
        self.tip_bet()
        print("Tip:"+ str(self.pl.get_tip()))

        self.pl.set_hand(self.hit())
        self.dl.set_hand(self.hit())

        print(self.pl.get_hand())
        print(self.dl.get_hand())

        print(self.pl.get_name() + " の得点は " + str(self.pl.score()))
        print(self.dl.get_name() + " の得点は " + str(self.dl.score()))

        command = input("hit:1 stand:2 => ")
        while command != "2":
            self.pl.set_hand(self.hit())

            print(self.pl.get_hand())
            print(self.pl.get_name() + " の得点は " + str(self.pl.score()))

            if self.pl.score() > 21:
                print("Bust5")
                break

            if self.pl.score() == 21:
                print("Black Jack6")
                break

            command = input("ディールの時は1を勝負の時は2を入力:")

        #ここまでで一応プレイヤー側の操作は全て終わってる
        #こっからは全てディーラーの処理
        while sum(self.dl.get_hand())<17:
            if sum(self.dl.get_hand())<sum(self.pl.get_hand()):
                self.dl.set_hand(self.hit())
                print(self.dl.get_hand())
                print(self.dl.get_name() + " の得点は " + str(self.dl.score()))

            if sum(self.dl.hand) >= sum(self.pl.get_hand()) or sum(self.dl.hand) > 22:
                break

        self.win_lose()
        print("Tip:"+ str(self.pl.get_tip()))


def main():
    g = Game()
    while True:
        g.deal()
        x = input("まだやりますか y/n")
        if x =="n":
            break
        elif x =="y":
            pass
        else:
            print("続ける")
        g.clear()


if __name__ == '__main__':
    # main()
    gui.TestApp().run()
