import socket
from concurrent.futures import ThreadPoolExecutor

SERVER_ADDRESS = ('localhost', 8888)

POOL_SIZE = 10


def handle_connection(client_socket):
    
    
    pass



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen()


while True:
    client_socket, client_address = server_socket.accept()
