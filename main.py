from game.game import UnoGame
from game.data.ai_names import get_ai_name


def main():
    print("Welcome to Uno! (1 Human vs AI)")

    # Get human player name
    human_name = input("Enter your name: ").strip()
    while not human_name.strip():
        human_name = input("Name cannot be empty! Enter your name: ")

    # AI opponent selection
    print("\nSelect AI opponents:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    # Get AI count (1-3)
    ai_count = 0
    while ai_count < 1 or ai_count > 3:
        try:
            ai_count = int(input("How many AI opponents? (1-3): "))
        except ValueError:
            print("Please enter a number 1-3")

    # Get difficulty (1-3)
    ai_level = ""
    while ai_level not in ["1", "2", "3"]:
        ai_level = input("Select AI difficulty (1-3): ")

    # Create player configs - ONLY ONCE
    player_configs = [("human", human_name)]
    ai_level_name = ["easy", "medium", "hard"][int(ai_level) - 1]

    for i in range(ai_count):
        ai_name = get_ai_name(ai_level_name)  # Get random name
        player_configs.append((f"ai-{ai_level_name}", ai_name))

    # Start game
    game = UnoGame(player_configs)
    game.play_game()


if __name__ == "__main__":
    main()