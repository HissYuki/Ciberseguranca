import random
import math

vet = []
for i in range(0, 6):
    vet.append(random.randint(0, 10))

sum = 0

for i in range(0, len(vet)):
    sum += vet[i]

med = sum / len(vet)
md = 0

for i in range(0, len(vet)):
    md += (vet[i] - med)**2

md = math.sqrt(md / len(vet))

print(f'Média: {med}\nDesvio padrão: {md}')