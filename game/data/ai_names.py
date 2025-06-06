import random

NAME_LISTS = {
    'easy': [
        # Yu-Gi-Oh! beginners
        "Joey Wheeler", "Téa Gardner", "Tristan Taylor",
        # MTG newbies
        "Timmy Power", "Johnny Combo", "Spike Junior",
        # Pokémon TCG
        "Ash Ketchum", "Misty", "Brock",
        # General
        "Card Apprentice", "Deck Builder", "Mulligan Master"
    ],
    'medium': [
        # Yu-Gi-Oh! duelists
        "Seto Kaiba", "Mai Valentine", "Weevil Underwood",
        # MTG pros
        "Luis Scott-Vargas", "Paulo Vitor Damo da Rosa", "Reid Duke",
        # Poker players
        "Daniel Negreanu", "Phil Ivey", "Doyle Brunson",
        # General
        "The Gambler", "Bluff King", "Tactician"
    ],
    'hard': [
        # Yu-Gi-Oh! legends
        "Yugi Muto", "Atem", "Maximillion Pegasus",
        # MTG Hall of Famers
        "Kai Budde", "Jon Finkel", "Shahar Shenhar",
        # World Champions
        "Ondřej Stráský", "Javier Dominguez", "Eli Kassis",
        # Final Bosses
        "The Shadow Player", "Cardistry God", "Grand Archduke"
    ]
}

_used_names = set()


def get_ai_name(difficulty):
    """Returns unique random name for AI"""
    available = [n for n in NAME_LISTS[difficulty]
                 if n not in _used_names]

    if not available:
        available = NAME_LISTS[difficulty]
        _used_names.clear()

    name = random.choice(available)
    _used_names.add(name)
    return name