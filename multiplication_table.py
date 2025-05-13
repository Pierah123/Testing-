while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            break  
        else:
            print("Not a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")


print(f"\nMultiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
