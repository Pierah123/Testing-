cerealList = []

while True:
    cereal = input("Enter Cereal: ").strip().lower()
    if cereal in ["sultana and bran", "weetbix"]:
        break
    cerealList.append(cereal.title())

print("\nCereal List:")
print(cerealList)
