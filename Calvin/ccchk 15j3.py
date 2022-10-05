def place_queen(pos):
    x, y = pos
    x -=1
    y -=1

    board[y] = [0 for i in range(6)]
    for i in range(6):
        board[i][x] = 0
    for i in range(-5,6):
        if y + i in range(6):
            if x+i in range(6):
                board[y+i][x+i] = 0
            if y-1 in range(6):
                board[y-i][x+i] = 0


board = [[1 for i in range(6)]for j in range(6)]


num_queens - int(input().split()[1])
for i in range(nm_queens):

    pos = list(map(int, input().split()))
    place_queen(pos)
ouptut = sum(list(map(sum,board)))
print(output)


