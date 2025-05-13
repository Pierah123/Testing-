attempts = 0  

while attempts < 3:
    password = input("Enter Password: ")
    if password == "ABC":
        print("Correct Password")
        break
    else:
        print("Incorrect Password")
        attempts += 1

if attempts == 3:
    print("You are now locked.")
