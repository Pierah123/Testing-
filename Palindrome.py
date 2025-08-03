def can_form_palindrome(s: str) -> str:
    from collections import Counter
    
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    
    if len(s) % 2 == 0:
        return "Possible" if odd_count == 0 else "Not possible"
    else:
        return "Possible" if odd_count == 1 else "Not possible"

# Loop to ask user input multiple times
while True:
    user_input = input("Enter a string (or type 'quit' to stop): ")
    if user_input.lower() == 'quit':
        break
    result = can_form_palindrome(user_input)
    print(result)
