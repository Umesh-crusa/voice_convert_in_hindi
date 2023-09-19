import pyttsx3
import speech_recognition as sr
import datetime
import random
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
     hour=int (datetime.datetime.now().hour)
     if hour>=0 and hour<=12:
        speak("Good morning!")  
     elif hour>12 and hour<=18:
        speak("good afternoon sir")
        speak("hi umesh crusa how i can help you ")           
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listion....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
          print("Recognizing..")    
          query = r.recognize_google(audio, language='hi-in')
          print(f"User said query :{query}\n")   
    except Exception as e:
        print(e) 

        print("say that agin please...")
        return"none"
    return query
if __name__=="__main__":
    wishMe()
    while True:
       query = takeCommand().lower()
       
 