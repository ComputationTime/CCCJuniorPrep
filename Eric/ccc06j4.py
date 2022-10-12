from os import kill


input_completion = False

while input_completion == False:
    do_first = input()
    do_second = input()
    if do_first == "0" and do_second == "0":
        input_completion = True
    

