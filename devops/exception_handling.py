try:
    number = int(input("Enter a number: "))
    result = 10/number
except ValueError:
    print("Invalid value entered")
except ZeroDivisionError:
    print("Cannot divide number by zero")
except Exception as e:
    print(f"An unexpected exception occured {e}")
else:
    print(f"Result is {result}")

print("The program ends here")