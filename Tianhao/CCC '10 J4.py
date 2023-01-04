def verify(seq, n):
    for i in range(n, len(seq)):
        if seq[i] != seq[i % n]:
            return False
    return True

while True:
    tem = input().split()
    if tem[0] == "0":
        break
    tem = tem[1:]
    for i in range(0, len(tem)-1):
        tem[i] = int(tem[i+1]) - int(tem[i])
    tem.pop()

    t = len(tem)
    for i in range(1,len(tem)):
        if tem[0] == tem[i] and verify(tem,i):
            t = min(t, i)
            break
    print(t)