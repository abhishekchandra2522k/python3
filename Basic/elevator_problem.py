user_floor=3
current_floor=int(input())
difference = user_floor - current_floor

if difference > 0:
    current_floor = user_floor
    print("Move Down")
if difference < 0:
    current_floor= user_floor
    print("Move up")