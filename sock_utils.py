import socket as s

def create_tcp_server_socket(address, port, queue_size):
    HOST = address 
    PORT = port
    sock_escuta = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock_escuta.listen(queue_size)
    return sock_escuta

def create_tcp_client_socket(address, port):
    HOST = address
    PORT = port
    sock_ligacao = s.socket(s.AF_INET, s.SOCK_STREAM)
    return sock_ligacao
    
#Esta função receberá exatamente lenght bytes através da socket. Devem considerar o caso de a
#socket remota fechar a ligação antes de enviar o número esperado de bytes.
#socket será a socket de ligação para ler os dados.
#lenght determina o número de bytes que devem ser lidos e devolvidos.
#Retorna os bytes recebidos (com tamanho length)