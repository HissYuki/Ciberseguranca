from socket import socket, AF_INET, SOCK_DGRAM
import MyHashLib as HL


# CHARLES está interceptando todas as mensagens trocadas entre ALICE e BOB.
# Crie uma estratégia para que ALICE receba a autenticação de usuários pela rede.
# A solução deve ser imune a ataques de REPETIÇÃO (REPLAY)


# ALICE tem uma base de senhas cadastradas
# -- ALICE não deve salvar as senhas em plain-text
# -- E mais: ALICE não deve conhecer a senha dos usuários em plain-text!!!

senhas = {
    'BOB' : 'SEGREDO',
    'MOE' : 'SENHA',
    'LARRY' : 'OPA',
    'CURLY' : 'YAHOO'
}


print('ESTA TELA PERTENCE A ALICE')

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 9999))

while True:

#------------------------------------------------------------------------------------------------------------
# 1) ALICE AGUARDA UM PEDIDO DE LOGIN
# -- não precisa modificar essa seção

    print('Aguardando solicitação de LOGIN ...')
    
    data, addr = s.recvfrom(1024) 
    print('RECEBI: ', data)
    msg = HL.separaMensagem(data)  # mensagem esperada: [ 'HELLO', 'USUARIO' ]

    if len(msg) < 2 or msg[0] != 'HELLO': 
        print('recebi uma mensagem inválida')
        continue
    else:
        user = msg[1]
        user_addr = addr
        if user not in senhas.keys():
            print('Usuario desconhecido')
            continue

#------------------------------------------------------------------------------------------------------------
# 2) ALICE responde ao HELLO com um CHALLENGE 
# -- troque string NONCE por um nonce em formato base64 convertido para string (decode)

    nonce, nonce_b64 = HL.geraNonce(256)
    cs_ALICE = nonce_b64.decode()
    data = HL.formataMensagem(['CHALLENGE', cs_ALICE])

    s.sendto(data, addr )
    print('ENVIEI: ', data)

#------------------------------------------------------------------------------------------------------------
# 3) ALICE recebe a resposta do CHALLENGE
# -- não precisa modificar essa seção.

    data, addr = s.recvfrom(1024) # mensagem esperada: ['CHALLENGE_RESPONSE', 'NONCE', 'HASH_SENHA' ]
    print('RECEBI: ', data)

    if addr != user_addr:
        print('mensagem de origem desconhecida')
        continue

    msg = HL.separaMensagem(data) 

    if len(msg) < 3 or msg[0] != 'CHALLENGE_RESPONSE': 
        print('ERRO DE PROTOCOLO!!!')
        continue
    else:
        cs_BOB = msg[1]
        hash_BOB = msg[2]

#------------------------------------------------------------------------------------------------------------    
# 4) ALICE verifica se a senha está correta
# -- e preciso calcular o local_HASH usando a CHALLENGE da Alice
# -- substitua PROVA_PARA_BOB pelo hash calculado com a senha de BOB e o challenge enviado por BOB

    local_HASH = HL.calculaHASH(senhas[user] + cs_ALICE)

    if hash_BOB == local_HASH[1]:
        resposta = 'SUCCESS'
        print(f'Este usuário é {user}')
    else:
        resposta = 'FAIL'
        print(f'Ataque detectado: Pedido de LOGIN NEGADO!!!')
        continue    # ATENCAO: remova essa linha para fazer o teste de repetição do HMAC

    _, prova_para_BOB = HL.calculaHASH(senhas[user] + cs_BOB)

    msg = HL.formataMensagem([resposta, prova_para_BOB])
    
    s.sendto(msg, addr )
    print('ENVIEI: ', msg)

#------------------------------------------------------------------------------------------------------------
# 5) ALICE envia uma mensagem assinada para BOB
# -- não precisa modificar essa seção.


    msg = f'OLA {user}, VOCE SE AUTENTICOU COM SUCESSO.'

    data = HL.assinaMensagem(msg, senhas[user]) 
    s.sendto(data, addr )     
    print('ENVIEI: ', data)



