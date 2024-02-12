import random
import time

face_value = {
    'A': 1,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
}
colour_value = {
    'S': 3,
    'H': 2,
    'D': 1,
    'C': 0
}
def update_table(card_at_hand):
    if card_at_hand[1] == 7:
        table[card_at_hand[0]] = [7]
    elif card_at_hand[1] < table[card_at_hand[0]][0]:
        table[card_at_hand[0]] = [card_at_hand[1]] + table[card_at_hand[0]]
    else:
        table[card_at_hand[0]] += [card_at_hand[1]]
    print(table)

def update_available_move(card_at_hand):
    if card_at_hand[1] == 7:
        available_move[card_at_hand[0]] = [6,8]
    elif card_at_hand[1] < 7:
        available_move[card_at_hand[0]][0] -= 1
    else:
        available_move[card_at_hand[0]][1] += 1
    print(available_move)


class Card:
    face: str
    colour: str
    value: int

    def __init__(self, colour: str, num: str) -> None:
        self.face = num 
        self.colour = colour
        self.colour_value = colour_value[colour]
        self.value = face_value.get(num)
        if self.value is None:
            self.value = int(num)

    def __lt__(self, other):
        return self.value < other.value if self.colour == other.colour else self.colour_value > other.colour_value

    def __gt__(self, other):
        return self.value > other.value if self.colour == other.colour else self.colour_value < other.colour_value

    def __str__(self) -> str:
        return f'{self.colour}/{self.face}'
    
    def __repr__(self) -> str:
        return f'{self.colour}/{self.face}'

class Player:
    deck: list

    def __init__(self, deck) -> None:
        self.deck = deck

    def play_card(self, targat_card):
        for card in self.deck:
            if targat_card == str(card):
                self.deck.remove(card)
                return
    
    def search_in_deck(self, available_move):
        for suit,nums in available_move.items():
            for num in nums:
                for card in self.deck:
                    if card.colour == suit and card.value == num:
                        return (suit,num)
    
    def take_turn(self):
        card_at_hand = self.search_in_deck(available_move)
        player2.play_card(f'{card_at_hand[0]}/{card_at_hand[1]}')
        update_table(card_at_hand)
        update_available_move(card_at_hand)
        print()


num = 'A23456789TJQK'
colour = 'SHDC'

deck = [Card(num=n, colour=c) for c in colour for n in num]
shuffled = deck.copy()
random.seed(0)
random.shuffle(shuffled)
deck1 = shuffled[:26]
deck2 = shuffled[26:]
deck1.sort()
deck2.sort()

if any('S/7' == str(card) for card in deck1):
    player1 = Player(deck1)
    player2 = Player(deck2)
else:
    player1 = Player(deck2)
    player2 = Player(deck1)

player1.play_card('S/7')
table = {'S': [7], 'H': [], 'D': [], 'C': []}
available_move = {'S': [6,8], 'H': [7], 'D': [7], 'C': [7]}

player2.take_turn()


while player2:
    player1.take_turn()
    player2.take_turn()
    # ip = input('next round?')
    # if ip == '':
    #     continue
    # elif ip == 'q':
    #     break