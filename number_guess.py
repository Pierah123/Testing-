import random  # Import random module for number generation

# Show welcome message
def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible (you will have 10 guesses!)")
    print("--------------------------------------------------")

# Show exit message
def exit_message():
    print("Thanks for playing the Number Guessing Game! Goodbye! ")

# Game round logic
def play_game():
    number = random.randint(1, 100)
    max_guesses = 10
    guesses = []

    for attempt in range(1, max_guesses + 1):
        try:
            guess_input = input(f"Guess #{attempt}: ")
            guess = int(guess_input)

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")  # Outcome 4
                continue

        except ValueError:
            print("Please enter a valid number.")  # Outcome 3
            continue

        guesses.append(guess)

        if guess == number:
            print(f" Correct! You guessed the number in {len(guesses)} tries.")
            break

        if len(guesses) > 1:
            prev_distance = abs(guesses[-2] - number)
            curr_distance = abs(guess - number)
            if curr_distance < prev_distance:
                print("Warmer!")  # Outcome 1
            else:
                print("Colder!")  # Outcome 2

    else:
        print(f" Sorry! You ran out of guesses. The number was {number}.")

    print("\nYour guesses were:", guesses)
    print(f"Number of guesses: {len(guesses)}")
    print("--------------------------------------------------")

# Main program loop
def main():
    while True:
        welcome_message()
        play_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            break
    exit_message()

# Start the program
main()


