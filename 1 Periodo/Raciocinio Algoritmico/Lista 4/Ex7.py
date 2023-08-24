### 7. Escreva um programa que imprima os n primeiros números da sequência de Fibonacci.

n = int(input('Digite um número inteiro: '))

ant = 0
fib = 1
cont = 0

while(cont < n):
    if(cont == 0):
        print(ant)
    elif(cont == 1):
        print(fib)
    else:
        aux = fib
        fib = fib + ant
        ant = aux
        print(fib)
    cont += 1
