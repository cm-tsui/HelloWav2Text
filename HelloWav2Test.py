# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio
# pip install pydub

import speech_recognition as sr

recognizer = sr.Recognizer()

# recording the sound
with sr.AudioFile("speech.wav") as source:
    recorded_audio = recognizer.listen(source)
    print("Done recording")

# Recorgnizing the Audio
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
    print("Decoded Text : {}".format(text))

except Exception as ex:
    print(ex)