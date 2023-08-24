vet =[]
num = int(input('Digite um número: '))
if num % 2 == 0:
    vet.append(num)

cont = input('Deseja continuar inserindo valores? Y/N\n')

while cont.casefold() == "y":
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        vet.append(num)
    cont = input('Deseja continuar inserindo valores? Y/N\n')

print(vet)
