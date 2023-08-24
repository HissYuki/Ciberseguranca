import random

vet = []
for i in range(0, 100):
    vet.append(random.randint(0, 10))

print(vet)

for i in range(0, 100):
    sum = vet[i] + vet[len(vet) - 1 - i]
    print(sum)