import socket

#setting up the IP address of the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Address = "196.42.71.159"
port = 1234

s.bind((Address, port))

s.listen(5)


#The server is always on host
while True:
    try:
        client_Socket,address = s.accept()
        print(f"connected on {address}")

        data = client_Socket.recv(1024).decode("utf-8")

        data = data.upper()
        
        client_Socket.sendall(data.encode("utf-8"))
    except:
        print("failed to connect")

s.close()
                            







