def get_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Please enter a number!")

people = get_int("How many people are there? ")
all_langs = set()
common_langs = None

for p in range(1, people + 1):
    count = get_int(f"(To person {p}) How many languages can you speak? ")
    print("What languages can you speak in?")
    langs = {input().strip() for _ in range(count)}

    all_langs |= langs
    common_langs = langs if common_langs is None else common_langs & langs

print("\nNumber of languages everyone speaks:", len(common_langs))
if common_langs:
    print("Spoken language(s) everyone speaks:", ", ".join(sorted(common_langs)))
else:
    print("Spoken language(s) everyone speaks: None")
print("Total languages spoken in the group:", len(all_langs))
print("Languages spoken:", ", ".join(sorted(all_langs)))
