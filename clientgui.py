from tkinter import *
from socket import *
from tkinter import messagebox 
#TO CREATE WINDOW :
window = Tk()
window.title('Client gui')
window .geometry("400x300")
en=Entry(window,width=100)
en.grid(row=1,column=1)
s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=8000

def clicked():  
    s.connect((host,port))
    x=en.get()    
    s.send(bytes(x.encode('utf-8')))       
    lbl=Label(window,font=('Helvetica','15'))
    lbl.grid(row=4,column=0)
    lbl["text"]=s.recv(1024).decode('utf-8')
bt=Button(window,text="send",bg="indian red",fg="black",width=3,height=1,font=('Helvetica','15'),command=clicked) 
bt.grid(row=3,column=0) 
window.mainloop()
