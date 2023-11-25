DATA_SIZE=3
msg=input("enter the message")
msg_chunks=[msg[ i : i+DATA_SIZE ] for i in range(0,len(msg),DATA_SIZE)]
frames=list(enumerate(msg_chunks,start=1))
print("fragmneted frames are",frames,"\n")
import random
random.shuffle(frames)
print("unsorted frames are",frames,"\n")
frames.sort()
print("sorted frames are",frames)
print("sorted message is", ''.join([ x[1] for x in frames ]))