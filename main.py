from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr

r = sr.Recognizer()


def speaker(words):
    sound = gTTS(text="{}".format(words), lang="en")
    sound.save("test.mp3")
    playsound("test.mp3")
    os.remove("test.mp3")


def listener():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=2)
            statement = r.recognize_google(audio, language='en-gb')
            # print(f"user said:{statement}\n")
        except:
            return "None"
        return statement


isActive = False
# x = input("Name: ")
introduction = "Hello. Welcome to the Melody, A, I."
# speaker(introduction)
while True:
    text = listener().lower()
    if "alexa" in text:
        if "turn the volume on" in text or "turn on volume" in text or "increase volume" in text or "turn on the volume" in text or "increase the " \
                                                                                                    "volume" in text:
            speaker("Of course!")
            isActive = False
        else:
            isActive = True
            speaker("Go on?")
    elif isActive and text != "none":
        if "turn the volume on" in text or "turn on volume" in text or "increase volume" in text or "turn on the volume" in text or "increase the " \
                                                                                                    "volume" in text:
            speaker("Of course! Turning to volume on!")
        elif "goodbye" in text or "exit" in text or "quit" in text or "bye" in text:
            break
        else:
            speaker("I couldn't quite understand that.")
        isActive = False
        print(text)
    if text == 0:
        continue

speaker("Goodbye!")