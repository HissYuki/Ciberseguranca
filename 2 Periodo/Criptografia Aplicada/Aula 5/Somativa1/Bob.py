import socket
import time
import RSALib as RSA
import AESLib as AES

ipServidor = '127.0.0.1'
portaServidor = 9999
destino = (ipServidor, portaServidor)

print('ESTA TELA PERTENCE A BOB')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Neste loop BOB tenta contato com Alice
while True:
    # Tenta contato com Alice
    s.sendto('HELLO'.encode(), destino )
   
    print('Aguardando chave pública ...')

    try:
        chavePubPEM, addr = s.recvfrom(1024) 
        print('Recebi uma chave pública')
        print('Chave Publica:', chavePubPEM)
        break
    except:
        print('Alice não responde!')
        time.sleep(5)


try:

    # 1) BOB RECEBE A CHAVE PÚBLICA DE ALICE
    #   -- é preciso converter a chave de base64 para o objeto do Python
    chavePubObj = RSA.converteChavePublica(chavePubPEM)

    # 2) BOB GERA UMA CHAVE SECRETA ALEATÓRIA
    chavesecreta, chavesecreta_pem = AES.geraChave(128)

    # 3) BOB CRIPTOGRAFA A CHAVE SECRETA (EM BYTES) COM A CHAVE PÚBLICA DA ALICE
    #  -- observe que não deve usar a opção byte e não a PEM
    
    chaveCifrada = RSA.cifraComPublica(chavesecreta, chavePubObj)

    # 4) BOB ENVIA A CHAVE SECRETA CRIPTOGRAFADA PARA ALICE
    #    -- é preciso trocar a string CHAVECIFRADA pela chave secreta criptografada em formato base64 (remova o encode())

    s.sendto(chaveCifrada, destino )
    print(f'Enviei uma chave secreta para {addr}')
    print('Chave Cifrada:', chaveCifrada)

    # 5) BOB DESCRIPTOGRAFA UMA MENSAGEM CIFRADA DA ALICE
    # -- é preciso descriptografar o ciphertext e salvar em plain text!!!
    ciphertext, addr = s.recvfrom(1024) 
    print(f'Recebi uma mensagem cifrada de {addr}')
    print('Ciphertext:', ciphertext)

    plaintext = AES.decifraMensagem(ciphertext, chavesecreta)

    #------------------------------------------------
    # SE VOCE FEZ TUDO CERTO A MENSAGEM DA ALICE VAI SER IMPRESSA AQUI
    print('Plaintext:', plaintext)

except Exception as e:
    print(e)

# ATENCAO: A entrega desta atividade são as mensagens que aparecem na tela do BOB
# -- As chaves são aleatórias então duas equipes não podem ter as mesmas chaves
# -- Faça um COPY-AND-PAST das mensagens que aparecem no terminal de BOB e cole em um arquivo texto para postar o trabalho




