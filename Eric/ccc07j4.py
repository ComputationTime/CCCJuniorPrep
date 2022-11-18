line1 = input()

line2 = input()

line1 = line1.replace(" ","")

line2 = line2.replace(" ","")


line1 = sorted(line1)
line2 = sorted(line2)

if line1 == line2:
    print('Is an anagram.')

else:
    print('Is not an anagram.')
    



