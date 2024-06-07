import random
import smtplib
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommond():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='eng-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Jamal. please say that again please...")
            return "none"
        return query

#to wish

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('muhammadjamalbakhsh70@gmail.com','')
    server.sendmail('muhammadjamalbakhsh70@gmail.com',to ,content)
    server.close()

def wish():
    hour = (datetime.datetime.now().hour)

    if hour>=12  and hour<=12:
        speak("Good Morning")
    elif hour>1 and hour<3:
        speak("Good Afternoon")
    else:
        speak("good morning Jamal how are YOU. i hope you doing well")
        speak("I am Jarvis A I Assistant. Please Tell Me How Can i Help you")

if __name__ == "__main__":
        wish()
        while True:

            query = takecommond().lower()

            #logic building for tasks

            if "open notepad" in query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)


            elif "open command prompt" in query:
                os.system("start cmd")

            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyWindow()

            elif "play music" in query:
                music_dir = "E:\\musics"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))


            elif "what is my ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif"wikipedia" in query:
                speak("searching wikipedia....")
                query = query.replace("old_string", "new_string")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia")
                speak(results)
                print(results)

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open google" in query:
                speak("jamal , what should i search google")
                cm = takecommond().lower()
                webbrowser.open(f"{cm}")


            elif "send message " in query:
                pywhatkit.sendwhatmsg("+923259819348","call me",6,56)

            elif "play song on youtube" in query:
                pywhatkit.playonyt("we down we go")

            elif "email to jalal" in query:
                try:
                    speak("what should i say?")
                    content = takecommond().lower()
                    to = "jalal317616@gmail.com"
                    sendEmail(to, content)
                    speak("email has been sent to jalal")

                except Exception as e:
                    print(e)
                    speak("sorry jamal, i am not able to send this email to jalal")


            elif "no thanks" in query:
                speak("thank q jamal. to using me.  i am happy to help you Have a Good Day and use me again i will help you with my pleasure")
                sys.exit()

            speak("Jamal, do you any other work. Please tell me. i am here for you")