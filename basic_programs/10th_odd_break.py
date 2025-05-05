count = 0
first_number = int(input())
last_number = int(input())
for x in range(first_number,last_number+1):
    if x%2 != 0:
        count = count + 1 
    if count == 10:
        print(count)
        print(x)
        break