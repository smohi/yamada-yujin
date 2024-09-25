import speech_recognition as sr

#initilizing recognizer
recognizer = sr.Recognizer()

#capturing speech using microphone
with sr.Microphone() as source:
    print("Say something in English or Japanese:")
    audio = recognizer.listen(source)
    
    try:
        #recognizing speech
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, I couldn't reach the speech recognition service.")
