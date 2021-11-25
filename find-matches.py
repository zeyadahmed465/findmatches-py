from tkinter import *
import random
#from tkinter import messagebox
import time
import math



root = Tk()
root.geometry("500x620")


global winner, matches, tries
winner, tries = 0,0
photo1 = PhotoImage(file="img/test1.png")
photo2 = PhotoImage(file="img/test2.png")
photo3 = PhotoImage(file="img/test3.png")
photo1 = PhotoImage(file="img/test1.png")
photo4 = PhotoImage(file="img/test4.png")
photo5 = PhotoImage(file="img/test5.png")
photo6 = PhotoImage(file="img/test6.png")
back_photo = PhotoImage(file="img/back.png")


matches = [photo1,photo2,photo3,photo4,photo5,photo6,photo1,photo2,photo3,photo4,photo5,photo6]
random.shuffle(matches)

my_frame = Frame(root)
my_frame.pack(pady=10)

#define our winner counter

#define some variables
count = 0
answer_list = []
answer_dict = {}

#variables for clock function
m,s,stop = 0,0,0
time1 = int(time.strftime("%H"))*3600 + int(time.strftime("%M")) *60 + int(time.strftime("%S"))
#reset the game
def reset():
    global matches, winner, stop, time1, tries
    winner = 0
    tries = 0
    matches = [photo1,photo2,photo3,photo4,photo5,photo6,photo1,photo2,photo3,photo4,photo5,photo6]
    random.shuffle(matches)
    my_label2.config(text="00:00")
    my_label3.config(text="correct : 0")
    my_label4.config(text="tries : 0")
    #reset our tiles 
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    for button in button_list:
        button.config(image= back_photo, state="normal")
    time1 = int(time.strftime("%H"))*3600 + int(time.strftime("%M")) *60 + int(time.strftime("%S"))
    stop = 0
    clock()
    

#creating the timer
def clock():
    if stop!= 0:
        return 
    global time1
    current_time = int(time.strftime("%H"))*3600 + int(time.strftime("%M")) *60 + int(time.strftime("%S"))
    current_time = current_time - time1
    s = current_time % 60
    m = current_time // 60
    my_label2.config(text="{:02d}:{:02d}".format(m,s))
    my_label2.after(1000, clock)

#creating the winner function
def win():
    my_label.config(text="congrates! you win!!")
    

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
        my_label4.config(text=f"tries : {tries}")
        keys = list(answer_dict.keys())

        if matches[answer_list[0]] == matches[answer_list[1]] and len(keys) == 2:
            
            #disalbe the buttons
            for button in answer_dict: # each button will be the key which is the Button()
                button["state"] = "disabled"
            #resitting our variables
            answer_dict = {}
            answer_list = []
            count = 0
            #increment our winner
            winner += 1 
            my_label3.config(text=f"correct : {winner}" )
            if winner == 6:
                win()
                stop = 1
        else:
            #my_label.config(text="try again!")
            answer_list = []
            count = 0
            
            #messagebox.showinfo("Incorrect!", "Incorrect")
            
            
            #reset the incorrect buttons
            def x():
                global answer_dict
                for button in answer_dict:
                    button["image"] = back_photo
                answer_dict = {}
            if(len(keys) == 2):
                dummyLabel.after(300, lambda: x())


#define our buttons
b0 = Button(my_frame, text=" ", font=("Helvetica", 20),image = back_photo, command=lambda: button_click(b0, 0), relief="groove")
b1 = Button(my_frame, text=" ", font=("Helvetica", 20), image = back_photo, command=lambda: button_click(b1, 1), relief="groove")
b2 = Button(my_frame, text=" ", font=("Helvetica", 20), image = back_photo, command=lambda: button_click(b2, 2), relief="groove")
b3 = Button(my_frame, text=" ", font=("Helvetica", 20),image = back_photo, command=lambda: button_click(b3, 3), relief="groove")
b4 = Button(my_frame, text=" ", font=("Helvetica", 20), image = back_photo, command=lambda: button_click(b4, 4), relief="groove")
b5 = Button(my_frame, text=" ", font=("Helvetica", 20), image = back_photo, command=lambda: button_click(b5, 5), relief="groove")
b6 = Button(my_frame, text=" ", font=("Helvetica", 20), image = back_photo, command=lambda: button_click(b6, 6), relief="groove")
b7 = Button(my_frame, text=" ", font=("Helvetica", 20), image = back_photo, command=lambda: button_click(b7, 7), relief="groove")
b8 = Button(my_frame, text=" ", font=("Helvetica", 20),image = back_photo, command=lambda: button_click(b8, 8), relief="groove")
b9 = Button(my_frame, text=" ", font=("Helvetica", 20), image = back_photo, command=lambda: button_click(b9, 9), relief="groove")
b10 = Button(my_frame, text=" ", font=("Helvetica", 20), image = back_photo, command=lambda: button_click(b10, 10), relief="groove")
b11 = Button(my_frame, text=" ", font=("Helvetica", 20), image = back_photo, command=lambda: button_click(b11, 11), relief="groove")

b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root, text="")
my_label2 = Label(root, text="", bg="black", fg="white")
my_label2.after(0, clock)
my_label2.pack(pady=5)

#number of coorect tries label
my_label4 = Label(root, text="tries : 0", fg="white", bg="black")
my_label4.pack(pady=5)
my_label3 = Label(root, text="correct : 0", fg="white", bg="black")
my_label3.pack(pady=0)
dummyLabel = Label(root, text= "")
dummyLabel.pack()
#number of tries

#create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

#create an option dropdown menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options", menu=option_menu)
my_menu.add_command(label="Reset game", command=reset)
my_menu.add_separator()
my_menu.add_command(label="Exit game", command=root.quit)


root.mainloop()
