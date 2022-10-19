a = int(input())
b = int(input())
c = int(input())
A = max(a - 100,0)* 0.25 + 0.15 * b + 0.2 * c
B = max(a - 250,0)* 0.45 +0.35 * b + 0.25 * c
print("Plan A costs %.2f" % A)
print("Plan B costs %.2f" % B)
if A < B:
  print("Plan A is cheapest.")
elif B < A:
  print("Plan B is cheapest.")
else:
  print("Plan A and B are the same price.")