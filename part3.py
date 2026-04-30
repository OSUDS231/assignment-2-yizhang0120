initial_height = float(input())
daily_growth = float(input())
days = int(input())
boost_amount = float(input())
max_height = float(input())

height = initial_height

for day in range(1, days + 1):
    height = height * (1 + daily_growth)

    if day % 7 == 0:
        height = height + boost_amount

    if height >= max_height:
        height = max_height
        break

print(f"After {day} days, the plant is {round(height, 2):.2f} cm tall.")