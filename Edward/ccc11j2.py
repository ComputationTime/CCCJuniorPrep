def altitude(h, t):
    A = (-6 * (t**4))  + (h*(t**3)) + (2*(t**2)) + t
    return A 


def solve():
    h = int(input()) # 0 to 100
    M = int(input()) # 1 to 239
    counter = 1
    height = altitude(h, 1)
    while (height >= 0 and counter <= M):
        counter += 1
        height = altitude(h, counter)
    if (counter > M):
        print("The balloon does not touch ground in the given time.")
    else:
        print("The balloon first touches ground at hour:")
        print(f"{counter}")


solve()