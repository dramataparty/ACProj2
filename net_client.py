"""
Aplicações Distribuídas - Projeto 2 - net_client.py
Grupo: 52
Números de aluno: 56931,56922
"""

# zona para fazer importação

import sock_utils as su
import sys, socket as s

# definição da classe server_connection 

class server_connection:
    def __init__(self, address, port):
        
        if len(sys.argv) > 1:
            self.address , self.port = s.getsockname()   
            su.create_tcp_client_socket(address, port)
        else:
            su.create_tcp_client_socket('127.0.0.1',9999)
    
    def connect(self):
        conn_sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        conn_sock.connect((self.address, self.port))
        return conn_sock

    def send_receive(self, data):
        conn_sock = server_connection.connect(self)
        while True:
            msg = str(input('comando >'))
            if msg == 'EXIT':
                break
            conn_sock.sendall(msg.encode('utf-8'))
            resposta = conn_sock.recv(1024)
            print("resposta: " + resposta.decode())
            
    def close(self):
        s.close()    