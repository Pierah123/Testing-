iLikePesto = []
otherFoods = []

for i in range(8):
    food = input("What’s your favourite food? ").strip().lower()
    if food == "pesto":
        iLikePesto.append(food)
    else:
        otherFoods.append(food)

print(f"\nPesto is loved by {len(iLikePesto)} people!")

for _ in iLikePesto:
    print("I like pesto")

print("\nOther Foods:")
for food in otherFoods:
    print(food.capitalize())
