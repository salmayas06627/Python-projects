from tkinter import *
from socket import *
from _thread import *
import threading 
#=======================
def receive_thread(c):
    while True:
        lbl["text"]=c.recv(1024) 
#=======================
def client_thread(c):
    receive=threading.Thread(target=receive_thread,args=(c,))
    receive.start()
    while True:
        x=en.get()    
        c.send(bytes(x.encode('utf-8'))) 
#=======================
#TO CREATE WINDOW :
window = Tk()
window.title('Server gui')
window.geometry("400x300")
en=Entry(window,width=100)
en.grid(row=1,column=1)
lbl=Label(window,font=('Helvetica','15'))
lbl.grid(row=2,column=0)
#========================
s=socket(AF_INET,SOCK_STREAM)  
host="127.0.0.1"
port=8000
s.bind((host,port))      
s.listen(5)
c,ad=s.accept()
while True:
     start_new_thread(client_thread,(c,))
window.mainloop()