import pyttsx3
import datetime

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

greeting()