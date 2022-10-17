import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate', 125)
engine.setProperty('voice',voices[1].id)    #it set voice is of male or female for male value should be zero

def wish():
    hour=int(datetime.datetime.now().hour)    #its tell the sytem whats the current time
    if hour>=0 and hour<=12:
        speak("Good Morning Anshul")
    elif hour>12 and hour<=18:
        speak("Good afternoon Anshul")
    else:
        speak("Good Night Anshul")
    speak("I'm Your assistant miri")
    speak("Please tell me how can i help you")

def speak(audio):                     #it speaks in audio form
    engine.say(audio)
    engine.runAndWait()
                      #it takes voice command from the user and returns str
def sendEmail(to ,cont):
    server = smtplib.SMTP('smntp@gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(kunwaranshul7739@gmail.com, password)
    server.sendmail(kunwaranshul7739@gmail.com, to, cont)
    server.close()
    
def tkcmd():
    #It takes microphone input from the user and returns string output

    a = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        a.pause_threshold = 1
        a.energy_threshold= 500
        audio = a.listen(source)
    try:
        print("Recognizing...")    
        query = a.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__=="__main__":
   
   while True:
       query =tkcmd().lower()

       if 'wikipedia' in query:
        speak('Ok Anshul Searching Wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=10)
        speak("According to wikipedia")
        print(results)
        speak(results)
       
       elif 'youtube' in query:
          webbrowser.open("youtube.com")
       elif 'google' in query:
          webbrowser.open("google.com")
       elif 'university' in query:
          webbrowser.open("uims.cuchd.in")
       elif 'lms' in query:
          webbrowser.open("lms.cuchd.in")
       elif 'linkedin' in query:
          webbrowser.open("linkedin.in")
       elif 'w3school' in query:
          webbrowser.open("www.w3schools.com/")
        #for opening song
       elif 'jatt da muqabala' in query:
          
          mdir="C:\\music"
          songs = os.listdir(mdir)
          print(songs)
          os.startfile(os.path.join(mdir,songs[1]))
       elif 'time' in query:
          strTime= datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Anshul , the time is {strTime}")
          print(strTime)
        #for opening app
       elif 'vs code' in query:
          vspath = "C:\\Users\\Swati\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          speak("Wait Anshul Visual studio code is opening")
          os.startfile(vspath)
       elif 'spotify' in query:
          wppath= "C:\\Users\\Swati\\AppData\\Roaming\\Spotify\\Spotify.exe"
          speak("Wait Anshul spotify is opening")
          os.startfile(wppath)
       elif 'ms' in query:
          wpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
          speak("wait Anshul Microsoft word is opening..")
          os.startfile(wpath)
        #sending email
       elif 'powerpoint' in query:
          ppath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
          speak("wait Anshul Powerpoint is opening..")
          os.startfile(ppath)


       elif 'email to anshul' in query:
          try:
            speak("Anshul Tell me what to sent on the email?")
            cont=tkcmd()
            to = "anshulkunwar56@gmail.com"
            sendEmail(to,cont)
            speak("Anshul your mail has been sent")
          except Exception as e:
            print(e)
            speak("Sorry Anshul I cant sent your email right now please try after some time")
       elif 'play' in query:
           speak("wait Anshul playing the song")
           speak(query)
           kit.playonyt(query)
       elif 'shutdown' in query:
           sec=10
           speak("Ok Anshul You PC will be shutdown within countdown of 10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 ")
           print("Shuting down the lappy........")
           os.system(f'shutdown /s /t {sec}')
       elif 'restart' in query:
           sec=10
           speak("Ok Anshul You PC will be restart within countdown of 10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 ")
           print("Restarting the lappy......")
           os.system("shutdown /r")\
        #personal interaction
       elif 'how are you' in query:
           speak("I am fine Anshul ,,, what about you")
       elif 'kaisi ho' in query:
           speak("Mai thik hu Anshul tum kaise ho")  
       elif 'love you' in query:
           speak("sorry but i hate you")
       elif 'Who is Anshul' in query:
           speak("Anshul is my owner")
      