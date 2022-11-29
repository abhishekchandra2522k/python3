calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(days, custom_message):
    print(f"{days} days are {days * calculation_to_units} {name_of_unit}")
    print(custom_message)


days_to_units(3, "greeting")
