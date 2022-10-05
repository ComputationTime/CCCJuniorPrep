lines = int(input())

for i in range(lines):
    curr_line = input()
    curr_line = curr_line.split()
    print(int(curr_line[0]) * str(curr_line[1]))