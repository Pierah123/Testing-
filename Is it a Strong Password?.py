import string

def check_password_strength():
    password = input("Enter your password: ")
    score = 0

    # Check each condition
    if len(password) > 7:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    # Determine strength
    if score == 5:
        strength = "strong"
    elif score >= 3:
        strength = "moderately strong"
    else:
        strength = "weak"

    print(f"Your password is {strength} (Score: {score}/5)")

# Run the function
check_password_strength()
