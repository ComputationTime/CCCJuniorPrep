plan = [(0,-1),(0,-2),(0,-3),(1,-3),(2,-3),(3,-3),(3,-4),(3,-5),(4,-5),(5,-5),
        (5,-4),(5,-3),(6,-3),(7,-3),(7,-4),(7,-5),(7,-6),(7,-7),(6,-7),(5,-7),
        (4,-7),(3,-7),(2,-7),(1,-7),(0,-7),(-1,-7), (-1,-6), (-1, -5)]



def parse_instructions(direction: str, magnitude: int, start):
    if direction == 'q':
        return None
    m = { "l": (-1, 0), "r": (1, 0), "u":(0, 1), "d": (0, -1) }
    ret = []
    for val in range(1, magnitude+1):
        dx, dy = m[direction]
        sx, sy = start
        ret.append((sx + dx * val, dy * val + sy))

    return ret





def solve():
    while True:
        direction, magnitude = input().split()
        dir_vector = parse_instructions(direction, int(magnitude), plan[-1])
        dangerFlag = 0
        if dir_vector is None:
            return
        for dir in dir_vector:
            dirX, dirY = dir
            if dir in plan:
                dangerFlag = 1
            plan.append(dir)
        dirX, dirY = plan[-1]
        if dangerFlag:
            print(dirX, dirY, 'DANGER')
            return
        print(dirX, dirY, 'safe')

solve()