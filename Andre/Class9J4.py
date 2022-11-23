time = int(input())
num_chores = int(input())
chore_times = []
for chore in range(num_chores):
    chore_times.append(int(input()))
chore_times.sort()
sum = 0
num_completed = 0
for task_time in chore_times:
    sum += task_time
    if sum <= time:
        num_completed += 1
    else:
        break
print(num_completed)