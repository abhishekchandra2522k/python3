# using while loop and for loop

print("Use 'e' to exit input stream")
section = []
sum = 0

while True:
    grade = input (" - ")
    if grade == "e":
        break
    else :
        grade = float(grade)
        section.append(grade)

for grade in section:
    sum = sum + grade
average = sum / len(section)
print("sum : ", sum)
print("average : ", average)