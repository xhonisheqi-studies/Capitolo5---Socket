import socket
import sys

# host su cui connettersi che in questo caso siamo noi
HOST = '127.0.0.1'
# una porta casuale sopra le 10000 -- mai sotto 1024 in quanto ci sono altri servizi
PORT = 50007
# dominio che dobbiamo cercare e lo mandiamo tramite argv nel terminale
domain_to_search = sys.argv[1]

# creiamo il socket del client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connettiamoci
s.connect((HOST,PORT))
# inviamo il dominio al server
s.sendall(domain_to_search.encode('utf-8'))

data = b''
while True:
    chunk = s.recv(4096)
    if not chunk: break
    data += chunk
# riceviamo al response 
data_decoded = data.decode('ISO-8859-1')
print(data_decoded)

# chiudiamo la sessione del socket
s.close()






