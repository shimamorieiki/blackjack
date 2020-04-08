# ここから動くことが判明したのでBJのアプリを作ってみる

import random


class Dealer():
    """docstring for ."""

    def __init__(self):
        self.hand = [0,0]

class Player():
    """docstring forPlayer."""

    def __init__(self):
        self.hand = [1,1]


def deal():#で札を配る
    return random.randint(1,13)

def main():
    dl = Dealer()
    pl = Player()
    print(dl.hand)
    print(pl.hand)

if __name__ == '__main__':
    main()
