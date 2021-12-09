from tkinter import *
from constants import setLevel
menu=Tk()
menu.title=("Our Menu")
menu.geometry("900x500")
menu.config(background="gray")



label1=Label(menu,text="WELCOME TO OUR MATCHING GAME!!",bg="gray",font=("Arial",20),height=3,pady=5,padx=5)
label1.pack()
def dele():
    menu.destroy()
def open_game(l):
    menu.destroy()
    setLevel(l)
    import findMatches
def score():
    pass    


open=Button(menu,command=lambda: open_game(6),text='Letꞌs Start 6',width=40,height=2,borderwidth=0)
open.place(x=300,y=140)
open=Button(menu,command=lambda: open_game(4),text='Letꞌs Start 4',width=40,height=2,borderwidth=0)
open.place(x=300,y=200)

scores=Button(menu,command=score,text='Playerꞌs Score',width=40,height=2,borderwidth=0)
scores.place(x=300,y=240)

close=Button(menu,command=dele,text='Exit Game',width=40,height=2,borderwidth=0)
close.place(x=300,y=340)

menu.mainloop()