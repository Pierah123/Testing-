import random

word_list = ['grain', 'apple', 'flint', 'stone', 'crane', 'drink', 'sword', 'plane']
target_word = random.choice(word_list)

def is_valid_guess(word):
    if not word.isalpha():
        print("Letters only")
        return False
    if len(word) < 5:
        print("Not enough letters")
        return False
    if len(word) > 5:
        print("Only 5-letter words")
        return False
    return True

def get_feedback(guess, target):
    feedback = []
    for i in range(5):
        if guess[i] == target[i]:
            feedback.append("🟩")
        elif guess[i] in target:
            feedback.append("🟨")
        else:
            feedback.append("⬛️")
    return "".join(feedback)

# Start of game
print("Welcome to Wordle! You have 6 chances to guess a 5-letter word.\n")

# Main game loop
for attempt in range(1, 7):
    guess = input(f"Attempt {attempt}/6: ").lower()

    while not is_valid_guess(guess):
        guess = input(f"Attempt {attempt}/6: ").lower()

    feedback = get_feedback(guess, target_word)
    print(feedback)

    if guess == target_word:
        print(f"Congratulations! You guessed '{target_word}' correctly.")
        break
else:
    print(f"Unfortunate! The word was '{target_word}'.")
