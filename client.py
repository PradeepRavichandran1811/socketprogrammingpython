import socket
#upload operation function
def upload(directory, conn):
    conn.send(open(directory, "rb").read())
    print (conn.recv(1024).decode())
#download operation function
def download(directory, conn):
    f = open("Client/download1.txt", "w+")
    conn.sendall(directory.encode())
    f.write(conn.recv(1024).decode())
    print (conn.recv(1024).decode())
    f.flush()
    f.close()
#delete operation function
def delete(directory, conn):
    conn.send(directory.encode())
    print (conn.recv(1024).decode())

#rename operation function
def rename(old_name, new_name, conn):
    conn.send(str(old_name+","+new_name).encode())
    print (conn.recv(1024).decode())

if __name__ == "__main__":
    #prompting the user to select a File operation to perform
    mode = input("Enter the File Operation to be Performed \n upload\n download\n delete\n rename\n")
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #establishing connection with server using port 8008
    connection.connect(('127.0.0.1', 8008))
    connection.sendall(mode.encode())
    print (connection.recv(1024).decode())
    if mode == "upload":
        upload(input('Enter file path:'.encode()), connection)

    elif mode == "download":
        download(input('Enter File Name that needs to be downloaded:'.encode()), connection)

    elif mode == "delete":
        path = input('Enter file path to be deleted')
        delete(path, connection)

    elif mode == "rename":
        rename(input('Enter the source file name(old name):'),
               input('Enter the source file name(new name):'), connection)
