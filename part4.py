initial_height = float(input())
daily_growth = float(input())
target_height = float(input())
days = int(input())
boost_amount = float(input())

found = False

for interval in range(days, 0, -1):
    height = initial_height

    for day in range(1, days + 1):
        height = height * (1 + daily_growth)

        if day % interval == 0:
            height = height + boost_amount

    if height >= target_height:
        print(f"To reach at least {target_height:.1f} cm in {days} days, apply a {boost_amount:.1f} cm boost every {interval} days.")
        found = True
        break

if not found:
    print(f"Target height not achievable within {days} days, even with daily boosts.")