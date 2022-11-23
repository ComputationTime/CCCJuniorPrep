word = input()
len = len(word)
max_pal = 0
for start in range(len):
    for end in range(start+1, len+1):
        if word[start:end] == word[start:end][::-1] and max_pal < end - start:
            max_pal = end-start
print(max_pal)

# n = 7

# for i in range(n):
#     for j in range(i+1, n):
#         print(i,j)
# word = 'string'

# word[0:6]
