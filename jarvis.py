import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("I am JARVIS sir . How can I help you today?")
    print("I am JARVIS sir . How can I help you today?")


def takeCommand():
    ''' it takes mic itnput and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio= r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xytjgj', 'cyxy')
    server.sendmail('gcuuc', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    
        elif 'open github' in query:
            webbrowser.open("github.com")           
        elif 'open notepad' in query:           
            webbrowser.open("notepad.exe")
        elif 'open command prompt' in query:            
            webbrowser.open("cmd.exe")
        elif 'open camera' in query:
            webbrowser.open("camera.exe")
        elif 'open calculator' in query:    
            webbrowser.open("calc.exe")
        elif 'open paint' in query: 
            webbrowser.open("mspaint.exe")
        elif 'open myntra' in query: 
            webbrowser.open("myntra.com")
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
        elif 'open spotify' in query: 
            webbrowser.open("open.spotify.com")
        elif 'open vs code' in query:
            codePath ="C:\\Users\\DASA GNANADEEP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.sartfile(codePath)
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"SIR,The time is {strTime}")
            speak(f"SIR,The time is {strTime}")
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "bkhjhvghn"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")
                print("Sorry sir, I am not able to send this email")
        elif 'exit' in query:
            speak("Thank you sir, have a nice day!")
            print("Thank you sir, have a nice day!")
            exit()
        elif 'shutdown' in query:
            speak("Shutting down sir!")
            print("Shutting down sir!")
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            speak("Restarting sir!")
            print("Restarting sir!")
            os.system("shutdown /r /t 1")
        elif 'open file' in query:
            speak("Opening file sir!")
            print("Opening file sir!")
            os.startfile("C:\\Users\\DASA GNANADEEP\\Desktop\\file.txt")
        elif 'open folder' in query:
            speak("Opening folder sir!")
            print("Opening folder sir!")
            os.startfile("C:\\Users\\DASA GNANADEEP\\Desktop\\folder")
        elif 'open netflix' in query:
            webbrowser.open("https://netfree2.cc/home")