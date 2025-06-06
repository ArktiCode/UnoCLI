from .deck import Deck
from .player import HumanPlayer
from .ai.easy_ai import EasyAI
from .ai.medium_ai import MediumAI
from .ai.hard_ai import HardAI
from .card import Card
import random


class UnoGame:
    def __init__(self, player_configs):
        self.players = []
        for type_, name in player_configs:
            if type_ == 'human':
                self.players.append(HumanPlayer(name))
            elif type_ == 'ai-easy':
                self.players.append(EasyAI(name, 'easy'))
            elif type_ == 'ai-medium':
                self.players.append(MediumAI(name, 'medium'))
            elif type_ == 'ai-hard':
                self.players.append(HardAI(name, 'hard'))
        self.deck = Deck()
        self.discard_pile = DiscardPile()
        self.current_player_idx = 0
        self.direction = 1
        self.setup_game()

    def play_game(self):
        """Main game loop"""
        while True:
            game_over = self.play_turn()
            if game_over:
                break

    def setup_game(self):
        '''Initializes first game state'''
        for _ in range(7):
            for player in self.players:
                player.draw(self.deck)

        while True:
            initial_card = self.deck.draw()
            if initial_card is None:
                raise ValueError("Deck is empty during setup!")
            if not initial_card.is_wild():
                break
        self.discard_pile.add_card(initial_card)

    def next_player(self):
        '''Move to next player based on game direction'''
        self.current_player_idx = (self.current_player_idx + self.direction) % len(self.players)

    def handle_wild_card(self, card, player):
        """Handle wild card color selection"""
        if isinstance(player, HumanPlayer):
            colors = ["red", "blue", "green", "yellow"]
            print("Choose a color:")
            for i, color in enumerate(colors, 1):
                print(f"{i}: {color}")
            while True:
                try:
                    choice = int(input("Enter color number (1-4): ")) - 1
                    if 0 <= choice < len(colors):
                        card.color = colors[choice]
                        print(f"Color set to {colors[choice]}")
                        break
                    print("Invalid choice. Please enter 1-4")
                except ValueError:
                    print("Please enter a number between 1-4")
        else:  # AI player
            # AI chooses the color they have most of
            color_counts = {'red': 0, 'blue': 0, 'green': 0, 'yellow': 0}
            for c in player.hand:
                if c.color in color_counts:
                    color_counts[c.color] += 1
            chosen_color = max(color_counts, key=color_counts.get)
            card.color = chosen_color
            print(f"{player.name} chose {chosen_color}")

    def handle_special_card(self, card):
        """Handles special card effects with verbose feedback"""
        if card.value == "reverse":
            if len(self.players) == 2:
                next_player = self.players[(self.current_player_idx + self.direction) % len(self.players)]
                print(f"↻ Reverse played! {next_player.name} will be skipped!")
            else:
                self.direction *= -1
                print(
                    f"⇄ Direction reversed! Now going {'counter-clockwise' if self.direction == -1 else 'clockwise'}!")

        elif card.value == "skip":
            skipped = self.players[(self.current_player_idx + self.direction) % len(self.players)]
            print(f"⏭️ {skipped.name} has been skipped!")
            self.next_player()

        elif card.value == "draw 2":
            target = self.players[(self.current_player_idx + self.direction) % len(self.players)]
            target.draw(self.deck, 2)
            print(f"‼️ {target.name} draws 2 cards and loses their turn!")
            self.next_player()

        elif card.value == "draw 4":
            target = self.players[(self.current_player_idx + self.direction) % len(self.players)]
            target.draw(self.deck, 4)
            print(f"💥 {target.name} draws 4 cards and loses their turn!")
            self.next_player()

    def show_turn_order(self, current_player):
        """Displays turn order in a clear linear format"""
        print("\n" + "=" * 40)
        print("TURN ORDER (Current → Next Players):")
        print("Direction: " + ("CLOCKWISE →" if self.direction == 1 else "← COUNTER-CLOCKWISE"))
        print("-" * 40)

        # Get players in turn order
        turn_order = []
        for i in range(len(self.players)):
            idx = (self.current_player_idx + i * self.direction) % len(self.players)
            turn_order.append(self.players[idx])

        # Display with clear indicators
        for i, player in enumerate(turn_order):
            # Current player marker
            marker = ">>> CURRENT: " if player == current_player else f"Player {i + 1}:  "

            # Color coding
            if isinstance(player, HumanPlayer):
                name = f"\033[92m{player.name}\033[0m"  # Green
            else:
                name = f"\033[91m{player.name}\033[0m"  # Red

            # Cards count
            cards = f"({len(player.hand)} cards)"

            print(f"{marker}{name.ljust(20)} {cards}")

        print("=" * 40 + "\n")

    def play_turn(self):
        '''Execute one player turn'''

        def play_turn(self):
            current = self.players[self.current_player_idx]

            # Show turn order before each turn
            self.show_turn_order(current)

        current = self.players[self.current_player_idx]
        game_state = {
            'top_card': self.discard_pile.top_card(),
            'players': self.players,
            'current_player_idx': self.current_player_idx
        }

        # Human player turn
        if isinstance(current, HumanPlayer):
            # Show game state first
            self.show_turn_order(current)
            print(f"\n{current.name}'s turn")
            print(f"\nTop card: {self.discard_pile.top_card()}")
            print("Your hand:")
            for i, card in enumerate(current.hand, 1):
                print(f"{i}: {card}")

            while True:
                action = input("Play a card (enter number) or 'draw': ").lower().strip()
                if action == "draw":
                    current.draw(self.deck)
                    self.next_player()
                    return False

                try:
                    card_idx = int(action) - 1
                    if not (0 <= card_idx < len(current.hand)):
                        print("Invalid card number!")
                        continue

                    chosen_card = current.hand[card_idx]
                    top_card = self.discard_pile.top_card()

                    if not (chosen_card.matches(top_card) or chosen_card.is_wild()):
                        print(f"Invalid play! {chosen_card} doesn't match top card's color or value!")
                        continue

                    played_card = current.play_card(card_idx, self.discard_pile)
                    print(f"You played: {played_card}")

                    if played_card.is_wild():
                        self.handle_wild_card(played_card, current)

                    self.handle_special_card(played_card)

                    if len(current.hand) == 1:  # Right after playing to 1 card
                        print(f"{current.name} shouts: UNO!")
                    elif len(current.hand) == 0:  # After playing last card
                        print(f"{current.name} wins!")
                        return True

                    self.next_player()
                    return False

                except ValueError:
                    print("Please enter a number or 'draw'")

        # AI player turn
        else:
            print(f"\n{current.name}'s turn")
            print(f"Top card: {self.discard_pile.top_card()}")

            # Show "thinking" animation
            print(f"{current.name} is thinking...", end='', flush=True)
            current._think()  # This pauses execution
            print("\r", end='')  # Clear the thinking line

            action = current.choose_action(game_state)


            if action['action'] == 'draw':
                print(f"{current.name} draws a card")
                current.draw(self.deck)
                self.next_player()
                return False

            elif action['action'] == 'play':
                card = current.hand[action['card_index']]
                played_card = current.play_card(action['card_index'], self.discard_pile)
                print(f"{current.name} plays: {played_card}")

                if played_card.is_wild():
                    self.handle_wild_card(played_card, current)

                self.handle_special_card(played_card)

                if current.has_uno():
                    print(f"{current.name} shouts: UNO!")
                if current.has_won():
                    print(f"{current.name} wins!")
                    return True

                self.next_player()
                return False
            return False


class DiscardPile:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.insert(0, card)

    def top_card(self):
        return self.cards[0] if self.cards else None

    def reshuffle_into_deck(self, deck):
        if len(self.cards) > 1:
            deck.cards.extend(self.cards[1:])
            self.cards = [self.cards[0]]
            deck.shuffle()