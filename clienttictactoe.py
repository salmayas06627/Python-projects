from tkinter import *
from tkinter import messagebox 
from socket import *
import threading
s=socket(AF_INET,SOCK_STREAM)
window = Tk()
window.title('client side')
window .geometry("400x300")
#=======================================
#to create labels:
lbl1=Label(window,text="Game : Tic-tac toe ",font=('Helvetica','15'))
lbl1.grid(row=0,column=0)
lbl1=Label(window,text="Player2",font=('Helvetica','15'))
lbl1.grid(row=2,column=0)
#=======================================
def clicked1( f= False ):
    global c
    if not f:
       if btn1["text"]==" ":
          btn1["text"]='x'
       s.send(b"a")
    elif btn1["text"]==" ":
       btn1["text"]='o'  
    check()       
def clicked2(f= False):
   if not f:
       if btn2["text"]==" ":
          btn2["text"]='x'
       s.send(b"b")
   elif btn2["text"]==" ":
       btn2["text"]='o' 
   check()
def clicked3(f= False):
   if not f:
       if btn3["text"]==" ":
          btn3["text"]='x'
       s.send(b"c")
   elif btn3["text"]==" ":
       btn3["text"]='o'
   check()
def clicked4(f= False):
    if not f:
        if btn4["text"]==" ":
          btn4["text"]='x'
        s.send(b"d")
    elif btn4["text"]==" ":
       btn4["text"]='o'       
    check()
def clicked5(f= False):
   if not f:
       if btn5["text"]==" ":
          btn5["text"]='x'
       s.send(b"e")
   elif btn5["text"]==" ":
       btn5["text"]='o'        
   check()
def clicked6(f= False):
    if not f:
        if btn6["text"]==" ":
           btn6["text"]='x'
        s.send(b"f")
    elif btn6["text"]==" ":
       btn6["text"]='o'
    check()       
def clicked7(f= False):
    if not f:
        if btn7["text"]==" ":
           btn7["text"]='x'
           s.send(b"g")
    elif btn7["text"]==" ":
       btn7["text"]='o'
    check()       
def clicked8(f= False):
    if not f:
        if btn8["text"]==" ":
           btn8["text"]='x'
        s.send(b"h")
    elif btn8["text"]==" ":
       btn8["text"]='o'  
    check()
def clicked9(f= False):
    if not f:
        if btn9["text"]==" ":
           btn9["text"]='x'
        s.send(b"i")
    elif btn9["text"]==" ":
       btn9["text"]='o'
    check()
#=================
def receive_thread(s):
    while True:
        x=s.recv(2048).decode('utf-8')
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
#====================================
Flag=1
def check():
    global Flag 
    Flag=Flag+1
    b1=btn1["text"] 
    b2=btn2["text"] 
    b3=btn3["text"] 
    b4=btn4["text"] 
    b5=btn5["text"] 
    b6=btn6["text"] 
    b7=btn7["text"] 
    b8=btn8["text"] 
    b9=btn9["text"] 
    if b1==b2 and b2==b3 and b1=='x' or b1==b2 and b2==b3 and b1=='o':
        win(b1)
    if b4==b5 and b5==b6 and b4=='x' or b4==b5 and b5==b6 and b4=='o':
        win(b4) 
    if b7==b8 and b8==b9 and b7=='x' or b7==b8 and b8==b9 and b7=='o':
        win(b7)
    if b1==b4 and b4==b7 and b1=='x' or b1==b4 and b4==b7 and b1=='o':
        win(b1) 
    if b2==b5 and b5==b8 and b2=='x' or b2==b5 and b5==b8 and b2=='o':
        win(b2)
    if b3==b6 and b6==b9 and b3=='x' or b3==b6 and b6==b9 and b3=='o':
        win(b3)     
    if b1==b5 and b5==b9 and b1=='x' or b1==b5 and b5==b9 and b1=='o':
        win(b1)        
    if b3==b5 and b5==b7 and b3=='x' or b3==b5 and b5==b7 and b3=='o':
        win(b3)      
    if Flag==10:
        messagebox.showinfo("","Game is finished")
        window.destroy()
#==================================================
def win(player):
   if(player=="x"):
      messagebox.showinfo("","Congratulation Player1") 
      window.destroy()
   else:
      messagebox.showinfo("","Congratulation Player2") 
      window.destroy() 
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
#==============================
host="127.0.0.1"
port=9000
s.connect((host,port))
receive=threading.Thread(target=receive_thread,args=(s,))
receive.start()   
window.mainloop()
