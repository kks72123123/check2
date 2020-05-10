import sys
import socket

args = sys.argv

host = args[1]
port = int(args[2])
command = args[3]

client_socket = socket.socket()

address = (host, port)

client_socket.connect(address)

data = command.encode()

client_socket.send(data)

response = client_socket.recv(1024)

response = response.decode()
print(response)

client_socket.close()
