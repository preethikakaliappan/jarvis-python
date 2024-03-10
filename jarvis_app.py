import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import comtypes.client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour <= 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am Jarvis, Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...!")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "Home"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("Acording to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open statkoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open music' in query:
            music_dir = 'D:\\songs\\favorite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetme.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")














            
