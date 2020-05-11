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

file = open("passwords.txt", "r")
passwords = file.read().splitlines()
file.close()

found_pass = "Not found"

for password in passwords:
    for pas in map(''.join, itertools.product(*((c.upper(), c.lower()) for c in password))):
        client_socket.send(pas.encode())
        response = client_socket.recv(1024)
        response = response.decode()
        if response == "Connection success!":
            found_pass = pas
            break
    else:
        continue
    break

print(found_pass)

client_socket.close()
