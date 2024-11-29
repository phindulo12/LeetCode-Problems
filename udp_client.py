import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Message and address
message = "hello world!"
message = message.encode("utf-8")
address = ("196.42.71.159", 1234)

# Send the message to the address
s.sendto(message, address)

# Receive response from the server
data, server = s.recvfrom(1024)  # Buffer size is 1024 bytes
data = data.decode("utf-8")
print(data)

# Close the socket
s.close()
