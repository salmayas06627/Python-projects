from socket import*
from _thread import*
import threading
#====================
s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port= 7005
s.connect((host, port)) 
#==================
def receive(s):
   x=s.recv(2048)
   print(x)
#==================
while True: 
    start_new_thread(receive, (s,))  
    s.send(bytes(input("client:").encode('utf-8')))