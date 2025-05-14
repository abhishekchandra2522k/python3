import random

#variable length argument (non keyword, tuple type)
def order_food(min_order, *args):
    print(f"You have ordered {min_order}")
    for i in args:
        print(f"You have ordered {i}")
    print("Your food will be delivered in 30mins")
    print("Enjoy the party")

order_food("salad", "pizza", "cold drink", "biryani")


# kwargs (keyword argument, dict type)
def time_activity(*args, **kwargs):
    '''
    Input: multiple values for minutes, key=value pair activities
    Output: return sum of minutes, + random min spect on random activity
    '''
    # print(args)
    # print(kwargs)
    min = sum(args) + random.randint(0,60)
    # print(min)
    choice = random.choice(list(kwargs.keys()))
    # print(choice)
    print(f"You have to spend {min} minutes in {kwargs[choice]}")

time_activity(10,20,30, hobby="Dance",sports="Boxing", fun="Driving", work="DevOps")