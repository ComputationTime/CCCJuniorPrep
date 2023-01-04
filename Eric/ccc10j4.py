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

    
        


line = input().split()
line = list(map(int,line))
line_diff = diff_checker(line)
print(line_diff)





