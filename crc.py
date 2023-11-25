

def getcrc(msg):
    reg=[0]*17
    
    for bit in msg:
        reg.pop(0)
        reg.append(int(bit))
        if reg[0]:
            reg[0] ^=1
            reg[4] ^=1
            reg[11] ^=1
            reg[16] ^=1
    return ''.join([str(x) for x in reg[1:]])  

print("sender")
msg=input("enter the binary msg")
msg_ext=msg + '0' * 16 
crc=getcrc(msg_ext)
msg=msg+crc
print("the computed crc is ",crc,"\nthe message is",msg)

print("reciever")
msg=input("enter the recieved message")
crc=getcrc(msg)
print("the crc is ",crc)
print("error in transmission "if int(crc,base=2) else "no error in transmission" )
            
    
    
