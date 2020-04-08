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
        elif dealer_score >=22:
            print("You Win")
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

    def set_card_d(self,pl_score):
        while sum(self.hand)<17:
            if sum(self.hand)<pl_score:
                self.hand.append(random.randint(1,10))
                print(self.get_hand())
                print(self.get_name() + " の得点は " + str(self.score()))

            if sum(self.hand) >= pl_score or sum(self.hand) > 22:
                break

        return self.hand


def main():
    flag = 0

    dl = Dealer()
    pl = Player()

    dl.set_card()
    pl.set_card()

    print(pl.get_hand())
    print(dl.get_hand())
    print(pl.get_name() + " の得点は " + str(pl.score()))
    print(dl.get_name() + " の得点は " + str(dl.score()))

    command = input("ディールの時は1を勝負の時は2を入力:")
    while command != "2":
        pl.set_card()

        print(pl.get_hand())
        print(pl.get_name() + " の得点は " + str(pl.score()))

        if pl.score() > 22:
            print("You Lose")
            flag = 1
            break

        if pl.score() == 21:
            print("Black Jack")
            flag = 1
            break

        command = input("ディールの時は1を勝負の時は2を入力:")

    if flag == 0:
        pl.win_lose(dl.set_card_d(pl.score()))



if __name__ == '__main__':
    main()
