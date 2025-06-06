from .card import Card
from abc import ABC, abstractmethod

class Player(ABC):
    """Base player class that can be human or AI"""

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, count=1):
        """Draw cards from deck"""
        cards = deck.draw(count)
        if isinstance(cards, list):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)
        return cards

    def play_card(self, index, discard_pile):
        """Play a card from hand to discard pile"""
        card = self.hand.pop(index)
        discard_pile.add_card(card)
        return card

    def has_uno(self):
        """Check if player has UNO (one card left)"""
        return len(self.hand) == 1

    def has_won(self):
        """Check if player has won (no cards left)"""
        return len(self.hand) == 0

    def show_hand(self):
        """Return string representation of hand"""
        return "\n".join(f"{i}: {card}" for i, card in enumerate(self.hand))

    @abstractmethod
    def choose_action(self, game_state):
        """Determine what action to take"""
        pass


class HumanPlayer(Player):
    """Human player that makes decisions via input"""

    def choose_action(self, game_state):
        print(f"\n{self.name}'s turn")
        print(f"Top card: {game_state['top_card']}")
        print("Your cards:")
        print(self.show_hand())

        while True:
            action = input("Play a card (enter number) or 'draw': ").lower().strip()
            if action == "draw":
                return {'action': 'draw'}
            try:
                card_idx = int(action)
                if 0 <= card_idx < len(self.hand):
                    return {'action': 'play', 'card_index': card_idx}
                print("Invalid card number!")
            except ValueError:
                print("Please enter a number or 'draw'")