import socket

# host da bindare
HOST = ''
# una porta casuale sopra le 10000 -- mai sotto 1024 in quanto ci sono altri servizi
PORT = 50007
# porta di default per servizio HTTP
HTTP_PORT = 80

# creaiamo il socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # prevebt address already in use
# bind di host e server
s.bind((HOST,PORT))
# impostiamolo in modalità ascolto
s.listen(1)


while True: 
    # accettiamo la connessione
    client_socket,addr = s.accept()
    # riceviamo il domain da parte del client
    domain = client_socket.recv(4096).decode('utf-8').strip()
    # creiamo un socket per la richiesta sulla porta 80 da parte del client
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((domain,HTTP_PORT))
    # componiamo la richiesta 
    request = f'GET / HTTP/1.1\r\nHost: {domain}\r\nConnection: close\r\n\r\n'
    # mandiamo la response al server socket
    remote_socket.sendall(request.encode('utf-8'))

    response = b''
    while True:
        chunk = remote_socket.recv(4096)
        if not chunk: break
        response += chunk
    # chiudiamo il remote socket
    remote_socket.close()
    # madimao la respone al client socket
    client_socket.sendall(response)
    # chiudiamo la sessione del client socket
    client_socket.close()