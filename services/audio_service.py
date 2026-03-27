from gtts import gTTS
import uuid

def text_to_speech(text):
    filename = f"{uuid.uuid4()}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    return filename