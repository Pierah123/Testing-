attendance = {}

print("Enter student names and whether they are Present or Absent.")
print("Type 'done' when you have finished entering all names.\n")

while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name == "done":
        break

    status = input("Is " + name + " Present or Absent? ")
    # Make sure input is either Present or Absent
    while status != "Present" and status != "Absent":
        status = input("Please type 'Present' or 'Absent' only: ")

    # Store True if Present, False if Absent
    if status == "Present":
        attendance[name] = True
    else:
        attendance[name] = False

print("\nStudents who are present:")
for student in attendance:
    if attendance[student] == True:
        print(student + " is Present")
