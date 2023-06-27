import random

vet = []

for i in range(0, 11):
    vet.append(random.randint(0, 100))

sum_2 = 0
sum_5 = 0
vet_10 = []

for i in range(0, len(vet)):
    if vet[i] % 2 == 0:
        sum_2 += vet[i]
    if vet[i] % 5 == 0:
        sum_5 += vet[i]
    if vet[i] % 10 == 0:
        vet_10.append(vet[i])

print(vet)
print(sum_2)
print(sum_5)
print(vet_10)