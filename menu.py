from tkinter import *
from constants import setLevel


menu=Tk()
menu.geometry("1050x500")
menu.title("Our Game")
menu.config(background="#102027")
def dele():
    menu.destroy()
def open_game(l):
    menu.destroy()
    setLevel(l)
    import findMatches
def score():
    menu.destroy()
    import menuscore   
label1=Label(menu,text="EA sports, It's in the game!",bg='#102027',font=("Arial",20),height=3,pady=45,padx=45,activeforeground = '#12005e',
            activebackground = "yellow",fg='white')
label1.pack(side='top')
B1 = Button(menu, text = "Start new game (EASY)",command=lambda: open_game(4),
                activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e",
                fg = "white", width = 50, font = 'summer',bd='5')
B1.place(x=400,y=250)
B4 = Button(menu, text = "Start new game (HARD)",command=lambda: open_game(8),
                activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e",
                fg = "white", width = 50, font = 'summer',bd='5')
B4.place(y=280)
B2 = Button(menu, text = "Score board",command=lambda:score(), activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e", fg = "white",
                width = 50, font = 'summer', bd = 5)
B2.place(y=210)
B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e", fg = "white",
                width = 50, font = 'summer', bd = 5)
B3.place(y=220)
B1.pack(side = 'top')
B4.pack(side = 'top')
B2.pack(side = 'top')
B3.pack(side = 'top')
menu.mainloop()
