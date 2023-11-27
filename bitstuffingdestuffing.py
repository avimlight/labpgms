def destuffing(ipbits):
    frames=[]
    frame=''
    zerocount=0
    onecount=0
    for bit in ipbits:
        if bit=='0' and zerocount==1 and onecount==6:
            zerocount=0
            onecount=0
            frame=frame[:-7]
            if frame:
                frames.append(frame)
                frame=''
        elif bit=='0'  and onecount==5:
            zerocount=0
            onecount=0
        else:
            frame+=bit
            if bit=='0':
                zerocount=1
                onecount=0
            else:
                onecount+=1
    frames.append(frame)
    return frames


def stuffing(msg):
    stuffing_msgs=[]
    for msgs in msg:
        onecount=0
        stuffingmsg=''
        for bit in msgs:
            stuffingmsg+=bit
            if bit=='0':
                onecount=0
            else:
                onecount+=1
                if onecount==5:
                    stuffingmsg+='0'
                    onecount=0
        stuffing_msgs.append(stuffingmsg)
    return stuffing_msgs

def framing(stuffmsg):
    flag='01111110'
    frame=''
    for msg in stuffmsg:
        frame+=flag+msg
    return frame

nofmessages=int(input('enter the number of messages  '))
messages=[]
for i in range(1,nofmessages+1):
    messages.append(input('enter the %d frame bits' %i))
    
stuffed_msg=stuffing(messages)

for i,msg in enumerate(stuffed_msg,start=1):
    print("the stufffed msg ",i,':',msg)
    
frames=framing(stuffed_msg)
print('output frames is',frames)

unstuffed_msg=destuffing(frames)

for i,msg in enumerate(unstuffed_msg,start=1):
    print(" mesage",i,":",msg)
    
    
    
    
    
            
                  
              
    