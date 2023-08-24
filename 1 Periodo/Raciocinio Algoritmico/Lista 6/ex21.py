vet = [1,1,1,1,1,1,1,1,1,1,1]
sum_1 = 0
sum_2 = 0
equal = True
ok = True
for i in range(0, len(vet)-2):
    sum_1 += vet[i] * (10-i)
    sum_2 += vet[i] * (11-i)
    if vet[i] != vet[0]:
        equal = False
sum_2 += vet[9] * 2

ver_1 = (sum_1 * 10) % 11
ver_2 = (sum_2 * 10) % 11

print(vet[9], ver_1)
print(vet[10], ver_2)

if ver_1 != vet[9] or ver_2 != vet[10] or equal:
    ok = False

if ok:
    print('CPF válido!')
else:
    print('CPF inválido!')

