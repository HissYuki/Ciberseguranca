import random

vet_1 =[]
vet_2 = []

for i in range(0, 6):
    vet_1.append(random.randint(0, 10))
    vet_2.append(random.randint(0, 10))

print(vet_1, vet_2)

vet_3 = []

for i in range(0, len(vet_1)):
    vet_3.append(vet_1[i] + vet_2[i])

print(vet_3)