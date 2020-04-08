# ここから動くことが判明したのでBJのアプリを作ってみる

import random

class Dealer():
    """docstring for ."""

    def __init__(self):
        self.hand = []

    def add_card(self):
        self.hand.append(random.randint(1,13))

    def show_cards(self):
        print(self.hand)

class Player():
    """docstring forPlayer."""

    def __init__(self):
        self.hand = []

    def add_card(self):
        self.hand.append(random.randint(1,13))

    def show_cards(self):
        print(self.hand)

def main():
    dl = Dealer()
    pl = Player()
    dl.show_cards()
    dl.add_card()
    pl.add_card()
    dl.show_cards()
    pl.show_cards()
    

if __name__ == '__main__':
    main()
