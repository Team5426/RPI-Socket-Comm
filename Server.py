import socket
import sys
import random

host = ''
port = 5426

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

try:
    s.bind((host, port))
except socket.error as msg:
    print("Failed to bind! Error code: " + str(msg[0]))
    sys.exit()

print("Socket bind successful")

s.listen(1)
print("Listening...")

conn, addr = s.accept()

while True:
    print("Connected with " + addr[0] + ":" + str(addr[1]))

    message = "Unknown command";

    data = conn.recv(4096)

    r = lambda: random.randint(0, 255)

    if data == 'GET':
        message = str(r()) + "," + str(r()) + "," + str(r())

    conn.sendall(message)

conn.close()
