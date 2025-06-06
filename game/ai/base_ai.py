from game.player import Player
import time
import random


class AIPlayer(Player):
    """Base class for AI players"""

    def __init__(self, name, difficulty):
        super().__init__(f"AI {name} ({difficulty})")
        self.difficulty = difficulty
        self.think_time = {
            'easy': (2, 3),  # Between 2-3 seconds
            'medium': (1, 2),
            'hard': (0.5, 1.5)
        }

    def _think(self, complexity_factor=1.0, is_special=False):
        """Simulates thinking time with optional modifiers"""
        min_t, max_t = self.think_time[self.difficulty]

        # Apply complexity factor
        base_delay = random.uniform(min_t, max_t) * complexity_factor

        # Add extra pause for special cards
        if is_special:
            base_delay += 1.0

        end_time = time.time() + base_delay

        while time.time() < end_time:
            print(".", end='', flush=True)
            time.sleep(0.5)

        print("\r", end='')

    def choose_action(self, game_state):
        """AI decision-making logic"""
        top_card = game_state['top_card']
        playable = self._get_playable_cards(top_card)

        # Calculate complexity factor
        complexity = 1.0
        if len(playable) > 3:
            complexity = 1.5

        # Check if we might play a special card
        is_special = any(
            self.hand[i].value in ["draw 2", "draw 4", "skip", "reverse"]
            for i in playable
        )

        self._think(complexity_factor=complexity, is_special=is_special)

        # Rest of your choose_action implementation...
        raise NotImplementedError("Subclasses must implement choose_action")

    def _get_playable_cards(self, top_card):
        """Helper method to find playable cards"""
        return [i for i, card in enumerate(self.hand)
                if card.matches(top_card)]