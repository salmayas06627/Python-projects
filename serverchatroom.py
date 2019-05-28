from socket import*
from _thread import*
import threading
#====================
def sendmessegetoall(messege,thisclient):
    for client in clients:
        if client!=thisclient:
            client.send(messege.encode('utf-8')) 
#====================
def connectnewuser(c,addr):
    while True:
      m=c.recv(2048)
      m=addr[0]+':'+m.decode('utf-8')
      sendmessegetoall(m,c)		
#====================
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET , SO_REUSEADDR, 1)
host="127.0.0.1"
port=7005
s.bind((host,port))
s.listen(5)
clients=[]
while True:
    con,addr=s.accept()
    clients.append(con)
    start_new_thread(connectnewuser,(con,addr))
     
