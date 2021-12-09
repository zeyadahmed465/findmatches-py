
import tkinter
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("calculator")
def sent():
    pass
def yes(yesB, noB, l):
    yesB.destroy()
    noB.destroy()
    noB.destroy()

    e=Entry(top)
    e.grid(row=5,column=1,columnspan=2,padx=10,pady=5)
    l1=Label(top,text="Enter you name")
    l1.grid(row=4,column=1,columnspan=2,padx=10,pady=5)
    submit=Button(top,text="submit",font=("Arial",20),command=sent)
    submit.grid(row=6,column=1,columnspan=2,padx=10,pady=5)

def no() :
    top.destroy()
    root.destroy()

def pop():
    score=1000-500 #must be modified
    global top
    global yes_button
    global no_button
    top =Toplevel()
    top.title("well done you win !!")
    top.geometry("300x350")
    l1=Label(top,text=f"Congratulations you got {score} ",font=("Arial",14))
    l1.grid(row=1,column=1,columnspan=2,padx=10,pady=5)
    label_cong=Label(top,text="Do you want to save this score",font=("Arial",14))
    label_cong.grid(row=2,column=1,columnspan=2,padx=10,pady=5)
    yes_button=Button(top,text="yes",command=lambda: yes(yes_button, no_button, label_cong),width=10,font=("Arial",10))
    yes_button.grid(row=3,column=1,padx=10,pady=5)
    no_button= Button(top, text="no", command=no,width=10,font=("Arial",10))
    no_button.grid(row=3, column=2,padx=10,pady=5)





b1=Button(root,text="click",command=pop)
b1.pack()


mainloop()