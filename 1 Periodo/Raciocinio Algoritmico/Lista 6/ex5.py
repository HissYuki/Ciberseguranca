vet = [0, 1, 2, 3, 4]

for i in range(0, len(vet)):
    if i > 0:
        print(f"Antecessor: {vet[i-1]}")
    print(f"Atual: {vet[i]}")
    if i < len(vet) - 1:
        print(f"Sucessor: {vet[i+1]}")


