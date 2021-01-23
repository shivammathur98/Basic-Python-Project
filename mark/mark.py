import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import re
import pyjokes
# you can import pywhatkit to add more advanced functionality, link - https://pypi.org/project/pywhatkit/
engine= pyttsx3.init('sapi5')
# for linux, mac users Google text to speech(gtts) or espeak will work instead of sepi5, so install it via pip

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Hi, my name is mark, how may I assist you ?")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_emailid@mgmail.com','your_password')
    server.sendmail('your_emailid@mgmail.com',to,content)
    server.close()

from os import system,name
def clear():
    if name == 'nt':
        #  for windows users:
        _= system('cls')
    else: 
        # for linux, mac users:
        _ = system('clear') 

if __name__ == "__main__": 
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak (results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open google" in query:
            webbrowser.open("www.google.com")
        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com") 
        elif "open github" in query:
            webbrowser.open("www.github.com")  
        elif "open irctc" in query:
            webbrowser.open("www.irctc.co.in")
        elif "open drive" in query:
            webbrowser.open("https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        elif "open gmail" in query:
            webbrowser.open("https://accounts.google.com/login")
        elif 'play music' in query:
            # provide your destination folder which contains music 
            music = 'C:\\Users\\Anonymous\\Documents\Music'
            songs = os.listdir(music)
            os.startfile(os.path.join(music,songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M %p")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            # provide path for your target shortcut for vs code or other program
            codePath = "C:\\Users\\Anonymous\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'mail to user' in query:
            try:
                speak("What should I write ?")
                content = takeCommand()
                # type the receiver's email id
                to = "receivermailid@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak ("I'm unable to send this email at this moment")
        elif 'search' in query:
            speak("What do you want me to search for ?")
            searches = takeCommand().lower()
            if('on youtube' in searches):
                new_keyword= searches.replace('on youtube','')
                url = "https://youtube.com/results?search_query=" + new_keyword
                webbrowser.get().open(url)
                speak("Here are some videos for" + new_keyword)
            else:
                url = "https://google.com/search?q=" + searches
                webbrowser.get().open(url)
                speak("Here is what I found")
        elif 'www' in query:
            webbrowser.get().open(query)
        elif "find location" in query:
            speak('What is the location ?')
            location = takeCommand().lower()
            url = "https://google.nl/maps/place/" + location + '/&amp;'
            speak("Here is the location for" + location)
            webbrowser.get().open(url)
        elif 'temperature' in query:
            tosearch = re.sub(r"^.+?(?=temperature)", "", query)
            url = "https://google.com/search?q=" + tosearch
            webbrowser.get().open(url)
            speak("Here's your temperature information")
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'exit' in query:
            speak("Okay, See you later")
            clear()
            exit()