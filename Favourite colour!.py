from collections import Counter

votes = []

print("Enter each classmate's favorite colour one at a time.")
print("When you're done, just press Enter with no input.\n")

while True:
    colour = input("Favourite colour: ").strip()
    if colour == "":
        break
    votes.append(colour)

if not votes:
    print("No votes entered.")
else:
    tally = Counter(votes)
    max_votes = max(tally.values())
    favourites = [colour for colour, count in tally.items() if count == max_votes]

    if len(favourites) == 1:
        print(f"\nThe class's favorite colour is {favourites[0]}!")
    else:
        colours = ", ".join(favourites)
        print(f"\nThe class's favorite colours are {colours}!")
