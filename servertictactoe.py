from tkinter import *
from _thread import *
import threading
from socket import *
from tkinter import messagebox 
#======================================
#TO CREATE WINDOW :
window = Tk()
window.title('server side')
window .geometry("400x300")
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET , SO_REUSEADDR, 1)
#=======================================
#to create labels:
lbl1=Label(window,text="Game : Tic-tac toe ",font=('Helvetica','15'))
lbl1.grid(row=0,column=0)
lbl1=Label(window,text="Player1",font=('Helvetica','15'))
lbl1.grid(row=2,column=0)
#=======================================
#to define functions :
global c
def clicked1( f= False ):
    if not f:
         if btn1["text"]==" ":
            btn1["text"]='o'
         c.send(b"a")       
    elif btn1["text"]==" ":
       btn1["text"]='x'             
def clicked2(f= False):
   if not f:
       if btn2["text"]==" ":
          btn2["text"]='o'
       c.send(b"b")
   elif btn2["text"]==" ":
       btn2["text"]='x' 
def clicked3(f= False):
   if not f:
       if btn3["text"]==" ":
          btn3["text"]='o'
       c.send(b"c")
   elif btn3["text"]==" ":
       btn3["text"]='x'
def clicked4(f= False):
    if not f:
        if btn4["text"]==" ":
           btn4["text"]='o'
        c.send(b"d")
    elif btn4["text"]==" ":
       btn4["text"]='x'       
def clicked5(f= False):
   if not f:
       if btn5["text"]==" ":
          btn5["text"]='o'
       c.send(b"e")
   elif btn5["text"]==" ":
       btn5["text"]='x'        
def clicked6(f= False):
    if not f:
        if btn6["text"]==" ":
           btn6["text"]='o'
        c.send(b"f")
    elif btn6["text"]==" ":
       btn6["text"]='x'      
def clicked7(f= False):
    if not f:
        if btn7["text"]==" ":
           btn7["text"]='o'
        c.send(b"g")
    elif btn7["text"]==" ":
       btn7["text"]='x'      
def clicked8(f= False):
    if not f:
        if btn8["text"]==" ":
           btn8["text"]='o'
        c.send(b"h")
    elif btn8["text"]==" ":
       btn8["text"]='x'  
def clicked9(f= False):
    if not f:
        if btn9["text"]==" ":
           btn9["text"]='o'
        c.send(b"i")
    elif btn9["text"]==" ":
       btn9["text"]='x'
#============================
def receive_thread(c):
    while True:
        x=c.recv(2048).decode('utf-8')
        print(x)
        if(x=="a"):
               clicked1(True)           
        elif(x=="b"):
            clicked2(True)
        elif(x=="c"):
            clicked3(True)
        elif(x=="d"):
            clicked4(True)          
        elif(x=="e"):
            clicked5(True)
        elif(x=="f"):
            clicked6(True)
        elif(x=="g"):
            clicked7(True)
        elif(x=="h"):
            clicked8(True)
        elif(x=="i"):
            clicked9(True)
#==================================================
#to create buttons :
btn1=Button(window,text=" ",bg="indian red",fg="white",width=5,height=2,font=('Helvetica','15'),command=clicked1) 
btn1.grid(row=1,column=1)     
btn2=Button(window,text=" ",bg="indian red",fg="white",width=5,height=2,font=('Helvetica','15'),command=clicked2)
btn2.grid(row=1,column=2)
btn3=Button(window,text=" ",bg="indian red",fg="white",width=5,height=2,font=('Helvetica','15'),command=clicked3)
btn3.grid(row=1,column=3)
btn4=Button(window,text=" ",bg="indian red",fg="white",width=5,height=2,font=('Helvetica','15'),command=clicked4)
btn4.grid(row=2,column=1)
btn5=Button(window,text=" ",bg="indian red",fg="white",width=5,height=2,font=('Helvetica','15'),command=clicked5)
btn5.grid(row=2,column=2)
btn6=Button(window,text=" ",bg="indian red",fg="white",width=5,height=2,font=('Helvetica','15'),command=clicked6)
btn6.grid(row=2,column=3)
btn7=Button(window,text=" ",bg="indian red",fg="white",width=5,height=2,font=('Helvetica','15'),command=clicked7)
btn7.grid(row=3,column=1)
btn8=Button(window,text=" ",bg="indian red",fg="white",width=5,height=2,font=('Helvetica','15'),command=clicked8)
btn8.grid(row=3,column=2)
btn9=Button(window,text=" ",bg="indian red",fg="white",width=5,height=2,font=('Helvetica','15'),command=clicked9)
btn9.grid(row=3,column=3)
#============================================
host="127.0.0.1"
port=9000
s.bind((host,port))
s.listen(5)
c,ad=s.accept() 
receive=threading.Thread(target=receive_thread,args=(c,))
receive.start()
window.mainloop()