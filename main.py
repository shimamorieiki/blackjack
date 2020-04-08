# ここから動くことが判明したのでBJのアプリを作ってみる

import random



class Player():
    """docstring for Player."""

    def __init__(self):
        self.hand = []
        self.name = "pl"

    def hit(self):
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

        if dealer_score >=22:
            print("Dealer Bust")

        if score > 21 and dealer_score > 21:
            print("You Lose")


        if score > dealer_score:
            print("You Win")
        elif score == dealer_score:
            print("Draw")
        else:
            print("You Lose")


class Dealer(Player):
    """docstring for Dealer."""

    def __init__(self):
        super()
        self.hand = []
        self.name = "dealer"

    def hit_d(self,pl_score):
        while sum(self.hand)<17:
            if sum(self.hand)<pl_score:
                self.hand.append(random.randint(1,10))
                print(self.get_hand())
                print(self.get_name() + " の得点は " + str(self.score()))

            if sum(self.hand) >= pl_score or sum(self.hand) > 22:
                break

        return self.hand

class Game():
    """docstring forGame."""



    def __init__(self):
        card = list(range(52))
        self.card =  random.shuffle(card)
        print(self.card)

    def hit(self):
        self.hand.append(random.randint(1,10))

    def play(self):

        flag = 0

        dl = Dealer()
        pl = Player()

        dl.hit()
        pl.hit()

        print(pl.get_hand())
        print(dl.get_hand())
        print(pl.get_name() + " の得点は " + str(pl.score()))
        print(dl.get_name() + " の得点は " + str(dl.score()))

        command = input("hit:1 stand:2 => ")
        while command != "2":
            pl.hit()

            print(pl.get_hand())
            print(pl.get_name() + " の得点は " + str(pl.score()))

            if pl.score() > 21:
                print("Bust")
                break

            if pl.score() == 21:
                print("Black Jack")
                break

            command = input("ディールの時は1を勝負の時は2を入力:")

        pl.win_lose(dl.hit_d(pl.score()))




def main():
    # g = Game()
    # g.play()
    card = list(range(52))
    random.shuffle(card)
    print(card)


if __name__ == '__main__':
    main()
