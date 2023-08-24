import random

vet = []

for i in range(0, 11):
    vet.append(random.randint(0,10))

max_num = 0
sec_max = 0

for i in range(0, len(vet)):
    if vet[i] > max_num:
        max_num = vet[i]
    if sec_max < vet[i] < max_num:
        sec_max = vet[i]
    
print(vet, max_num, sec_max)