import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK:'🪨', PAPER:'📃', SCISSORS:'✂️'}
choice = tuple(emojis.keys())

while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    comp_choice = random.choice(choice)

    if user_choice not in choice:
        print("Invalid choice!")
        continue

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[comp_choice]}')

    if user_choice == comp_choice:
        print("Match Draw!")
        continue
    elif ((user_choice == ROCK and comp_choice == SCISSORS) or
          (user_choice == PAPER and comp_choice == ROCK) or
          (user_choice == SCISSORS and comp_choice == PAPER)):
        print("You Win!")
    else:
        print("You Lose!")

    next_game = input("Continue? (y/n): ").lower()
    if next_game == 'n':
        break