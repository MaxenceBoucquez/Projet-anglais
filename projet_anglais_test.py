import simpleaudio as sa
from tkinter import *

# Creation of the tkinter window
root = Tk() 

# Definition of the event : for each key, when we click on it, it plays the appropriated sound

def clicked(event):
    if(event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        wave_obj = sa.WaveObject.from_wave_file("Music_notes/do1.wav")
        wave_obj.play()         # Play sound on Linux, for the Raspberry PI
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8) * 2) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        wave_obj = sa.WaveObject.from_wave_file("Music_notes/re.wav")
        wave_obj.play()
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8) *3) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        wave_obj = sa.WaveObject.from_wave_file("Music_notes/mi.wav")
        wave_obj.play()
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8) *4)and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        wave_obj = sa.WaveObject.from_wave_file("Music_notes/do1.wav")
        wave_obj.play()
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8)*5) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        wave_obj = sa.WaveObject.from_wave_file("Music_notes/sol.wav")
        wave_obj.play()
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8)*6) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        wave_obj = sa.WaveObject.from_wave_file("Music_notes/la.wav")
        wave_obj.play()
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8)*7) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        wave_obj = sa.WaveObject.from_wave_file("Music_notes/si.wav")
        wave_obj.play()
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8)*8) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        wave_obj = sa.WaveObject.from_wave_file("Music_notes/do2.wav")
        wave_obj.play()

# Definition of the canva
root.attributes('-fullscreen',True)
drawCanv = Canvas (width = root.winfo_screenwidth(), height = root.winfo_screenheight(), bd = 0)
drawCanv.bind ('<Button>', clicked) 
# Drawing of the white keys of the piano
for i in range(0,9):
    rectangle = drawCanv.create_rectangle(
        (drawCanv.winfo_screenwidth() / 8) *i, 0,
        (drawCanv.winfo_screenwidth() / 8) *i+1, drawCanv.winfo_screenheight(),\
        outline = 'black')

# Drawing of the black keys of the piano
for i in range(0,6):
    if(i!=3):
        rectangle = drawCanv.create_rectangle(
            (drawCanv.winfo_screenwidth()/8)*i+5*(drawCanv.winfo_screenwidth()/48),0,
            (drawCanv.winfo_screenwidth()/8)*(i+1)+3+(drawCanv.winfo_screenwidth()/48),drawCanv.winfo_screenheight()/(8/5),\
            outline='black', fill='black')
            

drawCanv.tag_bind("rectangle","<Button-1>",clicked)


drawCanv.tag_bind("rectangle","<Button-1>",clicked)

drawCanv.pack()

root.mainloop()