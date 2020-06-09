import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
username = "NoobSaiyan"

def speak(command):
    engine.say(command)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    day = datetime.datetime.now().strftime("%d:%B:%Y")
    speak(day)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour < 12:
        speak("good morning "+username)
    elif hour >=12 and hour < 18:
        speak("good afternoon "+username)
    elif hour >=18 and hour < 24:
        speak("good evening "+username)
    speak("Welcome back")
    speak("Current time is")
    time()
    speak("Today's date")
    date()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

takeCommand()