from socket import*
from _thread import *
import threading
s=socket(AF_INET,SOCK_STREAM)
#========================
def receive_thread(s):
    while True:
        x=s.recv(1024)
        print(x.decode('utf-8'))
#======================    
host="127.0.0.1"
port=8000
s.connect((host,port))
while True:
    receive=threading.Thread(target=receive_thread,args=(s,))
    receive.start()
    s.send(input("client text: ").encode('utf-8'))
    
