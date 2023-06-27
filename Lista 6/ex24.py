valid = True
passwd = input('Digite uma senha: ')

if len(passwd) < 10:
    valid = False

cont_special = 0
cont_capital = 0
for i in range(len(passwd)-1):
    if type(passwd[i]) == int and type(passwd[i+1]) == int:
        valid = False
    elif 33 <= ord(passwd[i]) <= 47 or 58 <= ord(passwd[i]) <= 64 or 91 <= ord(passwd[i]) <= 96 or 123 <= ord(passwd[i]) <= 126:
        cont_special += 1
    elif 65 <= ord(passwd[i]) <= 90:
        cont_capital += 1

if cont_special < 2 or cont_capital < 2:
    valid = False

if valid:
    print('Senha válida!')
else:
    print('Senha inválida!')    