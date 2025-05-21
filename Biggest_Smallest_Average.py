numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]

biggest = max(numsList)
smallest = min(numsList)
average = sum(numsList) / len(numsList)

print("Biggest number:", biggest, "at position", numsList.index(biggest))
print("Smallest number:", smallest, "at position", numsList.index(smallest))
print("Average:", average)
