import socket
from time import sleep

SERVER = "127.0.0.1"

pass_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pass_client.connect((SERVER, 7438))
pass_client.recv(2000)

help_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
help_client.connect((SERVER, 7438))

pass_client.sendall(b'pass lolz\n')
help_client.sendall(b'help goodboy\n')

sleep(0.3)
print(pass_client.recv(1024).decode())
