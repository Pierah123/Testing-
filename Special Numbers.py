a = [18, 2, 90, 3, 5]
b = [2, 86, 42, 5, 7]

for n in sorted(set(a) & set(b)):
    print(n)
