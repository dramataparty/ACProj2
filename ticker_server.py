#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações Distribuídas - Projeto 2 - ticker_server.py
Grupo: 52
Números de aluno: 56931, 56922
"""

# Zona para fazer importação

###############################################################################

import sock_utils as su
import sys, socket as s
import select as sel
import threading 
import time


###############################################################################

# código do programa principal
class resource:
    def __init__(self, resource_id):
        su.create_tcp_server_socket(self.address, self.port);
        self.resource_id=resource_id
        pass # Remover esta linha e fazer implementação da função

    def subscribe(self, client_id, time_limit):
        return self.subscribe(self, client_id, time_limit)

    def unsubscribe (self, client_id):
        return resource_pool.unsubscribe(self, client_id)

    def status(self, client_id):
        return resource_pool.status(self, client_id)

    def __repr__(self):
        output = ""
        
        # R <resource_id> <list of subscribers>

        return output



class resource_pool:   
    def __init__(self, N, K, M):
        self.subs = {}
        self.N = N
        self.K = K
        self.M = M
        self.N, self.K, self.M = sel.select(SocketList, [], [])
             
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)

        SocketList = [sock]
        while True:
            R, W, X = sel.select(SocketList, [], [])
            for s in R:
                if s is sock: 
                    conn_sock, (addr, port) = sock.accept()
                    SocketList.append(conn_sock)
                else: 
                    s.close() 
                    SocketList.remove(s)
                    print('Cliente fechou ligação')
            pass

    global msg



# Remover esta linha e fazer implementação da função

    def clear_expired_subs(self):
        delay = self.time_limit
        while True:
            time.sleep(delay)
            now = time.time()
            self.subs[:] = [elem for elem in self.subs if now - elem[1] < delay]

    def subscribe(self, resource_id, client_id, time_limit):
        self.time_limit = time_limit
        if(client_id not in self.subs):
            self.subs.update({resource_id:client_id})
            return 'True'
        elif(client_id in self.subs):
            return 'False'
        else:
            return 'None'

    def unsubscribe (self, resource_id, client_id):
        if(client_id in self.subs):
            self.subs.pop({resource_id:client_id})
            return 'True'
        elif(client_id not in self.subs):
            return 'False'
        else:
            return 'None'

    def status(self, resource_id, client_id):
        if({resource_id:client_id} in self.subs):
            
            return 'SUBSCRIBED'
        if ({resource_id:client_id} not in self.subs):
            return 'UNSUBSCRIBED'
        else:
            return 'None'

    def infos(self, option, client_id):
        if option=="M":
            subbed = []
            for i in self.subs:
                if client_id in i:
                    subbed.append({i})
                    
            return subbed #lista de elementos subscritos
        elif option=="K":
            
            return #<número de ações que cliente ainda pode subscre-ver>

    def statis(self, option, resource_id):
        if option=="L":
            if resource_id not in self.subs:
                return 'None'
        elif option=="ALL":
            return len(self.subs)#numero coisas



    global cmds 
    cmds = {'SUBSCR': subscribe,
            'CANCEL':unsubscribe,
            'STATUS':status ,
            'INFOS': infos ,
            'STATIS': statis }
    global process
    def process(line):
       
        cmd, *args = line.split()
        
        return cmds[cmd](*args)
    
    def __repr__(self):
        output = ""
        output += process(msg) + '\n'
        # Acrescentar no output uma linha por cada recurso
        return output
