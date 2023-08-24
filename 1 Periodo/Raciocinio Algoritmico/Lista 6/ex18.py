vet = [5,2,1,3,4]

for i in range(len(vet)):
    for j in range(i+1, len(vet)):
        if vet[j] < vet[i]:
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux

            

    