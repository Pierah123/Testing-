def triangleTest(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] + sides[1] > sides[2]

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))


if triangleTest(a, b, c):
    print("Yes, it is a triangle!")
else:
    print("No, it is not a triangle.")
