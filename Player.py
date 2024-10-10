from Card import *
from Deck import *

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.cards = []
        self.score = 0
        self.deck = deck
    
    def draw(self):
        if self.deck.is_empty:
            print('Deck is empty')
            return None
        card = self.deck.draw()
        card.flip()
        self.cards.append(card)
        self.cards.sort(key=lambda x: -x.value)
    
    def show_cards(self):
        for i in range(4):
            print(''.join([card.row(i) for card in self.cards]))

if __name__ == '__main__':
    import time
    from utils import *

    deck = Deck()
    deck.shuffle()
    player = Player('Player1', deck)
    for i in range(13):
        player.draw()
        clear_console()
        player.show_cards()
        time.sleep(0.3)