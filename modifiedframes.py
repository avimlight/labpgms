# Frame Sorting
DATA_SIZE = 3
msg = input("Enter a message: ")

# Breaks the message into chunks of fixed size
msg_chunks = [msg[i: i + DATA_SIZE] for i in range(0, len(msg), DATA_SIZE)]

# Construct message frames with sequence number
frames = list(enumerate(msg_chunks, start=1))
print("Fragmented frames: ", frames, "\n")

# Shuffles the packets. Simulate the unordered receiving of packets.
import random
random.shuffle(frames)
print('Unordered frames received: ', frames, "\n")
 
# Implementing Bubble Sort for sorting frames based on sequence number
n = len(frames)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if frames[j][0] > frames[j + 1][0]:
            frames[j], frames[j + 1] = frames[j + 1], frames[j]

print('Sorted frames using Bubble Sort: ', frames, "\n")
print('Sorted message: ' + ''.join([x[1] for x in frames]), "\n")
