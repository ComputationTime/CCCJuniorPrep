
def solve(storage):
    length = 1
    while True:
        flag = 1
        diff = []
        if len(storage) == 1:
            return 0
        for i in range(1, len(storage)):
            diff.append(storage[i] - storage[i-1])
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
        
        


storage = [int(x) for x in input().split()]
while storage != [0]:
    storage = storage[1:]
    print(solve(storage))
    storage = [int(x) for x in input().split()]

