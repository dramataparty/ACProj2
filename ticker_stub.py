#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações Distribuídas - Projeto 2 - ticker_client.py
Grupo:52
Números de aluno: 56931, 56922
"""
# imports

import sock_utils as su
import sys, socket as s

# Programa principal

def send_receive(self, data):
    while True:
        msg = str(input('comando >'));
        #validar o comando fornecido
        
        local_commands = []
        serv_commands = []
        if msg in local_commands:
            a = "process"
            #processar
        
        if msg in serv_commands:
            conn_sock = s.socket(s.AF_INET, s.SOCK_STREAM)
            conn_sock.connect((self.address, self.port))
            
            conn_sock.sendall(msg.encode('utf-8'))
            resposta = conn_sock.recv(1024)
            print("resposta: " + resposta.decode())
            conn_sock.close()
        
        if msg == 'EXIT':
            break

        if '' in sys.argv:#caso faltem argumentos
            print("MISSING-ARGUMENTS")

        else:
            print("UNKNOWN-COMMAND")
        #parâmetros linha de comandos


#------------------------------------------------------------------------------
#Implementar isto (stub) com a funcionalidade de cima

import socket, struct , pickle
class ListStub:
    def __init__(self):
        self.conn_sock = socket
    def connect(self, host, port):
        self.conn_sock=socket.connect(host,port)
    # código para estabelecer uma ligação,
    # i.e., tornando self.conn_sock válida
    def disconnect(self):
        self.conn_sock.close()
    # Fecha a ligação conn_sock
    # Métodos tradicionais de um objeto do tipo lista
    def append(self, element):
        pedido = ["ADICIONAR",element]
        self.sendBytes(pedido)
        resposta = self.recieveLista()
        return resposta
        
    def list(self):
        pedido = ["list"]
        self.sendBytes(pedido)
        resposta = self.recieveLista()
        return resposta
        
    def clear(self):
        pedido = ["clear"]
        self.sendBytes(pedido)
        resposta = self.recieveLista()
        return resposta
        
        
    # Outros métodos possíveis
    
    def bytesTolist(bytes):
        lista = []
        resp= pickle.loads(bytes)
        return resp
        pass