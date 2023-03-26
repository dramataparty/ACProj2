import socket
from concurrent.futures import ThreadPoolExecutor
import threading

SERVER_ADDRESS = ('localhost', 8888)

POOL_SIZE = 10


def handle_connection(client_socket):
    client_socket.recv(1024)
    mesage = "Test"
    client_socket.sendall(mesage)
    client_socket.close()
    pass



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen()


while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_connection, args=(client_socket))
    thread.start()
    
    



