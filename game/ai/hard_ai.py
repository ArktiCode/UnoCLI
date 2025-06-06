from .base_ai import AIPlayer


class HardAI(AIPlayer):
    """Strategic AI that considers multiple factors"""

    def choose_action(self, game_state):
        playable = self._get_playable_cards(game_state['top_card'])

        if not playable:
            return {'action': 'draw'}

        # Strategy: prioritize by danger level and hand reduction
        scored_plays = []
        for idx in playable:
            card = self.hand[idx]
            score = 0

            # High score for cards that reduce hand size quickly
            if card.value in ('draw 2', 'draw 4', 'skip'):
                score += 3
            elif card.value == 'reverse' and len(game_state['players']) > 2:
                score += 2

            # Prefer playing wild cards when we have many options
            if card.is_wild():
                color_options = sum(
                    1 for c in self.hand
                    if c.color != 'wild' and c.color != card.color
                )
                score += min(2, color_options / 2)

            scored_plays.append((score, idx))

        # Play highest scoring option
        scored_plays.sort(reverse=True)
        return {
            'action': 'play',
            'card_index': scored_plays[0][1]
        }