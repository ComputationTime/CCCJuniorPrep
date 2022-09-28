# *x*
#  xx
# * *

k = int(input())

if k == 0:
    k = 1
line1 = (k*"*") + (k*"x") + (k*"*")

line2 = (k*" ") + (k*"x") + (k*"x")

line3 = (k*"*") + (k*" ") + (k*"*")

for i  in range(k):
    print(line1)
    
for i in range(k):
    print(line2)

for i in range(k):
    print(line3)