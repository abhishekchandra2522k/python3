# Detailed Version

grades = []

while True:
    print(" ")
    print('Enter your choice :')
    print('1. Enter Grades')
    print('2. Delete grades')
    print('3. See all grades')
    print('4. Calculate Average')
    print('5. Exit')
    
    choice = input()
    
    if not (len(choice) == 1 or choice.isnumeric()):
        print("Enter a valid choice")
        continue
     
    if int(choice) == 6:
        break
    
    if int(choice) == 1:
        print("Enter grades: (use 'e' to exit input stream)")
        while True:
            grade = (input())
            if grade == 'e':
                break
            grade = float(grade)
            grades.append(grade)
    if int(choice) == 5:
        sum = 0
        if grades == []:
            print("First enter grades in choice 1")
            continue
        for grade in grades:
            sum = sum + grade
        average = sum / len(grades)
        print("Average is :",average)
        
    if int(choice) == 2:
        grades.delete(int(input()))
    if int(choice) == 3:
        print(grades)