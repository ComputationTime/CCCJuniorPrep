month = int(input())
date = int(input())



if date == 18 and month == 2:
    print('Special')

elif month == 2:
    if date > 18:
        print('After')
    if date < 18:
        print('Before')
elif month < 2:
    print('Before')
elif month > 2:
    print('After')