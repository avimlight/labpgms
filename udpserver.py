import socket
import re
localip="127.0.0.1"
localport=20001
bufferSize=1024
udpserversocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
udpserversocket.bind((localip,localport))
print("\n listenming to the server\n")
while True:
    byteAdressPair=udpserversocket.recvfrom(bufferSize)
    expression=byteAdressPair[0].decode()
    clientadress=byteAdressPair[1]
    num1,num2=re.split('\+|-|\*|/|%',expression.replace(' ', ''))
    num1=float(num1)
    num2=float(num2)
    result=0
    if '+' in expression:
        result=num1+num2
    elif '-' in expression:
        result=num1-num2
    elif '*' in expression:
        result=num1*num2
    elif '/' in expression:
        if num2==0:
            result='Division by zero'
        else:
            result=num1/num2
    elif '%' in expression:
        result=num1%num2
    print('equation from the client is ',expression,":",clientadress)
    print("result to the client is",result)
    udpserversocket.sendto(str(result).encode(),clientadress)    
        