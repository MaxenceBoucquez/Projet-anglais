from asyncio import sleep
import simpleaudio as sa
from datetime import datetime
import json

recording = False
recordedMusic = []
start_time = None

def play(note):
    wave_obj = sa.WaveObject.from_wave_file(f"Music_notes/{note}.wav")
    wave_obj.play()
    if recording:
        global start_time
        time = datetime.now()
        delta = time - start_time
        start_time = time
        add(note,round(delta.total_seconds() * 1000))

def add(note,timecode):
    print(timecode)
    recordedMusic.append([note,timecode])

async def playback():
    with open("music.json") as json_file:
        notes = json.load(json_file)
        for note in notes:
            await sleep(note[1])
            play(note[0])
    return None

def record():
    global recording
    global start_time
    if recording:
        stopRecord()
    else:
        recording = True
        start_time = datetime.now()
    return start_time

def stopRecord():
    global recording
    recording = False
    saveRecord()

def saveRecord():
    print("save")
    with open('music.json', 'w') as outfile:
        json.dump(recordedMusic, outfile)