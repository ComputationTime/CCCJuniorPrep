daytime = int(input())
evening = int(input())
weekend = int(input())

A_daytime = max(daytime - 100,0) * 0.25
B_daytime = max(daytime - 250,0) * 0.45

A_evening = 0.15 * evening 
B_evening = 0.35 * evening

A_weekend = 0.2 * weekend
B_weekend = 0.25 * weekend

A = A_daytime + A_evening + A_weekend
B = B_daytime + B_evening + B_weekend


if abs(A - B) < 0.01 :
    print(f'Plan A costs {A:.2f}')
    print(f'Plan B costs {B:.2f}')
    print('Plan A and B are the same price.')
elif A > B:
    print(f'Plan A costs {A:.2f}')
    print(f'Plan B costs {B:.2f}')
    print('Plan B is cheapest.')
else:
    print(f'Plan A costs {A:.2f}')
    print(f'Plan B costs {B:.2f}')
    print('Plan A is cheapest.')
