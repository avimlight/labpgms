import socket
expr=input('enter ann expression')
bytesToSend=str.encode(expr)
localAdressport=("127.0.0.1",20001)
bufferSize=1024

udpClientSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
udpClientSocket.sendto(bytesToSend,localAdressport)
messageFromServer=udpClientSocket.recvfrom(bufferSize)
print(expr,'=',messageFromServer[0].decode())