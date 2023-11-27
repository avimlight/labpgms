import socket
HOST="127.0.0.1"
PORT=5000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    filename=input("enter the filename")
    s.connect((HOST,PORT))
    print('Connected to the ',HOST)
    s.sendall(filename.encode())
    print("filename sent")
    data=s.recv(1024).decode()
    if(data.startswith('File not found')):
        print(f'Reqquested file {filename} is not found in the server {HOST}')
    else:
        print(f'Requested file name {filename}')
        with open("d"+filename,'w') as f:
            while True:
                f.write(data)
                if not data:
                    break
                data=s.recv(1024).decode()
            print('done')
        s.close()    
                   
            

