import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning! new day new life")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Shubham I think you are already rocking")

    elif hour>=18 and hour<17:
        speak("Good evening")

    else:
        speak("Good night! Abhi take some rest now. Win the next day")
    speak("I am JB your personalised Artificial Intelligence. How may I help you?")
    speak('''You can open youtube, google, linkedin, file explorer, visual studio, know the date and time,
     search wikipedia, open teams, open email,play music and customise me anytime''')

def takeCommand():
    speak("Speak anything")
    print('''You can open youtube, google, linkedin, file explorer, visual studio, know the date and time,
     search wikipedia, open teams, open email,play music and customise me anytime''')
    #it takes mic input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        r.pause_threshold=2
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language='en-in')
            print("You said : {}".format(text))
        except Exception as e:
            print("Sorry could not recognize what you said")
            return "None"
    return text

if __name__ == '__main__':
    wishMe()
    
    while 1:
        query=takeCommand().lower()
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/feed/")
        elif 'wikipedia' in query:
            print("searching wikipedia....")
            speak("searching wikipedia.... ")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)
        else:
            speak("Sorry search queries could not be satisfied. Thank you for your time")
            break
V            