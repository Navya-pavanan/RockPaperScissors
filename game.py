import random

# Choices and their emojis
choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
    "lizard": "🦎",
    "spock": "🖖"
}

# Rules dictionary
rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

print("🎮 Rock Paper Scissors Lizard Spock 🎮")
print("Choices:", ", ".join([f"{c} {choices[c]}" for c in choices]))

player_choice = input("Enter your choice: ").lower()
while player_choice not in choices:
    player_choice = input("Invalid choice! Try again: ").lower()

computer_choice = random.choice(list(choices.keys()))

print(f"\nYou chose: {choices[player_choice]} ({player_choice})")
print(f"Computer chose: {choices[computer_choice]} ({computer_choice})")

# Decide winner
if player_choice == computer_choice:
    print("🤝 It's a tie!")
elif computer_choice in rules[player_choice]:
    print("🎉 You win!")
else:
    print("💻 Computer wins!")
