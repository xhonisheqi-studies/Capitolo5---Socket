import socket

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # prevebt address already in use
s.bind((HOST,PORT))
s.listen(5)


while True: 
    client_socket,addr = s.accept()
    data = b''

    data = client_socket.recv(4096)
    client_socket.sendall(data)
    client_socket.close()

