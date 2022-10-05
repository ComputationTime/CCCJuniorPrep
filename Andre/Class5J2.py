from email import message


num_lines = int(input())

output =''

# for loop

for _ in range(num_lines):
    message = input().split()
    output += message[1]*int(message[0]) + '\n'
    # print(message[1]*int(message[0]))

# print
print(output)