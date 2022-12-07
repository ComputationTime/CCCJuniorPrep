day, no_of_days = map(int,input().split())
step = day
count = 6

print('Sun Mon Tue Wed Thr Fri Sat')
for i in range(no_of_days + step):
    date = i - step +1
    if i == (no_of_days + step):
        if date < 10:
            print(f"  {date}",end = None)
        else:
            print(f" {date}",end = None)
    elif date == no_of_days:
        if date < 10:
            print(f"  {date}",end = '')
        else:
            print(f" {date}",end = '')
    else:
        if count > 0:
            if day > 0:
                print("    ",end = '')
                day -= 1
            else:
                if count == 0:
                    if date < 10:
                        print(f"  {date}",end = '')
                    else:
                        print(f" {date}",end = '')
                else:
                    if date < 10:
                        print(f"  {date} ",end = '')
                    else:
                        print(f" {date} ",end = '')

            count -= 1
        else:
            if date < 10:
                print(f"  {date}")
            else:
                print(f" {date}")
            count += 6
    