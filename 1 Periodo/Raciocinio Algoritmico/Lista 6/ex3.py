num = int(input('Digite um número: '))
vet = [num]

cont = input('Deseja continuar inserindo valores? Y/N\n')

while cont.casefold() == "y":
    num = int(input('Digite um número:'))
    vet.append(num)
    cont = input('Deseja continuar inserindo valores? Y/N\n')

print(vet)
