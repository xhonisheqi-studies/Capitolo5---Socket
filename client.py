import socket
import sys

HOST = sys.argv[1]
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.sendall(b'Hello, World')

data = s.recv(4096)
# while True:
#     chunk = s.recv(4096)
#     if not chunk: 
#         break
#     data += chunk

data_decoded = data.decode('ISO-8859-1')
print(data_decoded)

s.close()






