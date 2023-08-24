phrase = "Ola mundo!"
p_inv = []

for i in range(0, len(phrase)):
    if 65 <= ord(phrase[i]) <= 90:
        p_inv.append(chr(ord(phrase[i]) + 32))
    elif 97 <= ord(phrase[i]) <= 122:
        p_inv.append(chr(ord(phrase[i]) - 32))  
    else:
        p_inv.append(phrase[i])      

print("".join(p_inv))