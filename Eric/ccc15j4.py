n = int(input())
time = -1
friendlist = []




def action(command,x):
    global friendlist
    global time

    match command:
        case 'R':
            existant = False
            time += 1
            for i in friendlist:
                if i[0] == x:
                    i[1] = time
                    existant = True
                    friend = i
            if existant:
                friend[1] = time
                friend[3] = False
            else:
                friendlist.append([x,time,0,False])
        case 'S':
            time += 1
            for i in friendlist:
                if i[0] == x:
                    i[2] += (time - i[1])
                    i[3] = True
        case 'W':
            if x == None:
                x = 1
            time += x-1

for i in range(n):
    c,x = input().split()
    action(c,int(x))

friendlist.sort(key=lambda x: x[0])

for tup in friendlist:
    if tup[3] == False:
        print(f'{tup[0]} -1')
    else:
        print(f'{tup[0]} {tup[2]}')
    


# 5
# R 2
# R 3
# W 5
# S 2
# S 3