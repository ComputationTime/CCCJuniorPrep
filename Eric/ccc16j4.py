#0700 - 1000
#1500 - 1900
hr,min = input().split(':')
time = (int(hr)*60) + int(min)



def solve(time):
    output = time
    for i in range(time,time+120):
        if i in range(420,600) and output<600:
            output += 2
        elif i in range(900,1140) and output<1140:
            output += 2
        else:
            output += 1
    return output % 1440




arr_time = solve(time)
hr = int(arr_time // 60)
min = int(arr_time % 60)
if hr < 10:
    hr = f'0{hr}'
if min < 10:
    min = f'0{min}'
print(f'{hr}:{min}')



        



