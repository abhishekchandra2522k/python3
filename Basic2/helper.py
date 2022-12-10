def days_to_units(days, conversion_unit):
    if conversion_unit == "hours":
        return f"{days} days are {days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{days} days are {days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dict):
    try:
        user_input_num = int(days_and_unit_dict["days"])

        # we want to do conversion only for positive integers
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num, days_and_unit_dict["unit"])
            print(calculated_value)
        else:
            print("invalid number")

    except ValueError:
        print("Invalid value entered")

user_input_message = "Enter number of days and a conversion unit: \n"
