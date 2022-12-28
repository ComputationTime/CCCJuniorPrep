n = int(input())
if n < 6:
    cnt = n // 2 + 1
else:
    hand_1 = 5
    hand_2 = n - 5
    cnt = 1
    for i in range(n//2):
        hand_1 -= 1
        hand_2 += 1
        if hand_2 > hand_1:
            break
        cnt += 1
        
print(cnt)