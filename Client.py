import socket, time, os                # Import socket module

s = socket.socket()             # Create a socket object
host = '000.000.000.000'     # Get local machine name
port = 6000                     # Reserve a port for your service.
s.connect((host, port))     #Connects host and port to server
prompt = s.recv(1024)           #Receives username prompt
username = raw_input(prompt)    #Prompts username
s.send(username)                #Sends username
passprompt = s.recv(1024)       #Receives password prompt
password = raw_input(passprompt)#Prompts password
s.send(password)                #Sends password

command = ""
    # s.send("Hello server!")
    
#Loops while not quitting to get the commands
while command != "quit":        
    time.sleep(1)
    commandList = s.recv(1024)
    command = raw_input(commandList)
    s.send(command)

    
    if command == "dir":
        data = s.recv(1024)
        print data
         
    elif command == "cd":
        data = s.recv(1024)
        print data
         
    elif command == "ls":
        data = s.recv(1024)
        print data
     
    elif command == "get":
        data = s.recv(1024)
        with open('received_file1.txt', 'wb') as f:
            print 'file opened'
            f.write(data)
        f.close()
         
    elif command == "put":
        with open('received_file1.txt', 'rb') as f:
            l = f.read(1024)
            while (l):
                s.send(l)
#                 print('Sent ',repr(l))
                l = f.read(1024)
#                 print(l)
        f.close()
         
    elif command == "mget":
        data = s.recv(1024)
        with open('received_file1.txt', 'wb') as f:
            print 'file opened'
            f.write(data)
        f.close()
        time.sleep(1)
        data = s.recv(1024)
        with open('received_file2.txt', 'wb') as f:
            print 'file opened'
            f.write(data)
        f.close()
        
        
    elif command == "mput":
        rootDir = '.'
        for root, dirs, files in os.walk(rootDir):
    #         time.sleep(1)
            for file in files:
                time.sleep(1)
                if file.endswith(".txt"):
                    f = open(file,'rb')
                    l = f.read(1024)
                    while (l):
                        s.send(l)
#                         print('Sent ',repr(l))
                        l = f.read(1024)
                    f.close()
                else:
                    print ""
                    
    elif command == "quit":
        s.close()
         
             
    
# s.close()
    



