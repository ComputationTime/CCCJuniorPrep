# board = [[1 for i in range(6)] for j in range(6)]

# def place_queen(pos):
#     x, y = pos
#     board[x-1] = [0 for i in range(6)]
#     for i in range(6):
#         board[i][y-1] = 0
#     for i in range(-6, 6):
#         if (x-1+i) in range(6):
#             if (y-1+i) in range(6):
#                 board[x-1 + i][y-1 + i] = 0
#             if (y-1-i) in range(6):
#                 board[x-1 + i][y-1 - i] = 0
# num_lines = int(input().split()[1])

# for _ in range(num_lines):
#     queen_pos = list(map(int, input().split()))
#     place_queen(queen_pos)

# output = sum(list(map(sum, board)))
# print(output)

# N, num_queens = list(map(int, input().split()))



# def place_queen(pos):
#     x, y = pos
#     # make them index 0
#     x -= 1
#     y -= 1

#     board[y] = [0 for i in range(N)]
#     for i in range(N):
#         board[i][x] = 0
#     for i in range(-N, N):
#         if x + i in range(N):
#             if y + i in range(N):
#                 board[y + i][x + i] = 0
#             if y - i in range(N):
#                 board[y - i][x + i] = 0

# board = [[1 for i in range(N)] for j in range(N)]



# for i in range(num_queens):
#     # place queens on board
#     pos = list(map(int, input().split()))
#     place_queen(pos)

# output = sum(list(map(sum, board)))
# print(output)

a = [0, 1, 2, 3, 4]

def fn(x):
    return str(x) + 'a'

print(list(map(fn, a)))