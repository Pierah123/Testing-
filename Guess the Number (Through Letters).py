import random

def guess_letter_number():
    # Generate a random number between 1 and 26
    target_number = random.randint(1, 26)
    tries = 0
    guessed_correctly = False

    print("I'm thinking of a letter from A to Z.")
    print("Can you guess which one?")

    while not guessed_correctly:
        letter = input("Enter a letter: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter (A-Z).")
            continue

        tries += 1
        guess_number = ord(letter) - ord('a') + 1

        if guess_number == target_number:
            guessed_correctly = True
        # No hints are given, as per the example

    print(f"You guessed {tries} times.")

# Run the game
guess_letter_number()
