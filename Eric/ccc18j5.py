N = int(input())
book = []
paths = []
completion = False


def search(pg,lvl):
    page = book[pg-1]
    if page[0] == True:
        return
    page[0] = True
    for i in page:
        if i == True:
            pass
        elif i == 0:
            paths.append(lvl)
        else:
            search(i,lvl+1)

for i in range(N):
    page = [int(i) for i in input().split()]
    page.insert(0,False)
    book.append(page)


search(1,1)
paths = sorted(paths)

output = 'Y'

for page in book:
    if page[0] == False:
        output = 'N'

print(output)
print(paths[0])






