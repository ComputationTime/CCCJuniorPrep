def solve():
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())

    if x1 == x2 == x3 == 60:
        print("Equilateral")
    elif x1 + x2 + x3 == 180 and (x1 == x2 or x2 == x3 or x1 == x3):
        print("Isosceles")
    elif x1 + x2 + x3 == 180 and x1 != x2 and x2 != x3 and x1 != x3:
        print("Scalene")
    else:
        print("Error")

solve()


