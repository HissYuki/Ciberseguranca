import random

mat = []

for i in range(50):
    mat.append([])
    for j in range(50):
        mat[i].append(random.randint(0, 9))

sum_d = 0
sum_s = 0

for i in range(50):
    for j in range(50):
        if i == j:
            sum_d += mat[i][j]
        if 49 - i == j:
            sum_s += mat[i][j]

print(sum_d//50)
print(sum_s//50)