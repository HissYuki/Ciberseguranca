import random

vet = []

for i in range(0, 11):
    vet.append(random.randint(0,10))

med = 0

for i in range(0, len(vet)):
    med += vet[i]

med /= len(vet)

vet_m = []

for i in range(0, len(vet)):
    if vet[i] < med:
        vet_m.append(-1)
    elif vet[i] == med:
        vet_m.append(0)
    else:
        vet_m.append(1)

print(vet, vet_m)