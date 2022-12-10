from helper import validate_and_execute, user_input_message
# from helper import * // for importing all the functions/variables from the module
# import helper as h // for importing all functions/variables and you can use them with h.func() or h.var alias

user_input = ''
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dict)
