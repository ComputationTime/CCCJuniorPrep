unfinished = True

operators = ['-','+',]


def pre_to_post(line):
    pre_stack = line.split()
    post_stack = []
    while len(pre_stack) > 0:
        element = pre_stack.pop() # this will remove the last element of the list. It's what you wanna remove
        if element in operators:
            element2 = post_stack.pop()
            element1 = post_stack.pop()
            new_element = (f'{element} {element1} {element2}')
            post_stack.append(new_element)
        else: 
            post_stack.append(element)
    return post_stack[0][::-1]




while unfinished:
    line = input()
    if line == "0":
        unfinished = False
    else:
        print(pre_to_post(line))
    

    


            

    