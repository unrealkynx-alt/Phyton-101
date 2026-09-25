import random


def get_bot_choice():
    choices = ["human", "elephant", "ant"]
    return random.choice(choices)


def check_winner(player, bot):
    if player == bot:
        return "Tie!"

    winning_moves = {
        "human": "ant",
        "ant": "elephant",
        "elephant": "human",
    }

    if winning_moves[player] == bot:
        return "Wow you actually won 😎"

    return "You did NOT win 😂"


stats = {
    "wins": 0,
    "loses": 0,
    "draws": 0,
}

while True:
    player = input("Human, elephant, or ant? (or quit) ").lower()

    if player == "quit":
        break

    if player not in ["human", "elephant", "ant"]:
        messages = [
            "BRO JUST TYPE IT CORRECTLY",
            "yo its gonna loop im lazy to make more dialogs",
            "zawg be fr",
        ]
        print(random.choice(messages))
        continue

    bot = get_bot_choice()
    print(f"Bot chose: {bot}")

    result = check_winner(player, bot)
    print(result)

    if result == "Tie!":
        stats["draws"] += 1
    elif result == "Wow you actually won 😎":
        stats["wins"] += 1
    else:
        stats["loses"] += 1

    print(stats)