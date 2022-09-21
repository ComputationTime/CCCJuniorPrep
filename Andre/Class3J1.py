finished = False

lowest_temp = 201
lowest_temp_city = ''

while not finished:
    city_and_temp = input().split()
    city_and_temp[1] = int(city_and_temp[1])
    if city_and_temp[0] == 'Waterloo':
        finished = True
    if lowest_temp > city_and_temp[1]:
        lowest_temp = city_and_temp[1]
        lowest_temp_city = city_and_temp[0]

print(lowest_temp_city)
