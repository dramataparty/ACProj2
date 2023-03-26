#Adaptar para este projeto 


import pickle
from Stub import ListStub

class ListSkeleton:
    def __init__(self):
        self.servicoLista = []
    def processMessage(self, msg_bytes) :
        pedido = ListStub.bytesToList(msg_bytes)
        resposta = []
        if pedido == None or len(pedido) == 0 :
            resposta.append('INVALID MESSAGE')
        else :
            if pedido[0] == 'append' and len(pedido) > 1 :
                self.servicoLista.append(pedido[1])
                resposta.append('True')
            elif pedido[0] == 'list' :
                resposta.append(str(self.servicoLista))
            elif pedido[0] == 'clear' :
                self.servicoLista = []
                resposta.append('True')
            else :
                resposta.append('INVALID MESSAGE')
        return ListSkeleton.listToBytes(self, resposta)
    
#outros métodos possíveis    
    def listToBytes(self, msg):
                mess = pickle.dumps(msg)
                con = self.conn_sock
                con.sendall(mess)
                return mess
            
        