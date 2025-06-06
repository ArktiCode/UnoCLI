from .base_ai import AIPlayer
import random


class EasyAI(AIPlayer):
    """Random but legal moves"""

    def choose_action(self, game_state):
        playable = self._get_playable_cards(game_state['top_card'])

        if playable and random.random() < 0.7:  # 70% chance to play if possible
            return {
                'action': 'play',
                'card_index': random.choice(playable)
            }
        return {'action': 'draw'}