calculation_to_units = 24
name_of_unit = "hours"
# scn = int(input(""))


def days_to_units(days):
    return f"{days} days are {days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_num = int(user_input)
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num)
            print(calculated_value)
        else:
            print("invalid number")
    except ValueError:
        print("Invalid value entered")


user_input = input("Enter a value: \n")
validate_and_execute()
