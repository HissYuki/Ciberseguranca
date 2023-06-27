import random

vet = []

for i in range(0, 21):
    vet.append(random.randint(0,10))

subvet_1 = []
subvet_2 = []

for i in range(0, len(vet)//2):
    subvet_1.append(vet[i])

for i in range(len(vet)//2, len(vet)):
    subvet_2.append(vet[i])

print(vet, subvet_1, subvet_2)