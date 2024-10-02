import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[33].id)

#test

#speak("hello, habiba begum, how are you doing? finished eating bhaat?")
speak("Hello there! how are you doing today?")