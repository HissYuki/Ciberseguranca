import random

mat = []

for i in range(7):
    mat.append([])
    for j in range(5):
        mat[i].append(random.randint(0, 9))

print(mat)

for i in range(5):
    max = 0
    sum = 0
    for j in range(7):
        if mat[j][i] > max:
            max = mat[j][i]
        sum += mat[j][i]
    print(f'Coluna {i}: {sum}/{max}')
