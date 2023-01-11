def gen_sequence(t1, t2, ret):
    t3 = t1 - t2
    ret.append(t3)
    if t3 <= t2:
        gen_sequence(t2, t3, ret)



def solve():
    t1 = int(input())
    t2 = int(input())
    ret = [t1, t2]
    gen_sequence(t1, t2, ret)
    print(len(ret))
    

solve()