SPADE = 1
HEART = 2
CLUB = 3
DIAMOND = 4
JOKER = 5


class Card:
    def __init__(self, value, kind):
        self.value = value
        self.kind = {
            SPADE: '♠',
            HEART: '♥',
            CLUB: '♣',
            DIAMOND: '♦',
            JOKER: 'J'
         }.get(kind, '?')
        self.text = {
            1 : 'A',
            11: 'J',
            12: 'Q',
            13: 'K',
            14: 'Q',  # 小王
            15: 'Q'   # 大王
        }.get(value, value)
        
        # 设置颜色前缀，红心和方片为红色，Joker也设为红色
        self.color_prefix = '\033[91m' if self.kind in ['♥', '♦'] or self.value == 15 else '\033[0m'
        self.covered = True
    
    def row(self, row_idx):
        if row_idx == 0 or row_idx == 3:
            return ' +----+'
        if self.covered:
            return ' |⣿⣿⣿⣿|'
        else:
            if row_idx == 1:
                return f' | {self.color_prefix}{self.kind} \033[0m |'
            if row_idx == 2:
                return f' | {self.color_prefix}{self.text:>2} \033[0m|'
        
    def flip(self):
        self.covered = not self.covered
    
    def print(self):
        for i in range(4):
            print(self.row(i))

if __name__ == '__main__':
    card = Card(10, HEART)  # 创建一张大王的牌
    card.flip()
    card.print()
    card = Card(9, HEART)  # 创建一张大王的牌
    card.flip()
    card.print()