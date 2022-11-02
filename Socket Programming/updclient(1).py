import socket
#the server name and port client wishes to access
server_name = "localhost"
server_port = 12000
#create a UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('',11000))

print("UDP client running...")
print("Connecting to server at IP: ", server_name, " PORT: ", server_port)

#take input from the user
msg = input("Enter a string to test if it is alphanumeric: ")

#send the message to the udp server
client_socket.sendto(msg.encode(),(server_name, server_port))

#return values from the server
msg, sadd = client_socket.recvfrom(2048)

#show output and close client
print(msg.decode())
client_socket.close()
