from .base_ai import AIPlayer
import random


class MediumAI(AIPlayer):
    """Prioritizes playing cards, prefers special cards"""

    def choose_action(self, game_state):
        playable = self._get_playable_cards(game_state['top_card'])

        if playable:
            # Prefer special cards (reverse, skip, draw)
            special_cards = [
                i for i in playable
                if self.hand[i].value in ('reverse', 'skip', 'draw 2', 'draw 4')
            ]

            return {
                'action': 'play',
                'card_index': random.choice(special_cards) if special_cards
                else random.choice(playable)
            }
        return {'action': 'draw'}