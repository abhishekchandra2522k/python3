calculation_to_units = 24
name_of_unit = "hours"
# scn = int(input(""))


def days_to_units(days):
    return f"{days} days are {days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_num = int(num_of_days)

        # we want to do conversion only for positive integers
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num)
            print(calculated_value)
        else:
            print("invalid number")
    except ValueError:
        print("Invalid value entered")


user_input = ''
while user_input != "exit":
    user_input = input("Enter number of days as a list : \n")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days in user_input.split(","):
        validate_and_execute()
