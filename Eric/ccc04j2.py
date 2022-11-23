year_X = int(input())
year_Y = int(input())

year_list = []


while year_X < year_Y:
    year_list.append(year_X)
    year_X += 60

for year in year_list:
    print(f'All positions change in year {year}')