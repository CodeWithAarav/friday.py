
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour <18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Friday Sir . How may I help You ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please ...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()

if 'wikipedia' in query:
    speak('Searching...')
    query = query.replace("Wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    speak("According to Wikipedia")
    speak(results)
    print(results)

elif  'open youtube' in query:
    webbrowser.open("youtube.com")

elif  'open google' in query:
    webbrowser.open("google.com")

elif 'oper classroom' in query:
    webbrowser.open("https://classroom.google.com/u/0/c/MzE0NzU1MjY5NTA1")

elif 'play music' in query:
    music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
    songs = os.listdir(music_dir)
    print(songs)
    

     

     

