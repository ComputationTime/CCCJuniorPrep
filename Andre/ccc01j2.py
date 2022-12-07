# n and mod_m
n = int(input())
mod_m = int(input())

n_inverse = None

for number in range(1, mod_m):
    if n*number % mod_m == 1:
        n_inverse = number

if n_inverse is not None:
    print(n_inverse)
else:
    print('No such integer exists.')