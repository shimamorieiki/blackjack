# ここから動くことが判明したのでBJのアプリを作ってみる

import random



class Player():
    """docstring for Player."""

    def __init__(self):
        self.hand = []
        self.name = "pl"

    def set_card(self):
        self.hand.append(random.randint(1,10))

    def get_hand(self):
        return self.hand

    def get_name(self):
        return self.name

    def score(self):
        return sum(self.hand)

    def win_lose(self,dealer_hand):
        score = sum(self.hand)
        dealer_score = sum(dealer_hand)
        if score >= 22:
            print("You Lose")
        if score == 21:
            print("Black Jack")
        elif score > dealer_score:
            print("You Win")
        else:
            print("You Lose")


class Dealer(Player):
    """docstring for Dealer."""

    def __init__(self):
        super()
        self.hand = []
        self.name = "dealer"


def main():
    flag = 0

    dl = Dealer()
    pl = Player()

    dl.set_card()
    pl.set_card()

    print(dl.get_hand())
    print(pl.get_hand())
    print(dl.get_name() + " の得点は " + str(dl.score()))
    print(pl.get_name() + " の得点は " + str(pl.score()))

    command = input("ディールの時は1を勝負の時は2を入力:")
    while command != "2":
        dl.set_card()
        pl.set_card()

        print(pl.get_hand())
        print(dl.get_hand())
        print(pl.get_name() + " の得点は " + str(pl.score()))
        print(dl.get_name() + " の得点は " + str(dl.score()))

        if pl.score() > 22:
            print("You Lose")
            flag = 1
            break

        command = input("ディールの時は1を勝負の時は2を入力:")

    if flag == 0:
        pl.win_lose(dl.get_hand())



if __name__ == '__main__':
    main()
