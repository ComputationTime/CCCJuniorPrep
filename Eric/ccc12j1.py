limit = int(input())
speed = int(input())

fine = 0

if speed > limit and speed < limit+20:
    print('You are speeding and your fine is $100.')
elif speed > limit+20 and speed < limit+30:
    print('You are speeding and your fine is $270.')
elif speed > limit+30:
    print('You are speeding and your fine is $500.')
else:
    print('Congratulations, you are within the speed limit!')

