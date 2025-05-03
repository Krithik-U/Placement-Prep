import random

while True:
    user_choice = input("Roll the dice? (y/n): ").lower()

    if user_choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'You rolled {die1} and {die2}')
    elif user_choice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")