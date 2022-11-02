import socket

#select a server port
server_port = 12000

#create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind the server to the localhost at port server_port
server_socket.bind(('',server_port))

print('UDP Server running on port ', server_port)

#Now the loop that listens from clients
#As UDP is not connection oriented,the same UDP socket serves all clients

while True:
    #cadd below is the client process address
    cmsg, cadd = server_socket.recvfrom(2048)
    cmsg = cmsg.decode()
    client_port = cadd[1] #accessing the client's port number from the tupple data type CADD
    if (client_port == 11000):
        print("Client 1: " + cmsg)
    elif (client_port == 13000):
        print("Client 2: " + cmsg)
    else:
        print("External Client:", cadd, ":" + cmsg)    

    if(cmsg.isalnum()==False):
        cmsg = "Not Alphanumeric."
    else:
        cmsg = "Alphanumeric."

    #send reply message to the client process            
    server_socket.sendto(cmsg.encode(),cadd)

