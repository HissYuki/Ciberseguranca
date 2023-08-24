#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'                                          #localhost = esta máquina
PORT = int(input('digite a porta do servidor: '))           #portas abaixo de 1023 exigem permissão de root

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       ##AF_INET -> IPV4 (AF: Address Family, e.g.: INET6 -> IPV6) // STREAM -> TCP
try:
    s.bind((HOST, PORT))
except:
   print('# erro de bind')
   sys.exit()

s.listen(5)                                                 #Backlog: 5

while True:
    print('aguardando conexoes em ', PORT)
    conn, addr = s.accept()                                 #Conexão e IP:port do cliente que conectou
    print('recebi uma conexao de ', addr)
    while True:
        try:
            data = conn.recv(1024)                          #Servidor dorme até receber uma mensagem do cliente
            print('recebi ', len(data), ' bytes')
        
            if not data:
                print(f'o cliente {addr} saiu')
                break
            print(f'o cliente {addr} transmitiu {data}')
        except Exception as e:                              #Excecão para fechamento forcado do cliente
            print(e)
            print('o cliente foi fechado de maneira forcada')
            break

    print('a conexao foi encerrada')
    conn.close()