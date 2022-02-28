import socket
import time

ip = "127.0.0.1"
# server IP
port = 5678 # server port number
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
t1 = time.time()
s.send(b"hello from from the client")
msg = s.recv(1024)
t2 = time.time()
print("Time taken "+str(t2-t1))
msg = msg.decode("utf-8")
print(msg)
s.close()