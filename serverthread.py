from socket import*
from _thread import *
import threading 
#=======================
def receive_thread(c):
    while True:
        x=c.recv(500)
        print(x.decode('utf-8'))
#=======================
def client_thread(c):
    receive=threading.Thread(target=receive_thread,args=(c,))
    receive.start()
    while True:
        c.send(input("enter text:").encode('utf-8'))
#=======================
s=socket(AF_INET,SOCK_STREAM)  
host="127.0.0.1"
port=8000
s.bind((host,port))      
s.listen(5)
while True:
    c,ad=s.accept()
    print("connection from:",ad[0])
    start_new_thread(client_thread,(c,))