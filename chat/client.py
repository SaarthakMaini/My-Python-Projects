import socket
port=3000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# instead of explicitly binding the socket, I will let OS do it
# we will be using ephemeral ports
#Os will bind this for 
hostname='127.0.0.1'#server to which I have to send data

while True:
    s.connect((hostname,port))
    message=input("Type message:")
    data=message.encode("ascii")
    s.send(data)
    #data recieved
    CHUNK=65535
    data=s.recv(CHUNK)
    text=data.decode('ascii')
    print(f"Papa says {text}")
