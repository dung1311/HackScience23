import pyttsx3

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

