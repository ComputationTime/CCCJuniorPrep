drillx = 0
drilly = -1
drilled_cords = [(0,-1)]
danger = False
def drill(direction, steps):
    global drillx
    global drilly
    global danger
    match direction:
        case 'd':
            for i in range(1,steps+1):
                if (drillx,drilly-i) in drilled_cords:
                    danger = True
                drilled_cords.append((drillx,drilly-i))
            drilly -= steps
        case 'u':
            for i in range(1,steps+1):
                if (drillx,drilly+i) in drilled_cords:
                    danger = True
                drilled_cords.append((drillx,drilly+i))
            drilly += steps
        case 'l':
            for i in range(1,steps+1):
                if (drillx-i,drilly) in drilled_cords:
                    danger = True
                drilled_cords.append((drillx-i,drilly))
            drillx -= steps
        case 'r':
            for i in range(1,steps+1):
                if (drillx+i,drilly) in drilled_cords:
                    danger = True
                drilled_cords.append((drillx+i,drilly))
            drillx += steps
    if danger:
        return (drillx,drilly,'DANGER')
    else:
        return (drillx,drilly,'safe')


drill('d',2)
drill('r',3)
drill('d',2)
drill('r',2)
drill('u',2)
drill('r',2)
drill('d',4)
drill('l',8)
drill('u',2)

while True:
    direction, steps = input().split()
    output = drill(direction,int(steps))
    if direction == 'q':
        break
    print(f'{output[0]} {output[1]} {output[2]}')
    if output[2] == 'DANGER':
        break

    