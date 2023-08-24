vet = [1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0]
max_cont = 0
cont = 0

for i in range(len(vet)):
    if vet[i] == 0:
        cont += 1
    else:
        if cont > max_cont:
            max_cont = cont
        cont = 0
    
print(max_cont)