initial_height = float(input())
daily_growth = float(input())
days = int(input())

height = initial_height

for i in range(days):
    height = height * (1 + daily_growth)

print(f"After {days} days, the plant is {round(height, 2)} cm tall.")