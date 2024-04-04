students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
 # split separates components of a file based on provided arguments

for student in sorted(students):
    print(student)