n = int(input())
k = int(input())


combos = 1
people = [1 for i in range(k)]
people[-1] += n - k


def solve(n,k):
    combos = 1
    people = [1 for i in range(k)]
    people[0] += n - k
    for i in range(k-1):
        while people[i] > people[i+1] and people[i]-1 >= people[i+1]+1:
            people[i] -= 1
            people[i+1] += 1
            combos += 1
            print(people)

    # while (people[0] - people[1]) > 1:
    #     for i in range(k-1):
    #         print(i)
    #         while people[i] > people[i+1]:
    #             if (people[i+1]+1) > people[i]-1:
    #                 try:
    #                     people[i+2] += 1
    #                     people[i] -= 1
    #                 except:
    #                     IndexError
    #             else:
    #                 people[i] -= 1
    #                 people[i+1] += 1
    #                 combos+=1
    #                 print(people)
    print(combos)


    
solve(n,k)


