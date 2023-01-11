visited = [[-1, -6], [-1, -7], [0, -7], [1, -7], [2, -7], [3, -7], [4, -7], [5, -7], [6, -7], [7, -7], [7, -6], [7, -5], [7, -4], [7, -3], [6, -3], [5, -3], [5, -4], [5, -5], [4, -5], [3, -5], [3, -4], [3, -3], [2, -3], [1, -3], [0, -3], [0, -2], [0, -1]]
currentc = [-1, -5]

danger = False 

while True:
    directions, numSpaces = input().split()
    if directions == 'q':
        break
    for i in range(int(numSpaces)):
        visited.append(currentc)
        if directions == 'd':
            currentc = [currentc[0], currentc[1] - 1]
        elif directions == 'u':
            currentc = [currentc[0], currentc[1] + 1]
        elif directions == 'l':
            currentc = [currentc[0] - 1, currentc[1]]
        else:
            currentc = [currentc[0] + 1, currentc[1]]
    
        if currentc in visited:
            danger = True

    if danger:
        print(currentc[0], currentc[1], "DANGER")
        break
    else:
        print(currentc[0], currentc[1], "safe")