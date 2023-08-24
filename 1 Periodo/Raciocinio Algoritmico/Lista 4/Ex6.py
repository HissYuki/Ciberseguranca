### 6. Escreva um programa que solicite um número inteiro e calcule a soma de seus dígitos.

n = int(input('Digite um número inteiro: '))

aux = 1
sum = 0

while(n // aux != 0):
    aux *= 10

aux /= 10

while(aux >= 1):
    sum = sum + (n // aux)
    n = n - (n // aux) * aux
    aux /= 10

print(f'A soma dos dígitos do número é {sum}')