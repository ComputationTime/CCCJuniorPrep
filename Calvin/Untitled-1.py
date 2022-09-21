input_finish = False

lowest_temp = 201
lowest_temp_city = ''


while not input_finish:
    curr_line = input().split()
    curr_line[1] = int(curr_line[1])
    if curr_line[0].strip() == 'Waterloo':
        input_finish = True
    if curr_line[1] < lowest_temp:
        lowest_temp = curr_line[1]
        lowest_temp_city = curr_line[0]

print(lowest_temp_city)
