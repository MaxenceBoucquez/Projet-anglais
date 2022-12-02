from tkinter import *
import simpleaudio as sa

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
        # os.system("mpg123 " + "Music_notes/fa.wav")
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8)*5) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        # PlaySound('Music_notes/sol.wav', SND_FILENAME)
        wave_obj = sa.WaveObject.from_wave_file("Music_notes/sol.wav")
        wave_obj.play()
        os.system("mpg123 " + "Music_notes/sol.wav")
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8)*6) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        # PlaySound('Music_notes/la.wav', SND_FILENAME)
        os.system("mpg123 " + "Music_notes/la.wav")
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8)*7) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        # PlaySound('Music_notes/si.mp3', SND_FILENAME)
        os.system("mpg123 " + "Music_notes/si.mp3")
    elif((event.x>0 and event.x<(drawCanv.winfo_screenwidth() / 8)*8) and event.y>0 and event.y<drawCanv.winfo_screenheight()):
        # PlaySound('Music_notes/do2.wav', SND_FILENAME)
        os.system("mpg123 " + "Music_notes/do2.wav")

# Definition of the canva
root.attributes('-fullscreen',True)
drawCanv = Canvas (width = root.winfo_screenwidth(), height = root.winfo_screenheight(), bd = 0)
drawCanv.bind ('<Button>', clicked) 
# Drawing of the white keys of the piano
for i in range(0,9):
    rectangle = drawCanv.create_rectangle ((drawCanv.winfo_screenwidth() / 8) *i, 0, (drawCanv.winfo_screenwidth() / 8) *i+1, drawCanv.winfo_screenheight(),\
            outline = 'black')
# Drawing of the black keys of the piano
# for i in range(0,6):
#     if(i != 3):
#         rectangle = drawCanv.create_rectangle (((drawCanv.winfo_screenwidth()/8)*i+3*(drawCanv.winfo_screenwidth()/48)), 0, ((drawCanv.winfo_screenwidth()/8) *(i+1)+(drawCanv.winfo_screenwidth()/48)), drawCanv.winfo_screenheight()/3 \
#             outline = 'black' , fill='black')

drawCanv.tag_bind("rectangle","<Button-1>",clicked)


drawCanv.tag_bind("rectangle","<Button-1>",clicked)

drawCanv.pack()

root.mainloop()