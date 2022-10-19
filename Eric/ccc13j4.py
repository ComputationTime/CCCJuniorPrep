time = int(input())
tasks = int(input())
min_spent = 0
output = 0

task_list = []

for i in range(tasks):
    min = int(input())
    task_list.append(min)

task_list = sorted(task_list)



for i in range(len(task_list)):
    min = task_list[i]
    if (min_spent + min) <= time:
        min_spent += min
        output += 1
    else:
        pass

print(output)

