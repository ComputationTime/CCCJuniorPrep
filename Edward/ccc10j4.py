
def solve(data):
    length = 1
    while True:
        flag = 1
        diff = []
        if len(data) == 1:
            return 0
        for i in range(1, len(data)):
            diff.append(data[i] - data[i-1])
        patt = []
        for i in range(len(diff)):
            try: 
                patt.append(diff[i % length])
            except IndexError:
                pass
        
        for i in range(len(diff)):
            if diff[i] == patt[i]:
                continue
            else:
                flag = 0
                break
        
        if flag:
            return length
        else:
            length += 1
        
        


data = [int(x) for x in input().split()]
while data != [0]:
    data = data[1:]
    print(solve(data))
    data = [int(x) for x in input().split()]

