N = int(input())
book = []
paths = []
completion = False

def search(node,pages):
    book[node][0] = True
    pages+=1
    node_children = []
    for i in book[node]:
        if i == True or i == False:
            pass
        else:
            node_children.append(i)
    for node in node_children:
        book[node-1][0] = True
        if book[node-1][1] == 0:
            paths.append(pages)
        else:
            search(book[node-1][1],pages)


    

    

for i in range(1,N+1):
    line = input()
    page = line.split()
    page = list(map(int,page))
    page.insert(0,False)
    book.append(page)


search(0,0)

paths = sorted(paths)

output = 'Y'


for page in book:
    if page[0] == False:
        output = 'N'

print(output)
print(paths[0]+1)






