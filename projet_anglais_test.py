import simpleaudio as sa
from tkinter import *
from sounds import *

# Creation of the tkinter window
root = Tk() 
root.attributes('-fullscreen',True)

# Definition of the event : for each key, when we click on it, it plays the appropriated sound
def clicked(event):
    if(event.x < (drawCanv.winfo_screenwidth() / 8)):
        play("do1")
    elif(event.x < ((drawCanv.winfo_screenwidth() / 8) * 2)):
        play("re")
    elif(event.x < ((drawCanv.winfo_screenwidth() / 8) * 3)):
        play("mi")
    elif(event.x < ((drawCanv.winfo_screenwidth() / 8) * 4)):
        play("fa")
    elif(event.x < ((drawCanv.winfo_screenwidth() / 8) * 5)):
        play("sol")
    elif(event.x < ((drawCanv.winfo_screenwidth() / 8) * 6)):
        play("la")
    elif(event.x < ((drawCanv.winfo_screenwidth() / 8) * 7)):
        play("si")
    elif(event.x < ((drawCanv.winfo_screenwidth() / 8) * 8)):
        play("do2")

# Definition of the canva
drawCanv = Canvas(
    width = root.winfo_screenwidth(), 
    height = root.winfo_screenheight(),
    bd = 0)

drawCanv.bind('<Button>', clicked) 
# Drawing of the white keys of the piano
for i in range(0,9):
    rectangle = drawCanv.create_rectangle(
        (drawCanv.winfo_screenwidth() / 8) * i, 0,
        (drawCanv.winfo_screenwidth() / 8) * i+1, drawCanv.winfo_screenheight(),\
        outline = 'black')

# Drawing of the black keys of the piano
for i in range(0,6):
    if(i!=3):
        rectangle = drawCanv.create_rectangle(
            (drawCanv.winfo_screenwidth()/8) * i+5 * (drawCanv.winfo_screenwidth()/48),0,
            (drawCanv.winfo_screenwidth()/8) * (i+1) + 5 + (drawCanv.winfo_screenwidth()/48),drawCanv.winfo_screenheight()/(8/5),\
            outline='black', fill='black')
            
# Map the click event to trigger sounds
drawCanv.tag_bind("rectangle","<Button-1>",clicked)

drawCanv.pack()

root.mainloop()