class Card:
    def __init__(self, color, value):
        '''
        Initialize a card with arguments, color and value.
        color (str): Card Color
        value (str): Card Value
        '''
        self.color = color
        self.value = value

    def __str__(self):
        '''
        String representation of the card
        Lessens the need for parsing the card value unlike in first ver. of the code.
        '''
        return f"{self.color} {self.value}"

    def __repr__(self):
        '''
        For Debugging Purposes
        '''
        return f"{self.color} {self.value}"

    def is_wild(self):
        '''
        Check if the card is considered as a wild card.
        '''
        return self.color == "wild"

    def matches(self, other_card):
        '''
        Check if this card can be played on another card (is_valid_play) logic from original code
        Returns True if card matches color/value/if wild card, otherwise False.
        '''
        return (self.color == other_card.color or
                self.value == other_card.value or
                self.is_wild())