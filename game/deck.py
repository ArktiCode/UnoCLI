import random
from .card import Card

class Deck:
    '''Deck of uno Cards for drawing and shuffling'''

    def __init__(self):
        '''Initialize the Uno Deck'''
        self.cards = []
        self.create_standard_deck()
        self.shuffle()

    def create_standard_deck(self):
        '''Create a standard Uno deck with 108 cards (Color[4x] 0-9, + reverse, skip, draw 2, and 4 each Wild Card, Wild Draw 4)'''
        colors = ["red", "blue", "green", "yellow"]
        numbers = [str(i) for i in range(10)] # Starts from number 0 - 9
        actions = ["reverse", "skip", "draw 2"]

        for color in colors:
            self.cards.append(Card(color, "0")) #One 0 card per color

            for num in numbers[1:]:
                self.cards.append(Card(color,num))
                self.cards.append(Card(color,num)) #two append syntax so the card numbers will be multiplied by 2

            for action in actions:
                self.cards.append(Card(color,action))
                self.cards.append(Card(color,action)) #same reasoning above, two append syntax for special color cards

        for _ in range(4):
            self.cards.append(Card("wild", "card"))
            self.cards.append(Card("wild", "draw 4"))

    def shuffle(self):
        random.shuffle(self.cards) #typical card shuffle using random

    def draw(self, count=1):
        '''Draw one or more cards from the deck
        count is an integer that determines the number of cards to be drawn
        returns list[card] or Card if list count >1, single card if count = 1
        '''
        if count == 1:
            return self.cards.pop() if self.cards else None

        drawn = []

        for _ in range (min(count, len(self.cards))):
            drawn.append(self.cards.pop())
        return drawn

    def __len__(self):
        '''Return the number of cards remaining in the deck'''
        return len(self.cards)