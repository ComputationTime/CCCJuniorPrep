from itertools import combinations
n = int(input())

dependancies = []
people_list = []
combos = []

def combo_maker(people,size):
    combolist = []
    if size == 1:
        return people
    for combo in combinations(people,size):
        combolist.append(combo)  
    return combolist


for i in range(1,n):
    person = int(input())
    people_list.append(i)
    dependancies.append((person,i))


for i in range(1,n):
    possible_combos = combo_maker(people_list,i)
    for i in possible_combos:
        combos.append(i)


for dependancy in dependancies: 
    for combo in combos:
        if combo in range(1,6):
            if combo == dependancy[0]:
                print(dependancy[0], dependancy[1], "removing", combo)
                combos.remove(combo)
               
        else:
            if dependancy[0] in combo and dependancy[1] not in combo:
                print(dependancy[0], dependancy[1], "removing", combo)
                combos.remove(combo)
                


print(len(combos)+1)

