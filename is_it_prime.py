
x = int(input("Enter an integer: "))

if x < 2:
    print("Your number is not a prime number.")
else:
    found = False

    for i in range(2, x):
        
        if x % i == 0:
            found = True  

   
    if found:
        print("That is not a prime number.")
    else:
        print("That is a prime number.")
