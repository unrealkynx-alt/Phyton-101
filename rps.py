# import random

# def get_bot_choice():
#     choices = ["rock", "paper", "scissors"]
#     return random.choice(choices)

# def check_winner(player, bot):
#     if player == bot:
#         return "Tie!"
#     elif (player == "rock" and bot == "scissors") or \
#          (player == "paper" and bot == "rock") or \
#          (player == "scissors" and bot == "paper"):
#         return "You win!"
#     else:
#         return "Bot wins!"

# while True:
#     player = input("Rock, paper, or scissors? (or quit) ").lower()
    
#     if player == "quit":
#         break
    
#     if player not in ["rock", "paper", "scissors"]:
#         print("Invalid choice, try again")
#         continue
    
#     bot = get_bot_choice()
#     print(f"Bot chose: {bot}")
#     print(check_winner(player, bot))



# Did by myself

import random

def get_bot_choice():
    choices = ["human", "elephant", "ant"]
    return random.choice(choices)

def check_winner(player, bot):
    if player == bot:
        return "Tie!"
    if player == "human" and bot == "elephant":
        return "blud got crushed by an elephant 💀"
    elif (player == "elephant" and bot == "human") or \
         (player == "ant" and bot == "elephant") or \
         (player == "human" and bot == "ant"):
        return "Wow you actually won😎"
    else:
        return "You did NOT win 😂"

while True:
    player = input("Human, elephant, or ant? (or quit) ").lower()

    if player == "quit":
        break

    elif player not in ["human", "elephant", "ant"]:
        print(random.choice(correct_typing))
        continue

    correct_typing = [
        "BRO JUST TYPE IT CORRECTLY",
        "yo its gonna loop im lazy to make more dialogs",
        "zawg be fr"
    ]

    bot = get_bot_choice()
    print(f"Bot chose: {bot}")
    print(check_winner(player, bot))