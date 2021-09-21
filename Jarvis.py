import sys
import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyaudio
import wikipedia
from requests import get
import pyjokes
import pywikihow
from pywikihow import search_wikihow
import speedtest





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=4)

    try:
        print("Recognizing.....")
        query =r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"good morning, its {tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening,  its {tt}")
    speak("i am jarvis your personal ai assistant,  please tell me,  how can i help you")

def TaskExecution():
    wish()

    while True:
        query = takecommand().lower()

        if "open password manager" in query:
            npath = "C:\\Users\\GOVT ITI WOMENS\\OneDrive\\Documents\\python\\appMade\\main\\main"
            os.startfile(npath)

        elif "open password generator" in query:
            apath = "C:\\Users\\GOVT ITI WOMENS\\Downloads\\unity\\2018.4.34f1\\Password Generator\\output\\main\\main"
            os.startfile(apath)

        elif "open google" in query:
            speak("what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "close password generator" in query:
            speak("closing notepad")
            os.system("taskkill /f /im main.exe")

        elif "activate how to do mode" in query:

            speak("how to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how = takecommand()
                try:
                    if "close" in how:
                        speak("how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")

        elif "check internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            correctDownload = int(dl/800000)
            up = st.upload()
            correctupload = int(up/800000)
            speak(f"sir we have {correctDownload} mega bytes per second downloading speed and {correctupload} mega bytes per second uploading speed")

        elif "you can sleep now" in query:
            speak("i am going to sleep but you can call me anytime")
            break

def Pass(pass_inp):

    password = "Sector 16"

    passss = str(password)

    if passss == str(pass_inp):
        speak("access granted")
        Hotword()

    else:
        speak("Access not granted")




def Hotword():
    while True:
        permission = takecommand()
        if "wake up Jarvis" in permission:
            TaskExecution()
        elif "goodbye Jarvis" in permission:
            speak("thanks for using me. have a good day")
            sys.exit()


if __name__ == "__main__":
    speak("This needs password for access")
    speak("Kindly Provide password to access")
    passssss = takecommand()

    Pass(passssss)




