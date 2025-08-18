import random

# ---------------- Forest Treasure Hunt ----------------
def forest_game():
    print("\nYou are in the forest...")

    # Monkey challenge
    fruits = ["banana", "apple", "strawberry", "blueberry", "orange"]
    guessed = []
    print("A monkey blocks your way! Guess the 5 fruits.")

    while len(guessed) < len(fruits):
        guess = input("Enter a fruit: ").lower()
        if guess in fruits and guess not in guessed:
            guessed.append(guess)
            print("Correct! Fruits so far:", guessed)
        elif guess in guessed:
            print("You already guessed that one.")
        else:
            print("Wrong fruit, try again.")
    print("You passed the monkey!\n")

    # Tiger challenge
    height = int(input("Enter your height in cm: "))
    if height <= 160:
        print("Too short, you drown. Game over.")
        return
    elif height > 180:
        print("Too tall, the tiger sees you. Game over.")
        return
    else:
        print("Good height! You cross safely.\n")

    # Password door
    password = [random.randint(0, 9) for _ in range(4)]
    print("You reach a locked door. Guess the 4-digit code.")
    for attempt in range(10):
        guess = input(f"Attempt {attempt+1}/10: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Enter exactly 4 digits.")
            continue
        guess_digits = [int(d) for d in guess]
        if guess_digits == password:
            print("Correct! Door unlocked. You win!")
            return
        else:
            correct = sum(guess_digits[i] == password[i] for i in range(4))
            print(correct, "digit(s) correct.")
    print("Out of tries. Game over.")

# ---------------- Python Quiz ----------------
def quiz_game():
    print("\nWelcome to the Python Quiz!")

    questions = [
        ("Correct file extension for Python?", ["1) .pyth", "2) .py", "3) .pt", "4) .pyt"], 2),
        ("Keyword to define a function?", ["1) func", "2) define", "3) def", "4) function"], 3),
        ("Result of 3/2?", ["1) int", "2) float", "3) str", "4) bool"], 2),
        ("How to write a comment?", ["1) //", "2) #", "3) <!-- -->", "4) * *"], 2),
        ("Which is mutable?", ["1) tuple", "2) list", "3) string", "4) frozenset"], 2),
        ("len('Python') returns?", ["1) 5", "2) 6", "3) 7", "4) Error"], 2)
    ]

    score = 0
    for i, (q, opts, correct) in enumerate(questions, 1):
        print(f"\nQ{i}: {q}")
        for opt in opts:
            print(opt)
        ans = int(input("Your answer (1-4): "))
        if ans == correct:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    wrong = len(questions) - score
    percent = (score / len(questions)) * 100
    print("\nResults:")
    print("Correct:", score, "Wrong:", wrong, "Percent:", percent)

    # Different endings
    if score == 6:
        print("Excellent! 6/6")
    elif score >= 4:
        print("Good job!")
    elif score >= 2:
        print("Keep practicing.")
    else:
        print("Needs improvement.")

# ---------------- Main ----------------
def main():
    scenario = random.randint(1, 2)
    if scenario == 1:
        forest_game()
        if input("\nPlay the Python Quiz? (yes/no): ").lower() == "yes":
            quiz_game()
    else:
        quiz_game()
        if input("\nPlay the Forest Game? (yes/no): ").lower() == "yes":
            forest_game()
    print("\nThanks for playing!")

main()
