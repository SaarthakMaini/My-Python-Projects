import socket
port=3000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#create a socket object
CHUNK = 65535#recieve at most this bytes of data at once
#socket.socket(family,type)
#AF_NET: family of ipv4 ip address
#SOCK_DGRAM: UDP, SOCK_STREAM:TCP
print(s)
#It tells us that this is a socket object, the port IP address is this (0.0.0.0) and port is 0
#some ip address that the server will listen to when message comes
hostname='127.0.0.1'
#ip address of local machine, same for everyone, localhost

#So, for now any traffic which comes on this localhost and port 3000, I have to find through the socket

s.bind((hostname,port))
print(f"server is live on{s.getsockname()}")

# run this server infinitely till I stop manually
while True:
    data,clientAdd=s.recvfrom(CHUNK)
    #when this socket recieves data from the client , then this method is called , it is listening infinitely
    message=data.decode('ascii')# because data by default travels in bytes
    print(f"Saarthak at {clientAdd} Says:{message}")
    message_send=input("Reply:")
    data=message_send.encode('ascii')
    #send the data to the ip add that sent the data
    s.sendto(data,clientAdd)