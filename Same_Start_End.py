stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]

count = 0

for word in stringsList:
    if word[0].lower() == word[-1].lower():
        count += 1

print("Number of strings with the same start and end:", count)
