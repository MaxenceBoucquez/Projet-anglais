import simpleaudio as sa

listener = None

def play(note):
    wave_obj = sa.WaveObject.from_wave_file(f"Music_notes/{note}.wav")
    wave_obj.play()
    if listener:
        listener(note)

def playback(data):
    return

def record():