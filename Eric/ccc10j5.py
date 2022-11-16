Ax, Ay = input().split()
Bx, By = input().split()
Ax = int(Ax)
Ay = int(Ay)
Bx = int(Bx)
By = int(By)

completion = False

searchlist = []

explored_tiles = []

def search(knightx,knighty,steps):
    global output
    global completion
    explored_tiles.append([knightx,knighty])
    if completion != True:
        if knightx == Bx and knighty == By:
            completion = True
            output = steps
        else: 
            searchlist.append(knightx-1)
            searchlist.append(knighty-2)
            searchlist.append(steps+1)

            searchlist.append(knightx+1)
            searchlist.append(knighty-2)
            searchlist.append(steps+1)

            searchlist.append(knightx-1)
            searchlist.append(knighty+2)
            searchlist.append(steps+1)

            searchlist.append(knightx+1) 
            searchlist.append(knighty+2)
            searchlist.append(steps+1)

            searchlist.append(knightx-2)
            searchlist.append(knighty-1)
            searchlist.append(steps+1)

            searchlist.append(knightx+2)
            searchlist.append(knighty-2)
            searchlist.append(steps+1)

            searchlist.append(knightx-2)
            searchlist.append(knighty+1)
            searchlist.append(steps+1)

            searchlist.append(knightx+2)
            searchlist.append(knighty+1)
            searchlist.append(steps+1)
                    

search(Ax,Ay,0)

while completion != True:
    x = searchlist.pop(0)
    y = searchlist.pop(1)
    steps = searchlist.pop(2)
    search(x,y,steps)

print(output)
                      
                    










    

        


