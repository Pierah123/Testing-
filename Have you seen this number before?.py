numbers = [1, 3, 8, 35, 4, 2, 3]

for i in range(len(numbers) - 1):
    next_num = numbers[i + 1]
    if next_num in numbers[:i + 1]:
        print("YES")
    else:
        print("NO")
