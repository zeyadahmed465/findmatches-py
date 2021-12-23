from tkinter import *
from constants import getLevel
import random
import time

level = getLevel()

root = Tk()
root.geometry("500x{}".format(level * 40 + 150))
root.config(background="#102027")

if level > 14:
    level = 14
elif level % 2:
    level -=1




global winner, matches, tries


#def recent_scores(info):
#    scores_list.insert(END, info)
    

def score_calc():
    global winner, tries,m , s
    return  int( 1000 * level * winner / (tries * (s + (m)*60)) )

def time_taken():
    global m, s
    return (s + (m)*60)

winner, tries = 0,0
back_photo = PhotoImage(file="img/back.png")

matches = [PhotoImage(file=f"img/pic{i}.png") for i in range(1,level +1)] * 2
random.shuffle(matches)

my_frame = Frame(root)
my_frame.pack(pady=10)




#define our buttons
buttonList = [Button(my_frame, text=" ",
                    font=("Helvetica", 20), image = back_photo, 
                        relief="groove") for _ in range(level*2)]


rows = level // 2 

#define our winner counter

#define some variables
count = 0
answer_list = []
answer_dict = {}

#variables for clock function
m,s,stop = 0,0,0
time1 = int(time.strftime("%H"))*3600 + int(time.strftime("%M")) *60 + int(time.strftime("%S"))
#reset the game
def retrun2menu():
    root.destroy()
    import menu
def reset():
    global matches, winner, stop, time1, tries
    winner =0
    tries = 0
    time_label.config(text="00:00")
    correct_label.config(text="correct : 0")
    tries_label.config(text="tries : 0")
    #reset our tiles 
    
    for button in buttonList:
        button.config(image= back_photo, state="normal")
    time1 = int(time.strftime("%H"))*3600 + int(time.strftime("%M")) *60 + int(time.strftime("%S"))
    random.shuffle(matches)
    stop = 0
    clock()
    

#creating the timer
def clock():
    if stop!= 0:
        return 
    global time1, m, s
    current_time = int(time.strftime("%H"))*3600 + int(time.strftime("%M")) *60 + int(time.strftime("%S"))
    current_time = current_time - time1
    s = current_time % 60
    m = current_time // 60
    time_label.config(text="{:02d}:{:02d}".format(m,s))
    time_label.after(1000, clock)

#creating the winner function
    

#function for clicking buttons
def button_click(b, number):
    global count, answer_list, answer_dict, winner, stop, tries
    if b["text"] == ' ' and count < 2 :
        b["image"] = matches[number]


        #add number to answer_list
        answer_list.append(number)
        #add button with its text to the answer_dic
        answer_dict[b] = matches[number]
        #Increment the count
        count += 1
    #start to determine correct or not
    if len(answer_list) == 2:
        tries += 1
        tries_label.config(text=f"tries : {tries}")
        keys = list(answer_dict.keys())

        if len(keys) == 2 and matches[answer_list[0]] == matches[answer_list[1]]:
            
            #disalbe the buttons
            for button in answer_dict: # each button will be the key which is the Button()
                button["state"] = "disabled"
            #resitting our variables
            answer_dict = {}
            answer_list = []
            count = 0
            #increment our winner
            winner += 1 
            correct_label.config(text=f"correct : {winner}" )
            if winner == len(buttonList)/2:
                stop = 1
                clock()
                from popUp import pop
                pop()
                #win()
        else:
            #my_label.config(text="try again!")
            answer_list = []
            count = 0
            
            #messagebox.showinfo("Incorrect!", "Incorrect")
            
            
            #reset the incorrect buttons
            def resetFor():
                global answer_dict
                for button in answer_dict:
                    button["image"] = back_photo
                answer_dict = {}
            if(len(keys) != 2):
                resetFor()
            elif(len(keys) == 2):
                dummyLabel.after(300, lambda: resetFor())



#let level 6 -> matches length is 12
#knowing that col length is 4 -> row length is 3

for row in range(rows):
    for col in range(4):
        #multiplying the row index by 4 to get next 4 elemnts in buttonList to be initialized
        current = row*4 + col
        buttonList[current].grid(row=row, column=col)
        buttonList[current].configure(command=
                                        lambda current = current: button_click(buttonList[current], current))


time_label = Label(root, text="", bg="black", fg="white")
time_label.after(0, clock)
time_label.pack(pady=5)

#number of coorect tries label
tries_label = Label(root, text="tries : 0", fg="white", bg="black")
tries_label.pack(pady=5)
correct_label = Label(root, text="correct : 0", fg="white", bg="black")
correct_label.pack(pady=0)

dummyLabel = Label(root, text= "",bg="#102027")
dummyLabel.pack()


#create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

#create an option dropdown menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options", menu=option_menu)
my_menu.add_command(label="Reset game",command=reset)
my_menu.add_separator()
my_menu.add_command(label="menu",command=retrun2menu)
my_menu.add_command(label="Exit game", command=root.destroy)


root.mainloop()
