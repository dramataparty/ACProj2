#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações Distribuídas - Projeto 1 - ticker_server.py
Grupo: 52
Números de aluno: 56931, 56922
"""

# Zona para fazer importação

###############################################################################

import sock_utils as su
import sys, socket as s


###############################################################################

# código do programa principal
class resource:
    def __init__(self, resource_id):
        su.create_tcp_server_socket(self.address, self.port);
        self.resource_id=resource_id
        pass # Remover esta linha e fazer implementação da função

        def subscribe(self, client_id, time_limit):
            return resource_pool.subscribe(self, client_id, time_limit)
            pass # Remover esta linha e fazer implementação da função

        def unsubscribe (self, client_id):
            return resource_pool.unsubscribe(self, client_id)
            pass # Remover esta linha e fazer implementação da função

        def status(self, client_id):
            return resource_pool.status(self, client_id)
            pass # Remover esta linha e fazer implementação da função

        def __repr__(self):
            output = ""
            # R <resource_id> <list of subscribers>

            return output



class resource_pool:
    subs = {}
    
        
    def __init__(self, N, K, M):
        self.N = N
        self.K = K
        self.M = M
    pass # Remover esta linha e fazer implementação da função

    def clear_expired_subs(self):
        subs = {}
    pass # Remover esta linha e fazer implementação da função

    def subscribe(self, resource_id, client_id, time_limit):
        if(client_id not in resource_pool.subs):
            resource_pool.subs.update({resource_id:client_id})
            return 'OK'
        elif(client_id in resource_pool.subs):
            return 'NOK'
        else:
            return 'UNKNOWN RESOURCE'
            
    
    pass # Remover esta linha e fazer implementação da função

    def unsubscribe (self, resource_id, client_id):
        if(client_id in resource_pool.subs):
            resource_pool.subs.pop({resource_id:client_id})
            return 'OK'
        elif(client_id not in resource_pool.subs):
            return 'NOK'
        else:
            return 'UNKNOWN RESOURCE'
    pass # Remover esta linha e fazer implementação da função

    def status(self, resource_id, client_id):
        if({resource_id:client_id} in resource_pool.subs):
            
            return 'SUBSCRIBED'
        if ({resource_id:client_id} not in resource_pool.subs):
            return 'UNSUBSCRIBED'
        else:
            return 'UNKNOWN RESOURCE'
    pass # Remover esta linha e fazer implementação da função

    def infos(self, option, client_id):
        if option=="M":
            subbed = []
            for i in resource_pool.subs:
                if client_id in i:
                    subbed.append({i})
                    
            return subbed #lista de elementos subscritos
        elif option=="K":
            return #<número de ações que cliente ainda pode subscre-ver>
    pass # Remover esta linha e fazer implementação da função

    def statis(self, option, resource_id):
        if option=="L":
            if resource_id not in resource_pool.subs:
                return 'UNKNOWN RESOURCE'
        elif option=="ALL":
            return len(resource_pool.subs)#numero coisas
    pass # Remover esta linha e fazer implementação da função

   
    
    cmds = {'SUBSCR': subscribe,
            'CANCEL':unsubscribe,
            'STATUS':status ,
            'INFOS': infos ,
            'STATIS': statis }
    
    def process(line):
        cmd, *args = line.split()
        return cmds[cmd](*args)
    
    def __repr__(self):
        output = ""
        output += process(msg) + '\n'
        # Acrescentar no output uma linha por cada recurso
        return output



