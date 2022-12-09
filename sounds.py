import simpleaudio as sa

def play(note):
    wave_obj = sa.WaveObject.from_wave_file(f"Music_notes/{note}.wav")
    wave_obj.play()

def playback(data):
    return

def record(n):