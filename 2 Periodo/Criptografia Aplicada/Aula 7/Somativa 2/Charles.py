import socket
import MyHashLib as HL

ALICE = ('127.0.0.1', 9999)
BOB = None

print('ESTA TELA PERTENCE A CHARLES')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(HL.CHARLES)

cliente = []
servidor = []

def EavesDropping():

    while True:   
        data, addr = s.recvfrom(1024) 
        global BOB 
        
        BOB = addr

        msg = HL.separaMensagem(data)
        print('ESCUTEI: ', msg)

        tipo = msg[-1]
        msg.pop()
        data = HL.formataMensagem(msg)

        if tipo == 'SEND':  
            cliente.append(data) 
        else:
            servidor.append(data)
               
        if msg[0] == 'HMAC':
            break

        

def ReplayAttack():
    global BOB
    print(BOB)

    for m in cliente:
        s.sendto(m, ALICE)
        print('Enviei: ', m)
        data, addr = s.recvfrom(1024)
        msg = HL.separaMensagem(data)
        print('Recebi: ', msg)

    try:
        s.settimeout(5)
        print('Aguardando a mensagem: ')
        data, addr = s.recvfrom(1024)
        msg = HL.separaMensagem(data)
        print('Recebi: ', msg)
    except:
        print('A autenticação falhou')
    finally:
        if BOB is not None:           
            s.settimeout(None)
            print('Tentando duplicar a ultima mensagem enviada pelo servidor ...')
            print(servidor[-1])
            for i in range(3):
                s.sendto(servidor[-1], BOB)
        

while True:
    print('Iniciando escuta ...')
    EavesDropping()
    input('Digite <ENTER> para fazer o REPLAY ATTACK')
    ReplayAttack()
    break







