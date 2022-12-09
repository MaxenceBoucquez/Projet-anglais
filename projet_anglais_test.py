import simpleaudio as sa
from tkinter import *
from sounds import *
from time import *

# Creation of the tkinter window
root = Tk() 
root.attributes('-fullscreen',True)

# Definition of the canva
drawCanv = Canvas(
    width = root.winfo_screenwidth(), 
    height = root.winfo_screenheight(),
    bd = 0)
screenWidth = drawCanv.winfo_screenwidth()
screenHeight = drawCanv.winfo_screenheight()

# keys

# define the width of each key
# We have 8 white keys
whiteKeyWidth = screenWidth / 8
blackKeyWidth = screenWidth / 28


# Definition of the event : for each key, when we click on it, it plays the appropriated sound
def clicked(event):
    # Buttons
    #Record Button
    if ((event.x > drawCanv.winfo_screenwidth()-250) and (event.x < drawCanv.winfo_screenwidth()-40) and (event.y > 20) and (event.y < 80)) :
        print("Record")
        btn1
        actualTime = time()
        notes = []
        timers = []
        print(actualTime)
            
    elif ((event.x > drawCanv.winfo_screenwidth()-250) and (event.x < drawCanv.winfo_screenwidth()-40) and (event.y > 100) and (event.y < 160)) :
        print("Play recording")
        print(actualTime - time())
        
    # Keys
    elif not (blackkey_click(event)):
        whitekey_click(event)

def whitekey_click(event):
    if(event.x < whiteKeyWidth):
        play("do1")
    elif(event.x < whiteKeyWidth * 2):
        play("re")
    elif(event.x < whiteKeyWidth * 3):
        play("mi")
    elif(event.x < whiteKeyWidth * 4):
        play("fa")
    elif(event.x < whiteKeyWidth * 5):
        play("sol")
    elif(event.x < whiteKeyWidth * 6):
        play("la")
    elif(event.x < whiteKeyWidth * 7):
        play("si")
    elif(event.x < whiteKeyWidth * 8):
        play("do2")
        
def blackkey_click(event):
    if (event.y < screenHeight / (8/5)):
        if (event.x > whiteKeyWidth - blackKeyWidth/2 and event.x < whiteKeyWidth + blackKeyWidth/2):
            play("doSharp")
            return True
        if (event.x > whiteKeyWidth * 2 - blackKeyWidth/2 and event.x < whiteKeyWidth * 2 + blackKeyWidth/2):
            play("reSharp")
            return True
        if (event.x > whiteKeyWidth * 4 - blackKeyWidth/2 and event.x < whiteKeyWidth * 4 + blackKeyWidth/2):
            play("faSharp")
            return True
        if (event.x > whiteKeyWidth * 5 - blackKeyWidth/2 and event.x < whiteKeyWidth * 5 + blackKeyWidth/2):
            play("solSharp")
            return True
        if (event.x > whiteKeyWidth * 6- blackKeyWidth/2 and event.x < whiteKeyWidth * 6 + blackKeyWidth/2):
            play("siBemol")
            return True
    return False
    

drawCanv.bind('<Button>', clicked) 
# Drawing of the white keys of the piano
for i in range(0,9):
    rectangle = drawCanv.create_rectangle(
        whiteKeyWidth * i, 0,
        whiteKeyWidth * i + 1, screenHeight,\
        outline = 'black')

# Drawing of the black keys of the piano
for i in range(1,7):
    if(i!=3):
        rectangle = drawCanv.create_rectangle(
            whiteKeyWidth * i - blackKeyWidth / 2,0,
            whiteKeyWidth * i + blackKeyWidth / 2,screenHeight / (8/5),\
            outline='black', fill='black')
            
# Map the click event to trigger sounds
drawCanv.tag_bind("rectangle","<Button-1>",clicked)


# Button record
btn1 = drawCanv.create_rectangle(
            drawCanv.winfo_screenwidth()-250,20,
            drawCanv.winfo_screenwidth()-40,80,\
            outline='black', fill='grey')
drawCanv.create_text(drawCanv.winfo_screenwidth()-145, 50, text="RECORD", fill="black", font=('Helvetica 15 bold'))

# Button play recording
btn2 = drawCanv.create_rectangle(
            drawCanv.winfo_screenwidth()-250,100,
            drawCanv.winfo_screenwidth()-40,160,\
            outline='black', fill='grey')
drawCanv.create_text(drawCanv.winfo_screenwidth()-145, 130, text="PLAY RECORDING", fill="black", font=('Helvetica 15 bold'))

# Button play demo
btn3 = drawCanv.create_rectangle(
            drawCanv.winfo_screenwidth()-250,180,
            drawCanv.winfo_screenwidth()-40,240,\
            outline='black', fill='grey')
drawCanv.create_text(drawCanv.winfo_screenwidth()-145, 210, text="PLAY DEMO", fill="black", font=('Helvetica 15 bold'))



drawCanv.pack()

root.mainloop()