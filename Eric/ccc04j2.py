year_X = int(input())
year_Y = int(input())

year_list = [year_X]


while year_X + 60 < year_Y:
    year_X += 60
    year_list.append(year_X)

for year in year_list:
    print(f'All positions change in year {year}')