from tkinter import *
from Score import Score

results = Score.getLevel(1)
print(len(results))
root = Tk()

root.geometry("400x500")

mainFrame = Frame(root)
mainFrame.pack(fill = BOTH, expand=1)

canvas = Canvas(mainFrame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = Scrollbar(mainFrame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side = RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.bind('<Configure>', lambda event: 
    canvas.configure(scrollregion= canvas.bbox(ALL) ))

frame = Frame(canvas)

canvas.create_window((0,0), window=frame, anchor=NW)

texts = [StringVar(frame,"\n".join([str(i[0]).capitalize()+": "+str(i[1]) for i in result.items()]))
         for result in results
         ]

labels = [Label(frame, width=50, height=5, background="red", textvariable=text)
          for text in texts]

for i in range(len(labels)):
    labels[i].grid(row=i, pady=5, padx=5)

root.mainloop()


#print()


