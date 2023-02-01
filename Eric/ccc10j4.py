def diff_checker(line):
    last_num = None
    diff_list = []
    for i in line:
        if last_num == None:
            last_num = i
        else:
            diff = i - last_num
            diff_list.append(diff)
            last_num = i
    return diff_list

    
        

while True:
    line = input().split()
    if line == 0:
        break
    line = list(map(int,line))
    len = line.pop(0)
    line_diff = diff_checker(line)
 

    for i in range(1,len+1):
        seq = []
        pass

    
        






    # 7 3 4 6 4 5 7 5