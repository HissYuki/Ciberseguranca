vet = [10, 20, 30, 40, 50, 60]

for i in range(len(vet)):
    opposite = len(vet) - 1 - i
    for j in range(len(vet)):
        if j == i or j == opposite:
            print(vet[j], end=" ")
        else:
            print(" ", end=" ")
    print("")
