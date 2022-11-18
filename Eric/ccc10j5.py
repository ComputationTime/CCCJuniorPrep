Ax, Ay = input().split()
Bx, By = input().split()
Ax = int(Ax)
Ay = int(Ay)
Bx = int(Bx)
By = int(By)

completion = False

searchlist = []

explored_tiles = []

def search(x,y,steps):
    global output
    global completion
    explored_tiles.append(f"{x} {y}")
    if x == Bx and y == By:
        completion = True
        output = steps
    else:
        # only append stuff that hasn't been explored yet. AKA use your explored_tiles list (this is for efficiency only)
        if f"{x-1} {y-2}" in explored_tiles:
            pass
        else:
            searchlist.append(x-1)
            searchlist.append(y-2)
            searchlist.append(steps+1)

        if f"{x+1} {y-2}" in explored_tiles:
            pass
        else:
            searchlist.append(x+1)
            searchlist.append(y-2)
            searchlist.append(steps+1)

        if f"{x-1} {y+2}" in explored_tiles:
            pass
        else:
            searchlist.append(x-1)
            searchlist.append(y+2)
            searchlist.append(steps+1)

        if f"{x+1} {y+2}" in explored_tiles:
            pass
        else:
            searchlist.append(x+1) 
            searchlist.append(y+2)
            searchlist.append(steps+1)

        if f"{x-2} {y-1}" in explored_tiles:
            pass
        else:
            searchlist.append(x-2)
            searchlist.append(y-1)
            searchlist.append(steps+1)

        if f"{x+2} {y-1}" in explored_tiles:
            pass
        else:
            searchlist.append(x+2)
            searchlist.append(y-1)
            searchlist.append(steps+1)

        if f"{x-2} {y+1}" in explored_tiles:
            pass
        else:
            searchlist.append(x-2)
            searchlist.append(y+1)
            searchlist.append(steps+1)

        if f"{x+2} {y+1}" in explored_tiles:
            pass
        else:
            searchlist.append(x+2)
            searchlist.append(y+1)
            searchlist.append(steps+1)
                

search(Ax,Ay,0)

while completion != True:
    x = searchlist.pop(0) # pop also removes x from the list
    y = searchlist.pop(0) # this means you should pop(0) again instead of pop(1)
    steps = searchlist.pop(0) # and this should also be pop(0)
    if x < 9 and x > -1:
        if y < 9 and y > -1:
            search(x,y,steps)

print(output)
                      
                    










    

        


