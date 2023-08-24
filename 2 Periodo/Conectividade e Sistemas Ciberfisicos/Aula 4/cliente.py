#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'                                          #IP do servidor
PORT = int(input('digite a porta do servidor: '))                                                 #Porta do servidor         

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except:
   print('# erro de conexao')
   sys.exit()

while True:
    try:
        line = input('digite a mensagem e <ENTER> ')
        if not line:
            print('linha vazia encerra o programa')
            break
    except:
        print('programa abortado com CTRL+C')
        break

    data = bytes(line, 'utf-8')
    
    try:
        tam = s.send(data)
    except Exception as e:
        print(e)
        print('o servidor foi fechado de maneira forcada')
        break

    print(f'enviei {tam} bytes')
    print(data)