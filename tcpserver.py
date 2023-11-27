import socket,os
HOST="localhost"
PORT=5000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)
    while True:
        print("waiting for the clients information\n")
        conn,addr=s.accept()
        with conn:
            print("conn from",addr)
            while True:
                filename=conn.recv(1024).decode()
                if not filename:
                    break
                print('requested filename',filename)
                if not os.path.exists(filename):
                    print("file not found")
                    conn.sendall(b'file not found')
                else:
                    with open(filename) as f:
                        conn.sendall(f.read().encode())
                    print("the file is transmitted")
                    break
            print("closing this connection")     
                    
                
                        
                        
                        
    
    
    
    