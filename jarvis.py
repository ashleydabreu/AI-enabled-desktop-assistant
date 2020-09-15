import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak ("hey I am casandra here . tell me how can i help you")

def takeCommand():
    #it takes microphone input from user nad returns string op 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
        print("say that again please")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dabreuashley8@gmail.com', 'yourpassword')
    server.sendmail('dabreuashley8@gmail.com', to, content)
    server.close()


if __name__== "__main__":
   wishMe()
   while True:
       query = takeCommand().lower()
       if 'wikipedia' in query:
           speak('searching wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("according to wikipedia")
           speak(results)
       elif 'open youtube' in query:
            webbrowser.open("youtube.com")
       elif 'open google' in query:
            webbrowser.open("google.com")
       elif 'open gmail' in query:
            webbrowser.open("gmail.com")
       elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"hey , the time is {strTime}")
       elif 'open python' in query:
           codePath = "C:\\python3.7.9\\Lib\\idlelib\\idle.pyw"
           os.startfile(codePath)

       elif 'email to ashley' in query:
           try:
               speak('what should i say ?')
               content = takeCommand()
               to = "dabreuashley8@gmail.com"
               sendEmail(to, content)
               speak("email has been sent ! thanks")
           except Exception as e:
               print(e)
               speak("sorry i am not able to send this email")

       elif 'quit' in query:
           exit()





