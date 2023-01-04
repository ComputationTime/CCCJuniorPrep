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
 


    seq_found = False

    for i in range(len):
        if i == 0:
            pass
        else:
            if line_diff[0:i] == line_diff[i:i*2]:
                output = i
                seq_found = True
                break
    
    if seq_found != True:
        if line_diff[0] == line_diff[-1]:
            output = len-2
        else:
            output = len-1
    
    
            

    
    print(output)
    
        






    # 7 3 4 6 4 5 7 5