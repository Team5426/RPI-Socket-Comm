import socket

host = 'localhost' # UPDATE THIS TO PROPER IP OF RASPBERRY PI
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:

    command = input("-> ")

    if command == 'EXIT':

        s.send(str.encode(command))

        break

    elif command == 'KILL':

        s.send(str.encore(command))

        break;

    s.send(str.encore(command))

    reply = s.recv(1024) # Adjust buffer if necessary

    print(reply.decode('utf-8'))

s.close()
