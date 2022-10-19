daytime_min = int(input())
evening_min = int(input())
weekend_min = int(input())

plan_A = 0
plan_B = 0

if daytime_min > 250:
    plan_B += (daytime_min - 250)*0.45 + evening_min*0.35 + weekend_min*0.25
else:
    plan_B += evening_min*0.35 + weekend_min*0.25

if daytime_min > 100:
    plan_A += (daytime_min - 100)*0.25 + evening_min*0.15 + weekend_min*0.20
else:
    plan_B += evening_min*0.15 + weekend_min*0.2




print(f"Plan A costs {plan_A}")
print(f"Plan A costs {plan_B}")

if plan_B < plan_A:
    print("Plan B is cheapest")

elif plan_B > plan_A:
    print("Plan A is cheapest")

else:
    print("Plan A and B are the same price.")