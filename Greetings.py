name= input("Enter name:")
time= input("Enter time in 24 hour format, e.g: 14:52:")

hour = int(time.split(":")[0])

if 0 <= hour <= 12:
    greeting = "Good morning"
elif 13 <= hour <= 17:
    greeting = "Good afternoon"
elif 18 <= hour <= 23:
    greeting = "Good evening"
else:
    greeting = "Invalid time"


if greeting == "Invalid time":
    print("Please enter a valid time between 00:00 and 23:59.")
else:
    print(f"{greeting}, {name}!")
