start = tuple(map(int, input().split()))
finish = tuple(map(int, input().split()))

def valid(num):
    return num < 9 and num > 0

def movements(state):
    x, y = state[0]
    steps = state[1]
    potential_moves = [
        [(x+1,y+2),steps+1],
        [(x-1,y+2),steps+1],
        [(x-1,y-2),steps+1],
        [(x+1,y-2),steps+1],
        [(x+2,y+1),steps+1],
        [(x-2,y+1),steps+1],
        [(x-2,y-1),steps+1],
        [(x+2,y-1),steps+1]
    ]
    moves = []
    for move_step in potential_moves:
        if valid(move_step[0][0]) and valid(move_step[0][1]):
            moves.append(move_step)
    return moves


if start == finish:
    print(0)
else:
    queue = [[start,0]]
    while True:
        current = queue.pop(0)
        point = current[0]
        steps = current[1]
        if point == finish:
            print(steps)
            break
        queue.extend(movements(current))
