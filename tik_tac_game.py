from tkinter import *
from tkinter import messagebox
con=False
ctr=1
player1=0
player2=0
root=Tk()
root.geometry("500x500")
root.title("Tik tak tak Game")
p1_score=StringVar()
p2_score=StringVar()
def press(btn):
    global con,ctr
    if  btn["text"]==" " and con==False:
        con=True
        btn["text"]="X"
        check()
        ctr+=1
    elif btn["text"]==" " and con==True:
        con=False
        btn["text"]="O"
        check()
        ctr+=1  
def clearbutton():
    button1["text"]=" " 
    button2["text"]=" "
    button3["text"]=" " 
    button4["text"]=" " 
    button5["text"]=" " 
    button6["text"]=" " 
    button7["text"]=" " 
    button8["text"]=" "
    button9["text"]=" "        
def check():
    global player1,player2,p1_score,p2_score,ctr
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
       button1["text"]=="X"and button4["text"]=="X" and button7["text"]=="X" or
       button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
       button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
       button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
       button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
       button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
       button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        #clearbutton()  
        messagebox.showinfo("Tic Tac Toe Game", " Congrats Player1 Win!")
        ctr=0
        player1+=1
        p1_score.set(player1) 
    elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
       button1["text"]=="O"and button4["text"]=="O" and button7["text"]=="O" or
       button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
       button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
       button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
       button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
       button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
       button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        #clearbutton()
        messagebox.showinfo("Tic Tac Toe Game", " Congrats Player2 Win!")
        ctr=0
        player2+=1
        p2_score.set(player2)  
    elif ctr==8:
         messagebox.showinfo("Tic Tac Toe Game", "its a draw!")
                         
button1=Button(text=" ",font=" Times  15 bold",bg="yellow",height=3,width=8,command=lambda:press(button1))
button1.grid(column=1,row=1)
button2=Button(text=" ",font=" Times  15 bold",bg="yellow",height=3,width=8,command=lambda:press(button2))
button2.grid(column=2,row=1)
button3=Button(text=" ",font=" Times  15 bold",bg="yellow",height=3,width=8,command=lambda:press(button3))
button3.grid(column=3,row=1)
button4=Button(text=" ",font=" Times  15 bold",bg="yellow",height=3,width=8,command=lambda:press(button4))
button4.grid(column=1,row=2)
button5=Button(text=" ",font=" Times  15 bold",bg="yellow",height=3,width=8,command=lambda:press(button5))
button5.grid(column=2,row=2)
button6=Button(text=" ",font=" Times  15 bold",bg="yellow",height=3,width=8,command=lambda:press(button6))
button6.grid(column=3,row=2)
button7=Button(text=" ",font=" Times  15 bold",bg="yellow",height=3,width=8,command=lambda:press(button7))
button7.grid(column=1,row=3)
button8=Button(text=" ",font=" Times  15 bold",bg="yellow",height=3,width=8,command=lambda:press(button8))
button8.grid(column=2,row=3)
button9=Button(text=" ",font=" Times  15 bold",bg="yellow",height=3,width=8,command=lambda:press(button9))
button9.grid(column=3,row=3)
label=Label(text="Player1 = X " ,bg="white",fg="black",font="Garamond 15 italic")
label.grid(row=0,column=0)
label2=Label(text="Player2 = O",bg="white",fg="black",font="Garamond 15 italic")
label2.grid(row=1,column=0)
label3=Label(text="Player1 Score",font="Areal 10 bold")
label3.grid(row=4,column=2)
p1=Entry(textvariable=p1_score,width=5)
p1.grid(row=4,column=3)
label4=Label(text="Player1 Score",font="Areal 10 bold")
p2=Entry(textvariable=p2_score,width=5)
p2.grid(row=5,column=3)
label4.grid(row=5,column=2)
button11=Button(text="Play Again",bg="yellow",fg="black",borderwidth=0,font="Areal 15 bold",height=2,width=10,command=clearbutton)
button11.grid(row=6,column=2,columnspan=3)
root.mainloop()