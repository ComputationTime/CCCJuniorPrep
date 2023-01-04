def bounds_check(x, y):
    if x < 1 or x > 8 or y < 1 or y > 8:
        return False
    return True


def generate_moves(x, y):
    possible_moves = [(1, 2),(2, 1),(2,-1),(1, -2),(-1,-2),(-2,-1),(-2,1),(-1, 2)]
    ret_moves = []
    for move in possible_moves:
        newX = x + move[0]
        newY = y + move[1]
        if bounds_check(newX, newY):
            ret_moves.append((newX, newY))
    return ret_moves

def solve():
    startX, startY = [int(x) for x in (input().split())]
    endX, endY = [int(x) for x in (input().split())]
    if (startX == endX and startY == endY):
        print(0)
        return 0
    goal = (endX, endY)
    length = 1
    checked = [(startX, startY)]
    check_list = generate_moves(startX, startY)
    while True:
        next_layer = []
        remove_nodes = []
        if goal in check_list:
            print(length)
            return length
        for move in check_list:
            remove_nodes.append(move)
            checked.append(move)
            next_layer += generate_moves(move[0], move[1])
        for _ in range(len(remove_nodes)):
            check_list.pop(0)
        for n in next_layer:
            if n not in checked and n not in check_list:
                check_list.append(n)
        length += 1

solve()