from tkinter import *
from constants import setLevel


menu=Tk()
menu.geometry("1050x500")
menu.title("Our Game")
menu.config(background="black")
def dele():
    menu.destroy()
def open_game(l):
    menu.destroy()
    setLevel(l)
    import findMatches
def score():
    pass   
label1=Label(menu,text="EA sports,Im in the game!",bg='black',font=("Arial",20),height=3,pady=45,padx=45,activeforeground = 'red',
            activebackground = "yellow",fg='white')
label1.pack(side='top')
B1 = Button(menu, text = "Start new game",command=lambda: open_game(1),
                activeforeground = 'red',
                activebackground = "yellow", bg = "red", 
                fg = "yellow", width = 50, font = 'summer',bd='5')
B1.place(x=400,y=250)
B2 = Button(menu, text = "Score board",command=lambda:score(), activeforeground = 'red',
                activebackground = "yellow", bg = "red", fg = "yellow",
                width = 50, font = 'summer', bd = 5)
B2.place(y=210)
B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red',
                activebackground = "yellow", bg = "red", fg = "yellow",
                width = 50, font = 'summer', bd = 5)
B3.place(y=220)
B1.pack(side = 'top')
B2.pack(side = 'top')
B3.pack(side = 'top')
menu.mainloop()
