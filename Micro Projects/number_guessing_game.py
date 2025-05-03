import random

comp_guess = random.randint(1, 100)

while True:
    try:
        user_guess = int(input("Guess the number between 1 and 100: "))

        if user_guess > comp_guess:
            print("Too High!")
        elif user_guess < comp_guess:
            print("Too Low!")
        else:
            print("Congratulations! You guessed the number")
            break

    except ValueError:
        print("Please enter a valid number")
