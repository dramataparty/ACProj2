"""
Aplicações Distribuídas - Projeto 1 - net_client.py
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
            self.address = address
            self.port = port   
            su.create_tcp_client_socket(address, port);
        else:
            su.create_tcp_client_socket('127.0.0.1',9999);
    pass # Remover esta linha e fazer implementação da função
    

    def connect(self):
        s.connect((self.address, self.port))
    pass # Remover esta linha e fazer implementação da função

    def send_receive(self, data):
        while True:
            msg = str(input('comando >'));
            s.sendall(msg.encode('utf-8'))
            resposta = s.recv(1024)
            print("resposta: " + resposta.decode())
            if msg == 'EXIT':
                break
                
    pass # Remover esta linha e fazer implementação da função

    def close(self):
        s.close()    
    pass # Remover esta linha e fazer implementação da função



