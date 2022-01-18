import socket, os, time                 # Import socket module

port = 6000                     # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = '0.0.0.0'     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
path = "C:\Users\FTPClient"
directory = "C:\Users\FTPServer"

print 'Server listening....'

# retrieve the current directory function
def dir():
    currentDir = os.getcwd()
    print('Directory', currentDir)
    return currentDir

# List the current directory function
def ls():
    currentDir = os.getcwd()
    listDir = os.listdir(currentDir)
    return str(listDir)
    
# change the current directory function   
def cd():
    os.chdir(path)
    changedDir = os.getcwd()
    return changedDir

# send a file from the host machine to the local machine function
def get():
    filename='Test1.txt'
    f = open(filename,'rb') # opens the file on the hose machine
    l = f.read(1024)    # reads the opened file
    while (l):
        conn.send(l)    #sends the file to the local machine
#         print('Sent ',repr(l))
        l = f.read(1024)
    f.close()
    return l

# send a file from the local machine to the host machine function
def put():
    with open('Test1.txt', 'wb') as f:
        print 'file opened'
        info = conn.recv(1024)  #receives the file from the host
        f.write(info) # writes the received file to the current open file
#         print(info)
        f.close()
        return info

# send multiple files from the host machine to the local machine function
def mget():
    rootDir = '.'
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if file.endswith(".txt"):
                f = open(file,'rb')
                l = f.read(1024)
                while (l):
                    conn.send(l)
#                     print('Sent ',repr(l))
                    l = f.read(1024)
                f.close()
            else:
                print ""
        return l

# send multiple files from the local machine to the host machine function
def mput():
    data = conn.recv(1024)
    with open('Test1.txt', 'wb') as f:
        print 'file opened'
        f.write(data)
    f.close()
    time.sleep(1)
    data = conn.recv(1024)
    with open('Test2.txt', 'wb') as f:
        print 'file opened'
        f.write(data)
    f.close()
    return data



# list of commands for the local machine to choose to execute
functionDict = {'cd', 'dir', 'ls', 'get', 'put', 'mget', 'mput', 'quit'}


while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    conn.send("Please enter Username")  #sends username prompt to local machine
    username = conn.recv(1024)
    conn.send("Please enter Password")  #sends password prompt to local machine
    password = conn.recv(1024)
    print(username, '********')
    while conn:
        conn.send(str(functionDict))    #sends list of commands to local machine
        data = conn.recv(1024)
        print('Server receiver', repr(data))
          
        #receives local machine commands and executes command
        if data == "dir":
            command = dir()
            conn.send(command)
        elif data == "cd":
            command = cd()
            conn.send(command)
        elif data == "ls":
            command = ls()
            conn.send(command)
        elif data == "get":
            command = get()
            conn.send(command)
        elif data == "put":
            command = put()
            conn.send(command)
        elif data == "mget":
            command = mget()
            time.sleep(1)
            conn.sendall(command)
        elif data == "mput":
            command = mput()
            conn.send(command)
        elif data == "quit":
            conn.close()
         

    




