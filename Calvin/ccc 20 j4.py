t = input()
string = input()
not_found = True
for i in range(len(string)):
    if string in t:
        not_found = False
        print('yes')
        break
    string = string[1:] + string[0]
 
if not_found:
    print('no')