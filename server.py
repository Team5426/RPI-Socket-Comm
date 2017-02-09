import socket

host = ''
port = 5560

stored = ""

def setupServer():
    
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print('Socket created with host ' + str(host) + ' on port ' + str(port) + '!')

    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)

    print ('Socket bind complete')

    return s


def setupConnection():
    
    s.listen(1)

    connection, address = s.accept()

    print("Connected to: " + address[0] + ":" + str(address[1]))

    return connection

def GET():
    
    reply = 'Test Successful'
    
    return reply

def REPEAT(dataMessage):
    
    reply = dataMessage[1]

    return reply
    

def transfer(connection):

    while True:
        data = connection.recv(1024) # Change buffer size if needed
        data = data.decode('utf-8')
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]

        if command == 'TEST':
            
            reply = GET()
            
        elif command == 'REPEAT':
            
            reply = REPEAT(dataMessage)

        elif command == 'EXIT':
            
            print("Connection terminated")
            
            break;

        elif command == 'KILL':
            
            print("Server shutting down")
            
            s.close()
            
            break

        else:
            
            reply = 'Unknown Command'

        connection.sendall(str.encore(reply))
        
        print("Data sent")
        
    connection.close()


s = setupServer()


while True:
    try:
        connection = setupConnection()
        dataTransfer(connection)
    except:
        break;
