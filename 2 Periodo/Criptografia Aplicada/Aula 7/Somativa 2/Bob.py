import socket
import MyHashLib as HL


# CHARLES está interceptando todas as mensagens trocadas entre ALICE e BOB.
# Crie uma estratégia para que ALICE receba a autenticação de usuários pela rede.
# A solução deve ser imune a ataques de REPETIÇÃO (REPLAY)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ALICE = ('127.0.0.1', 9999)

while True:

    login = input('digite seu LOGIN: ')
    senha = input('digite sua SENHA: ')

#------------------------------------------------------------------------------------------------------------
# 1) BOB ENVIA UM HELLO PARA ALICE
# -- não precisa modificar essa seção.

    msg = HL.formataMensagem(['HELLO', login])
    s.sendto( msg, ALICE )
    HL.eavesDropping(msg, 'SEND') # CHARLES OUVIU ESSA MENSAGEM
    print('ENVIEI: ', msg)

#------------------------------------------------------------------------------------------------------------
# 2) BOB RECEBE UM CHALLENGE    
# -- não precisa modificar essa seção.
    data, addr = s.recvfrom(1024) 
    HL.eavesDropping(data, 'RECV') # CHARLES OUVIU ESSA MENSAGEM
    print('RECEBI: ', data)

    msg = HL.separaMensagem(data) 
    if len(msg) < 2 or msg[0] != "CHALLENGE": 
        print('recebi uma mensagem inválida')
        continue

    cs_ALICE = msg[1]

#------------------------------------------------------------------------------------------------------------
# 3) BOB responde ao CHALLENGE com um novo CHALLENGE e o HASH da sua senha 
# -- troque string NONCE por um nonce em formato base64 convertido para string (decode) 
# -- troque o prova_para_ALICE pelo HASH da senha com o challenge da ALICE (cs_ALICE)

    cs_BOB, cs_BOB_b64 = HL.geraNonce(256)
    cs_BOB_str = cs_BOB_b64.decode()
    prova_para_ALICE = HL.calculaHASH(senha + cs_ALICE)

    data = HL.formataMensagem(['CHALLENGE_RESPONSE', cs_BOB_str, prova_para_ALICE[1]]) 

    s.sendto(data, addr )
    HL.eavesDropping(data, 'SEND') # CHARLES OUVIU ESSA MENSAGEM

    print('ENVIEI: ', data)

#------------------------------------------------------------------------------------------------------------
# 4) BOB recebe o resultado da autenticaçao e a prova enviada por ALICE
# -- não precisa modificar essa seção.

    data, addr = s.recvfrom(1024)
    HL.eavesDropping(data, 'RECV') # CHARLES OUVIU ESSA MENSAGEM
    print('RECEBI: ', data)
    msg = HL.separaMensagem(data) 
    resultado = msg[0]
    prova = msg[1]
    print(resultado, prova)


#------------------------------------------------------------------------------------------------------------
# 5) BOB se a senha está correta
# -- é preciso substituir o local_hash pelo hash da senha pelo challenge enviado por BOB (cs_BOB)
    _, local_hash = HL.calculaHASH(senha + cs_BOB_str)

    if resultado == 'SUCCESS' and local_hash == prova:
        print('Este servidor é ALICE')
    else:
        print('Este servidor não é ALICE')

#------------------------------------------------------------------------------------------------------------    
# 6) BOB recebe uma mensagem autenticada de ALICE

    while True:
        print('Aguardando mensagens do Servidor')
        data, addr = s.recvfrom(1024)
        HL.eavesDropping(data, 'RECV') # CHARLES OUVIU ESSA MENSAGEM
        print('RECEBI: ', data)

        msg = HL.separaMensagem(data) 
        if msg[0] == 'HMAC':
            if HL.verificaMensagem(data, senha): 
                print('MENSAGEM VALIDA:', msg[1])          
            else:   
                print('MENSAGEM FALSA:', msg[1])


