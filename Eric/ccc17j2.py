number = int(input())
shift = int(input())
answer = number

for i in range(shift):
    number *= 10
    answer += number

print(answer)
