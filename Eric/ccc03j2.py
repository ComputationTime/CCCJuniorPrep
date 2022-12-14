while True:
    lowest_num = 0
    lowest_index = 0
    numlist = []
    numlist2 = []
    num = int(input())
    if num == 0:
        break
    else:
        for i in range(num):
            for j in range(num):
                if i * j == num:
                    numlist.append((i,j))
        for i in range(len(numlist)):
            numlist2.append(numlist[i][0] + numlist[i][1])
        numlist2 = sorted(numlist2)
        for i in range(len(numlist)):
            if numlist[i][0] + numlist[i][1] == numlist2[0]:
                num1,num2 = numlist[i][0],numlist[i][1]
                break
        perimeter = numlist2[0] * 2
        print(f'Minimum perimeter is {perimeter} with dimensions {num1} x {num2}')
    

    
    


    
                    