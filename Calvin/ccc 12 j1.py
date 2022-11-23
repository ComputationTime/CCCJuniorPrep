limit = int(input())
speed = int(input())

if speed < limit:
    print("Congratulations, you are within the speed limit!")
elif speed >= limit and speed <= limit + 20:
    print("You are speeding and your fine is $100.")
elif speed >= limit + 21 and speed <= limit + 30:
    print("You are speeding and your fine is $270.")
elif speed >= limit + 31:
    print("You are speeding and your fine is $500.")
