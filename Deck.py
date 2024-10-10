from Card import *
import random
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(1, 14):
            self.cards.append(Card(i, SPADE))
            self.cards.append(Card(i, HEART))
            self.cards.append(Card(i, CLUB))
            self.cards.append(Card(i, DIAMOND))
        self.cards.append(Card(15, JOKER))
        self.cards.append(Card(15, JOKER))
    
    def shuffle(self):
        random.shuffle(self.cards)

    @property
    def is_empty(self):
        return len(self.cards) == 0
    def draw(self):
        if self.is_empty:
            print('Deck is empty')
            return None
        return self.cards.pop()


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    for card in deck.cards:
        card.flip()
        card.print()