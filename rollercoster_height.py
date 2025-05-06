try:
    x = input("What's your height (in cm): ")
    
    if x.isalpha():
        print("Type height in numbers.")
    else:
        x = int(x)
        if x > 120:
            print("You can ride the roller coaster!")
        else:
            print("Sorry, you can't ride the roller coaster.")
except:
    print("Buddy, you need to enter a number only.")
