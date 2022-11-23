speed_limit = int(input())
speed = int(input())

if speed <= speed_limit:
    print('Congratulations, you are within the speed limit!')

else:
    if speed - speed_limit <= 20:
        fine = '100'
    elif speed - speed_limit <= 30:
        fine = '270'
    else:
        fine = '500'
    print('You are speeding and your fine is $' + fine + '.')
