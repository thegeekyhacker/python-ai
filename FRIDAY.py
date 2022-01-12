# pip install pyttsx3
# pip install SpeechRecognition
# pip install beautifulsoup4
# pip install google
# pip install wikipedia
# pip install pandas
# pip install PyPDF2
import pyttsx3
import speech_recognition as sr
import datetime
import random
from googlesearch import search
import webbrowser
import urllib.request
import urllib.parse
import re
import os
import wikipedia
import smtplib
import pandas as pd
import mysql.connector as sqltor
from PyPDF2.pdf import PdfFileReader
import pyaudio



edict = {'Utkarsh':'haethutkarsh@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[].id)
engine.setProperty('voice', voices[1].id)
hour1 = int(datetime.datetime.now().hour)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
con  = sqltor.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'utkarsh')
cursor = con.cursor()
today = datetime.datetime.now().strftime("%Y-%m-%d")
# os.chdir("C:/Users/admin/Desktop/UTKARSH/Class 12 Projects/Computer Project/JEE Notes")


#This is to make the AI speak. 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#This function wishes the user according to current time.     
def wishMe():
    speak("I am Friday sir!")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")
    elif hour>= 12 and hour<=17 :
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    print("How may I help you?")
    speak("How may I help you?")
def takecommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try :
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said :- {query}\n")
    except Exception as e:
        print(e) 
        print("Say that Again please....")
        speak("Say that again please....")
        return "None" 
    return query    
#This function sends email from your account              
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("haethutkarsh@gmail.com","haethutkarsh123") 
    server.sendmail("haethutkarsh@gmail.com", to, content)
    server.close()
def YouTube(search):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + video_ids[0]
    webbrowser.get(chrome_path).open_new_tab(url)
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            query = query.replace("wikipedia","")
            speak("Searching wikipedia......")
            results = wikipedia.summary(query,sentences = 2)
            speak("Wikipedia says: ")
            print(results)
            speak(results)
        elif "stop" in query :
            print("quitting.....")
            speak("quitting")
            if hour1>= 20 and hour1<=23 :
                print("Good Night Sir!")
                speak("Good Night Sir!")
            else:
                print("Goodbye Sir!")
                speak("Goodbye Sir!")    
            exit()
        elif "open youtube" in query:
            webbrowser.get(chrome_path).open_new_tab("youtube.com")

        elif "open google" in query:
            webbrowser.get(chrome_path).open_new_tab("google.com")

        elif "my mail" in query:
            webbrowser.get(chrome_path).open_new_tab("gmail.com")

        elif "music" in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            x = len(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,x-1)]))

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(strtime)

        elif "open code" in query:
            codePath = "C:/Users/UTKARSH/AppData/Local/Programs/Microsoft VS Code/Code.exe %s"
            os.startfile(codePath)

        elif ".com" in query:
            webbrowser.get(chrome_path).open(f"{query}")

        elif "send mail" in query:
            try:
                print("Do you want to send the Email to a new or an old contact?")
                speak("Do you want to send the Email to a new or an old contact?")
                p = takecommand()
                if "old" in p:
                    print()
                    print("Whom should I send the Email?")
                    speak("Whom should I send the Email?")
                    x = takecommand()
                    to = edict[x]
                    print("What should I say?")
                    speak("What should I say?")
                    content = takecommand()
                    sendEmail(to, content)
                    print("The Email has been successfully sent!")
                    speak("The Email has been successfully sent!")
                elif "new" in p:
                    print("Please tell me the email address of the recipient :")
                    speak("Please tell me the email address of the recipient :")
                    email_add = takecommand()
                    email_add = email_add.lower()
                    email_add = email_add.replace(" ","")
                    to = email_add + "@gmail.com"
                    print(to)
                    speak(to)
                    print("Is this the correct Email address?")
                    speak("Is this the correct Email address?")
                    x = takecommand()
                    if "no" in x:
                        while "no" in x:
                            print("Let's Try again")
                            speak("Let's Try again")
                            print("Please tell me the email address of the recipient :")
                            speak("Please tell me the email address of the recipient :")
                            email_add = takecommand()
                            email_add = email_add.lower()
                            email_add = email_add.replace(" ","")
                            to = email_add + "@gmail.com"
                            print(to)
                            speak(to)
                            print("Is this the correct Email address?")
                            speak("Is this the correct Email address?")
                            x = takecommand()
                    elif "yes" in x:
                        print("What should I say?")
                        speak("What should I say?")
                        content = takecommand()
                        sendEmail(to, content)
                        print("The Email has been successfully sent!")
                        speak("The Email has been successfully sent!")              
            except Exception as e:
                print(e)
                print("Sorry! I am not able to send this email at the moment")
                speak("Sorry! I am not able to send this email at the moment")
            print("Should I save this e-mail - address?")
            speak("Should I save this e-mail - address?")
            addemail = takecommand()
            if 'no' in addemail:
                print("OK")
                speak("OK")
            elif 'yes' in addemail :
                edict = edict + to    

        elif "What's up?" and "What is up?" in query:
            print("Nothing just chilling with my buddies Alexa, Cortana and Siri.")
            speak("Nothing just chilling with my buddies Alexa, Cortana and Siri.")

        elif "search" in query:
            query = query.replace("search","")
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)

        elif "audiobook" in query :      
            print("Which book do you want to read?")
            speak("Which book do you want to read?")
            book_name = takecommand()
            book_name = book_name + ".pdf"
            bookf = open(book_name,"rb")
            bookobj = PdfFileReader(bookf)
            pageno = bookobj.getNumPages()
            for i in range (pageno):
                bookp = bookobj.getPage(i)
                bookp = bookp.extractText()
                print(bookp)
                speak(bookp)  

        elif "open notepad" in query:
            print("Which file should I open?")
            speak("Which file should I open?")
            file_name = takecommand()
            file_name = file_name + ".txt"
            file_open = open(file_name,"w")
            print("What should I write?")
            speak("What should I write?")
            file_content = takecommand()
            file_open.write(file_content)
            file_open.close()
            file_open = open(file_name,"r")
            x = str(file_open.read())
            print(x)
            speak(x)
            file_open.close()
            exit()
        
        elif "open word" in query:
            print("Which file should I open?")
            speak("Which file should I open?")
            file_name = takecommand()
            file_name = file_name + ".docx"
            file_open = open(file_name,"r")
            x = str(file_open.read())
            print(x)
            speak(x)
            file_open.close()
            exit()
        elif "check for birthday" in query:
            print("Checking for Birthdays....")
            speak("Checking for Birthdays....")
            st = "select birthday from birthday"
            cursor.execute(st)
            data = cursor.fetchall()
            for i in range(len(data)):
                ihv = data[i][0].strftime("%Y-%m-%d")
                if today == ihv:
                    try :
                        cursor.execute(f"select name from birthday where birthday = '{ihv}'")
                        name = cursor.fetchall()
                        name = name[0][0]
                        print(f"Today is {name}'s birthday")
                        speak(f"Today is {name}'s birthday")
                        cursor.execute(f"select email from birthday where birthday ='{ihv}'")
                        date = cursor.fetchall()
                        cursor.execute(f"select msg from birthday where birthday = '{ihv}'")
                        content = cursor.fetchall()
                        content = content[0][0]
                        remail = date[0][0]
                        print(f"Would you like to wish {name}?")
                        speak(f"Would you like to wish {name}?")
                        choice = takecommand()
                        if "yes" in choice :
                            sendEmail(remail,content)
                        elif "no" in choice :
                            pass    
                    except Exception as f :
                        print(f)
                        print("Sorry! I am not able to send this email at the moment")
                        speak("Sorry! I am not able to send this email at the moment")
                else :      
                    print("Today is no one's birthday")
                    speak("Today is no one's birthday")        
        elif "add birthdays" in query:
            cursor.execute("select*from birthday")
            data1 = cursor.fetchall()
            sno = len(data1) + 1
            print("Whose birthday do you want to add?")
            speak("Whose birthday do you want to add?")
            name = takecommand()
            print("Tell me the birthdate in YYYYMMDD format")
            speak("Tell me the birthdate in YYYYMMDD format")
            bday = takecommand()
            bday = bday.replace(" ","")
            byear = bday[0:4]
            bmonth = bday[4:6]
            bdate = bday[6:8]
            bday2 = f'{byear}-{bmonth}-{bdate}'
            print("Enter the message you want to send")
            speak("Enter the message you want to send")
            messg = takecommand()
            print("Enter the email address of the recipient")
            speak("Enter the email address of the recipient")
            email = takecommand()
            email = email.lower()
            email = email.replace(" ","")
            email = email + "@gmail.com"
            comm = f"insert into birthday values({sno},'{name}','{bday2}','{messg}','{email}')"
            cursor.execute(comm)
            con.commit()                  
        elif "play" in query:
            query = query.replace("play","")
            query = query.replace(" ","")
            print(query)
            YouTube(query)
        elif "quit" in query:
            print("quitting.....")
            speak("quitting")
            if hour1>= 20 and hour1<=23 :
                print("Good Night Sir!")
                speak("Good Night Sir!")
            else:
                print("Goodbye Sir!")
                speak("Goodbye Sir!")    
            exit()