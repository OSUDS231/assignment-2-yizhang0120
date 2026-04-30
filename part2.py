initial_height = float(input())
daily_growth = float(input())
days = int(input())
boost_amount = float(input())

height = initial_height

for day in range(1, days + 1):
    height = height * (1 + daily_growth)

    if day % 7 == 0:
        height = height + boost_amount

print(f"After {days} days (with a {boost_amount} cm boost every 7th day), the plant is {round(height, 2)} cm tall.")