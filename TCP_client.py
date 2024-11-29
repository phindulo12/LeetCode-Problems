import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#setting up the TCP connection
s.connect(("196.42.71.159" ,1234))
word = "helo world"

s.send(word.encode("utf-8"))

print(s.recv(1024))

s.close()