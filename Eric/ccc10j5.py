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
    explored_tiles.append(x,y)
    if x == Bx and y == By:
        completion = True
        output = steps
    else:
        searchlist.append(x-1)
        searchlist.append(y-2)
        searchlist.append(steps+1)

        searchlist.append(x+1)
        searchlist.append(y-2)
        searchlist.append(steps+1)

        searchlist.append(x-1)
        searchlist.append(y+2)
        searchlist.append(steps+1)

        searchlist.append(x+1) 
        searchlist.append(y+2)
        searchlist.append(steps+1)

        searchlist.append(x-2)
        searchlist.append(y-1)
        searchlist.append(steps+1)

        searchlist.append(x+2)
        searchlist.append(y-2)
        searchlist.append(steps+1)

        searchlist.append(x-2)
        searchlist.append(y+1)
        searchlist.append(steps+1)

        searchlist.append(x+2)
        searchlist.append(y+1)
        searchlist.append(steps+1)
                

search(Ax,Ay,0)

while completion != True:
    x = searchlist.pop(0)
    y = searchlist.pop(1)
    steps = searchlist.pop(2)
    if x < 10 and x > -1:
        if y < 10 and y > -1:
            search(x,y,steps)

print(output)
                      
                    










    

        


