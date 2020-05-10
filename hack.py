import sys
import socket
import string
import itertools

args = sys.argv

host = args[1]
port = int(args[2])


client_socket = socket.socket()

address = (host, port)

client_socket.connect(address)

alpha = string.ascii_lowercase
digits = string.digits
chain = list(itertools.chain(alpha, digits))

found_pass = "Not found"
for i in itertools.count(1, 1):
    for pas_tuple in list(itertools.product(chain, repeat=i)):
        pas = ''.join(pas_tuple)
        client_socket.send(pas.encode())
        response = client_socket.recv(1024)
        response = response.decode()
        if response == "Connection success!":
            found_pass = pas
            break
        if response == "Too many attempt":
            found_pass = "Too many attempt"
            break
    else:
        continue
    break

print(found_pass)

client_socket.close()
