def pre_to_post(equation):
    operators = {'+', '-'}
    pre = equation.split()
    post = []
    while len(pre) > 0:
        element = pre.pop()
        if element not in operators:
            post.append(element)
        else:
            a = post.pop()
            b = post.pop()
            post.append(f"{a} {b} {element}")
    return post[0]

answers = []
eq = input()
answers.append(pre_to_post(eq))
while eq != '0':
    eq = input()
    answers.append(pre_to_post(eq))
for answer in answers[:-1]:
    print(answer)

