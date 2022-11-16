board=[]

for i in range(8):
    board.append([65, 65, 65, 65, 65, 65, 65, 65])
a,b=map(int, input().split())
c,d=map(int, input().split())

board[a-1][b-1]=0
order=[[a-1,b-1]]

def p(x,y,t):
    global order
    if 0 <= x <= 7 and 0 <= y <= 7:
        if board[x][y] > t+1:
            board[x][y] = t+1
            order.append([x,y])


def m(coordinate):
    global order
    order.pop(0)
    x = coordinate[0]
    y = coordinate[1]
    p(x+1,y+2, board[x][y])
    p(x+2,y+1, board[x][y])
    p(x+1,y-2, board[x][y])
    p(x+2,y-1, board[x][y])
    p(x-2,y-1, board[x][y])
    p(x-1,y-2, board[x][y])
    p(x-2,y+1, board[x][y])
    p(x-1,y+2, board[x][y])

while len(order) > 0:
    m(order[0])

print(board[c-1][d-1])
