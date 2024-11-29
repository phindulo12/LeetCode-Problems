import socket


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("196.42.71.159",1234))

while True:
    try:
        data,addr = s.recvfrom(1024)
        print(f"data received from {addr}")

        newText = data.decode("utf-8").upper()

        s.sendto(newText.encode("utf-8"), addr)
    except Exception as e:
        print(e)
        break

s.close()

