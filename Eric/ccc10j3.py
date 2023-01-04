import math

A = 0
B = 0


while True:
    card = input().split()
    if len(card) > 2:
        if card[2] not in 'AB':
            card[2] = int(card[2])
    match card[0]:
        case '1':
            if card[1] == 'A':
                A = card[2]
            else:
                B = card[2]
        case '2':
            if card[1] == 'A':
                print(A)
            else:
                print(B)
                
        case '3':
            if card[1] == 'A':
                A += B
            else:
                B += A
        case '4':
            if card[1] == 'A':
                A += B
            else:
                B += A
        case '5':
            if card[1] == 'A':
                A -= B
            else:
                B -= A
        case '6':
            if card[1] == 'A':
                A /= B
                A = math.floor(A)
            else:
                B /= A
                B = math.floor(B)
        case '7':
            break
        