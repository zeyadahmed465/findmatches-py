from tkinter import *
from tkinter import ttk
levels  = {"Easy": 4, "Medium": 6, "Hard": 8}
root = Tk()
root.geometry("200x100")
def onChange(*args):
    global levelchoosen,levell
    print(levels[levelchoosen.get()])
    levell=levels[levelchoosen.get()]
def gett():
        return levell


mainFrame = Frame(root)
mainFrame.pack(fill = BOTH)

# Define the style for combobox widget
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "orange", background= "white")

n=StringVar()
n.trace("w", onChange)

chooselabel=Label(mainFrame,text="choose the level you want?",fg="gray",bg="black").pack()
levelchoosen=ttk.Combobox(mainFrame,width=10,textvar=n)
levelchoosen.pack()
levelchoosen["values"]=[i for i in levels.keys()]
levelchoosen.current(0)
root.mainloop() 


