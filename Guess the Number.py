import random

def guess_the_number():
    # Generate random number from 1 to 100
    number_to_guess = random.randint(1, 100)
    tries = 0
    guessed_correctly = False

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            tries += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < number_to_guess:
                print("Your guess was too low.")
            elif guess > number_to_guess:
                print("Your guess was too high.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number in {tries} tries.")
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
guess_the_number()
