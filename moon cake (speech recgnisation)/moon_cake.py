import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
username = "NoobSaiyan"

def speak(command):
    engine.say(command)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time)

def date():
    day = datetime.datetime.now().strftime("%d:%B:%Y")
    speak("Today's date")
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
    time()
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

if __name__ == "__main__":
    greeting()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia','')
            try:
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak(result)
            except Exception as e:
                print(e)
                speak('sorry! be more specific please')
        elif 'offline' in query:
            quit()
        else:
            speak('i dont have answer for this ')
        