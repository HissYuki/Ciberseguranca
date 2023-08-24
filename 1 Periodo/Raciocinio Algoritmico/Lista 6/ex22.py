phrase = input('Digite uma frase: ')
cont_space = 0
cont_capital = 0
cont_special = 0


for i in range(len(phrase)):
    if ord(phrase[i]) == 32:
        cont_space += 1
    elif 65 <= ord(phrase[i]) <= 90:
        cont_capital += 1
    elif 33 <= ord(phrase[i]) <= 47 or 58 <= ord(phrase[i]) <= 64 or 91 <= ord(phrase[i]) <= 96 or 123 <= ord(phrase[i]) <= 126:
        cont_special += 1

print(cont_space, cont_capital, cont_special)
