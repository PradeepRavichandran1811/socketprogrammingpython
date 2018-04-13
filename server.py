import socket
import os
#socket programming using TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#binds the IP address with the port 8008
server.bind(('127.0.0.1', 8008))
#server listens for connections
server.listen(5)
#pass socket object and address to the accept() function
connection, address = server.accept()

if connection:
    print ("Client has been Connected")
    mode = connection.recv(1024).decode()
    connection.send('Received Mode'.encode())
    #code for upload operation
    if mode == "upload":
        f = open("Server/upload1.txt", "w+")
        f.write(connection.recv(1024).decode())
        f.flush()
        connection.send("File has been Uploaded Successfully")
    #code for download operation
    if mode == "download":
        f = open(os.path.relpath(connection.recv(1024).decode()))
        connection.send(f.read(1024).encode())
        connection.send("File has been Downloaded Successfully".encode())
        f.close()
    #code for delete operation
    if mode == "delete":
        connection.send("File Deleted Successfully".encode()
                        if not os.remove(os.path.relpath(connection.recv(1024).decode()))
                        else "File Deletion failed".encode())
    #code for rename operation
    if mode == "rename":
        arg = connection.recv(1024).decode()
        arg = arg.split(",")
        connection.send("File Renamed Successfully".encode()
                        if not os.rename(os.path.relpath(arg[0]), os.path.relpath(arg[1]))
                        else "File Rename failed".encode())