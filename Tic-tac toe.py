from tkinter import *
from tkinter import messagebox 
#TO CREATE WINDOW :
window = Tk()
window.title('Tic-tac toe')
window .geometry("400x300")
#=======================================
#to create labels:
lbl1=Label(window,text="Game : Tic-tac toe ",font=('Helvetica','15'))
lbl1.grid(row=0,column=0)
lbl1=Label(window,text="Player1: X",font=('Helvetica','15'))
lbl1.grid(row=1,column=0)
lbl1=Label(window,text="Player2: O",font=('Helvetica','15'))
lbl1.grid(row=3,column=0)
#=======================================
#to define functions :
Turn=1
def clicked1():
    global Turn
    if btn1["text"]==" ":
        if Turn==1:
            Turn=2
            btn1["text"]='X'
        else:
            Turn=1
            btn1["text"]='O'
        check()    
def clicked2():
    global Turn
    if btn2["text"]==" ":
        if Turn==1:
            Turn=2
            btn2["text"]='X'
        else:
            Turn=1
            btn2["text"]='O' 
        check()     
def clicked3():
    global Turn
    if btn3["text"]==" ":
        if Turn==1:
            Turn=2
            btn3["text"]='X'
        else:
            Turn=1
            btn3["text"]='O'
        check()   
def clicked4():
    global Turn
    if btn4["text"]==" ":
        if Turn==1:
            Turn=2
            btn4["text"]='X'
        else:
            Turn=1
            btn4["text"]='O'
        check()    
def clicked5():
    global Turn
    if btn5["text"]==" ":
        if Turn==1:
            Turn=2
            btn5["text"]='X'
        else:
            Turn=1
            btn5["text"]='O'
        check()    
def clicked6():
    global Turn
    if btn6["text"]==" ":
        if Turn==1:
            Turn=2
            btn6["text"]='X'
        else:
            Turn=1
            btn6["text"]='O'
        check()    
def clicked7():
    global Turn
    if btn7["text"]==" ":
        if Turn==1:
            Turn=2
            btn7["text"]='X'
        else:
            Turn=1
            btn7["text"]='O'
        check()    
def clicked8():
    global Turn
    if btn8["text"]==" ":
        if Turn==1:
            Turn=2
            btn8["text"]='X'
        else:
            Turn=1
            btn8["text"]='O'
        check()    
def clicked9():
    global Turn
    if btn9["text"]==" ":
        if Turn==1:
            Turn=2
            btn9["text"]='X'
        else:
            Turn=1
            btn9["text"]='O' 
        check()    

#=================
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
    if b1==b2 and b2==b3 and b1=='X' or b1==b2 and b2==b3 and b1=='O':
        win(b1)
    if b4==b5 and b5==b6 and b4=='X' or b4==b5 and b5==b6 and b4=='O':
        win(b4) 
    if b7==b8 and b8==b9 and b7=='X' or b7==b8 and b8==b9 and b7=='O':
        win(b7)
    if b1==b4 and b4==b7 and b1=='X' or b1==b4 and b4==b7 and b1=='O':
        win(b1) 
    if b2==b5 and b5==b8 and b2=='X' or b2==b5 and b5==b8 and b2=='O':
        win(b2)
    if b3==b6 and b6==b9 and b3=='X' or b3==b6 and b6==b9 and b3=='O':
        win(b3)     
    if b1==b5 and b5==b9 and b1=='X' or b1==b5 and b5==b9 and b1=='O':
        win(b1)        
    if b3==b5 and b5==b7 and b3=='X' or b3==b5 and b5==b7 and b3=='O':
        win(b3)      
    if Flag==10:
        messagebox.showinfo("","Game is finished")
        window.destroy()
#================
def win(player):
   if(player=="X"):
      messagebox.showinfo("","Congratulation Player1") 
      window.destroy()
   else:
      messagebox.showinfo("","Congratulation Player2") 
      window.destroy() 
#==================================================
#to create buttons :
btn1=Button(window,text=" ",bg="indian red",fg="white",width=3,height=3,font=('Helvetica','15'),command=clicked1) 
btn1.grid(row=1,column=1)     
btn2=Button(window,text=" ",bg="indian red",fg="white",width=3,height=3,font=('Helvetica','15'),command=clicked2)
btn2.grid(row=1,column=2)
btn3=Button(window,text=" ",bg="indian red",fg="white",width=3,height=3,font=('Helvetica','15'),command=clicked3)
btn3.grid(row=1,column=3)
btn4=Button(window,text=" ",bg="indian red",fg="white",width=3,height=3,font=('Helvetica','15'),command=clicked4)
btn4.grid(row=2,column=1)
btn5=Button(window,text=" ",bg="indian red",fg="white",width=3,height=3,font=('Helvetica','15'),command=clicked5)
btn5.grid(row=2,column=2)
btn6=Button(window,text=" ",bg="indian red",fg="white",width=3,height=3,font=('Helvetica','15'),command=clicked6)
btn6.grid(row=2,column=3)
btn7=Button(window,text=" ",bg="indian red",fg="white",width=3,height=3,font=('Helvetica','15'),command=clicked7)
btn7.grid(row=3,column=1)
btn8=Button(window,text=" ",bg="indian red",fg="white",width=3,height=3,font=('Helvetica','15'),command=clicked8)
btn8.grid(row=3,column=2)
btn9=Button(window,text=" ",bg="indian red",fg="white",width=3,height=3,font=('Helvetica','15'),command=clicked9)
btn9.grid(row=3,column=3)
window.mainloop()