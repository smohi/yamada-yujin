import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

unknown_v = 0

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    with sr.Microphone() as source:
        print("Please, say something!")
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            global unknown_v 
            unknown_v = 0
            return text
        except sr.UnknownValueError:
            unknown_v = 1
            return "Sorry, I didn't catch that!"
        except sr.RequestError:
            return "Sorry, I couldn't reach the speech recognition service!"
        
if __name__ == "__main__":
    while True:
        user_input = listen()
        
        if unknown_v == 1:
            print(user_input)
            speak(user_input)
        else:
            print(f"You said, {user_input}")
            speak(f"You said: {user_input}")
        
        if 'goodbye' in user_input.lower():
            speak("Sayonara, talk to you soon!")
            unknown_v = 0
            break