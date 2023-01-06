import asyncio
import threading
import simpleaudio as sa
from tkinter import *
from sounds import *
from sounds import playback
from time import *

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

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

# keys array
arrayWhite = [False,False,False,False,False,False,False]
arrayBlack = [False,False,False,False,False]
# define the width of each key
# We have 8 white keys
whiteKeyWidth = screenWidth / 8
blackKeyWidth = screenWidth / 28


# Definition of the event : for each key, when we click on it, it plays the appropriated sound
def clicked(event):
    # Buttons
    # Record Button
    if ((event.x > drawCanv.winfo_screenwidth()-250) and (event.x < drawCanv.winfo_screenwidth()-40) and (event.y > 20) and (event.y < 80)) :
        print("Record")
        record()
    elif ((event.x > drawCanv.winfo_screenwidth()-250) and (event.x < drawCanv.winfo_screenwidth()-40) and (event.y > 100) and (event.y < 160)) :
        print("Play recording")
        loop.run_until_complete(playback())
    # Keys
    elif not (blackkey_click(event)):
        whitekey_click(event)

def whitekey_click(event):
    if(event.x < whiteKeyWidth):
        play("do1")
        # arrayWhite[0] = True
        # sleep(1000)
        # arrayWhite[0] = False
    elif(event.x < whiteKeyWidth * 2):
        play("re")
        #arrayWhite[1] = True
        #sleep(1000)
        #arrayWhite[1] = False
    elif(event.x < whiteKeyWidth * 3):
        play("mi")
        # arrayWhite[2] = True
        # sleep(1000)
        # arrayWhite[2] = False
    elif(event.x < whiteKeyWidth * 4):
        play("fa")
        # arrayWhite[3] = True
        # sleep(1000)
        # arrayWhite[3] = False
    elif(event.x < whiteKeyWidth * 5):
        play("sol")
        # arrayWhite[4] = True
        # sleep(1000)
        # arrayWhite[4] = False
    elif(event.x < whiteKeyWidth * 6):
        play("la")
        # arrayWhite[5] = True
        # sleep(1000)
        # arrayWhite[5] = False
    elif(event.x < whiteKeyWidth * 7):
        play("si")
        # arrayWhite[6] = True
        # sleep(1000)
        # arrayWhite[6] = False
    elif(event.x < whiteKeyWidth * 8):
        play("do2")
        # arrayWhite[7] = True
        # sleep(1000)
        # arrayWhite[7] = False
        
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


def drawAll():
    # Clearing the Canva
    drawCanv.delete("all")
    
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
    
    # TODO: Include the "isPressed" function to draw the key in grey
    # Drawing of the white note that are pressed 
    for i in range(0,9):
        a=0
        #if arrayWhite[i] == True:
        #   rectangle = drawCanv.create_rectangle(
        #   whiteKeyWidth * i, 0,
        #   whiteKeyWidth * i + 1, screenHeight,\
        #   outline = 'grey', fill='grey')
        #
            
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
   
    #
    drawCanv.pack()
    return

# This draws every keys and buttons
drawAll()



            
# Map the click event to trigger sounds
drawCanv.tag_bind("rectangle","<Button-1>",clicked)



drawCanv.pack()

root.mainloop()