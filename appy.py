import pyttsx3
import os
import PyPDF2
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import random
from requests import get 
import time
import pywhatkit as kit  
from cv2 import cv2
import pyjokes
import pyautogui as pe
import requests
import instaloader
import tkinter as tk
from googlesearch import search




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    

    if hour>=0 and hour<12:
         print(f"Hey, Good Morning!, its {tt}")
         speak(f"Hey, Good Morning!, its {tt}")
        

    elif hour>=12 and hour<18:
          print(f"Hey, Good Afternoon!, its {tt}")
          speak(f"Hey, Good Afternoon!, its {tt}")


    else:
          print(f"Hey, Good Afternoon!, its {tt}")
          speak(f"Hey, Good Evening!, its {tt}")
            
 
def wish_2():
     speak("my name is, appy... ,Good to see you again.., how may i help you")

def takeCommand():    # Listening Function

     r  = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 1
          audio = r.listen(source)
          speak

     try:
          print("Recognizing...")
          query = r.recognize_google(audio, language='en')
          print(f"User Said: {query}\n") 
          speak

     except Exception as e:
          print(e)
          print("Paddan Sir...")
          speak("Paddan Sir")
          return "None"

     return query


def sendEmail(to, content):
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login('dhruv.marathe1904@gmail.com' , 'drmarathe')
     server.sendmail('dhruv.marathe1904@gmail.com', to, content)
     server.close




 # News 

def news():
     main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=14d0bbfe0d7043628fc8ded6b7313a50'
     main_page = requests.get(main_url).json()
          #printing news
     articles = main_page["articles"]
          #printing articles
     head = []
     day=["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth"]
     for ar in articles:
          head.append(ar["title"])
     for i in range (len(day)):
          print(f"today's {day[i]} news is: {head[i]}")
          speak(f"today's {day[i]} news is: {head[i]}")

# reading pdf 

def pdf_reader():
     
     book = open('test.pdf', 'rb')
     pdf_Reader = PyPDF2.PdfFileReader(book)
     pages = pdf_Reader.numPages
     speak(f"fast mode activating, in this book there are total {pages} pages ")
     speak("sir can you enter the page number i should read")
     pg = int(input("Enter The Page Number: "))
     page = pdf_Reader.getPage(pg)
     text = page.extractText()
     speak(text) 
     

     
def search_links_on_google():
     speak("What should i search on google")          
     # to search
     google_search = takeCommand().lower()
     print("To stop scrooling CTRL + c")
     print("This will be search on google :-", google_search)
     pe.hotkey('win' , 'r')
     pe.typewrite('notepad')
     pe.press('Enter')
     time.sleep(0.5)
     pe.typewrite('Please give credit for this code https://ddsinfotech.tk')
     pe.press('Enter')
     time.sleep(1)               
     for j in search(google_search, tld="co.in", num=10, stop=5, pause=2):     
          pe.typewrite(j)
          pe.press('Enter')
          speak(j)
     
 

 # google_map_image 

def google_location():
     speak("which location do you want to find")
     search_loc = takeCommand().lower()
     chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' 
     url_loc = ("https://www.google.co.in/maps/place/" +  search_loc)
     webbrowser.get(chrome_path).open(url_loc)
     speak("My next holiday will be") 
     speak(search_loc)
     speak("Hope your journey is safe")
     
def search_website():
               try:
                    speak("which website do you want to search")
                    search_website = takeCommand().lower()
                    url = ("https://" + search_website)
                    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                    webbrowser.get(chrome_path).open(url)
                    speak("Openning" + search_website)

               except Exception as e:
                    print(e)
                    speak("There is problem with the url or")
                     

        

if __name__ == "__main__":
     wishMe()
     wish_2()
    

     
     
     while True:
          query = takeCommand().lower()

          #Logic 

          if 'wikipedia' in query: # Wikipedia Results
               speak("Searching,  Wait a minute")
               query = query.replace("search",  "")
               results = wikipedia.summary(query, sentences=3)
               speak("According to my, knowledge")
               print(results)
               speak(results)


          # Openning Webiste's 

          elif 'website' in query:
               search_website()

               


      


          # Music Function

          elif 'play music' in query or 'new song play kar' in query:
               music_dir = 'E:\\Dhruv\\Songs' 
               songs = os.listdir(music_dir)
               rd = random.choice(songs)
               os.startfile(os.path.join(music_dir, rd))
               speak("Your Music is ready sir")

          # Time 

          elif 'the time' in query:
               strTime = datetime.datetime.now().strftime("%I:%M %p")
               print(strTime)
               speak(f"The time is {strTime}")

          # Open Software

          elif 'open chrome' in query:
               chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe "
               os.startfile(chromepath)
               speak("Opening Chrome")

          elif "open visual studio code" in query or  "open code" in query:
               visual_code_path = "C:\\Users\\HP ZBOOK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
               os.startfile(visual_code_path)
               speak("Opening Visual Studio Code")


          elif 'open camera' in query:
               speak("wait a second, camera is initialising")
               cap = cv2.VideoCapture(0)
               while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50) 
                    if k==27:
                         break
               cap.release()
               cv2.destroyAllWindows()


          # Sending Email 

          elif 'send email' in query:
               try:
                    speak("What Should i send?")
                    content = takeCommand()
                    to = "vinod.marathe@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been send")
               except Exception as e:
                    print(e)
                    speak("There is problem sending your email")
                    

          # Funny Commands

          elif 'describe yourself' in query or "what are you ment for" in query:
               random_words = ["just stutup", "hey there", "I am Appy, my brother name is junior"]
               speak(random.choice(random_words))

               
          # Show all commands 

          elif 'show commands' in query:
               speak("showing commands. In 3, 2, 1")
               print('')


          # For Knowing ip addr

       
                       

          # Search on google

          elif 'search on google' in query:  
               speak("sir, what should i search on google")
               cm = takeCommand().lower()
               webbrowser.open(f"{cm}")


          # Sending Message via whatsApp

          # elif 'send message' in query:
          #      kit.sendwhatmsg("phoneNumber" , "this is a test message ",9,52)
               

          # playing songs from youtube

          elif "play video on youtube" in query:
               speak('which video do you want to play ')
               video = takeCommand().lower()
               kit.playonyt(f"{video}")

          # Exit 

          if 'switch off' in query or "stop" in query or "close" in query:
               speak("bye, sir")
               exit()


          # for Closeing Software

          elif 'close chrome' in query:
               try:
                    speak("okay sir, closing chrome")
                    os.system("taskkill /f /im chrome.exe")
               except Exception as e:
                    speak("Chorme is not open")


          # seting alarm 

          elif 'set alarm' in query:
               nn = int(datetime.datetime().year)
               if nn==22:
                    music_dir = 'E:\\Dhruv\\Songs'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))


          # Jokes 

          elif 'tell me a joke' in query:
               speak("calling modi to find joke for you")
               joke = pyjokes.get_joke()
               print(joke)
               speak(joke)


          # shutdown, restart, sleep

          elif "shut down my laptop" in query:
               os.system("shutdown /s /t 5")
               speak("shuting down myself meet you soon")

          elif "restart my laptop" in query:
               os.system("shutdown /r /t 5")
               speak("restarting myself meet you soon")

          elif "time to go to bed" in query: 
               os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

          # To switch window 

          elif "switch window" in query or "next tab" in query:
               pe.keyDown("alt")
               pe.press("tab")
               time.sleep(2)
               pe.keyUp("alt")
               speak("window has been switch")

          # News 
          
          elif "tell me news" in query or "latest news" in query:
               speak("please wait sir, feteching the letest news")
               news()

          # test

          elif "english is funny" in query:
               speak("HAHA ")

          
          #  To find location 

          elif 'where i am' in query or 'where are we' in query:
               speak("wait sir, collecting information from, nasa satellite ")
               ipAdd = get('https://api.ipify.org').text
               print(f"sir your IP address is {ipAdd}")
               speak(f"sir your IP address is {ipAdd}")
               try:
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                         # print(geo_data)
                    city = geo_data['city']
                    country = geo_data['country'] 
                    print(f"sir i am not sure, but i think are in {city} city of {country} country")
                    speak(f"sir i am not sure, but i think are in {city} city of {country} country")

               except Exception as e:
                    speak("Sorry..............To say but unable to determine your present location")


          elif "instagram profile" in query or " search profile instagram" in query:

                    speak("sir, which profile do you want to search, Please Enter that profile username")
                    which_profile = input("Enter username here: ")
                    webbrowser.open(f"https://www.instagram.com/{which_profile}")
                    speak(f"Sir here is the profile of the user {which_profile}")
                    time.sleep(5)
                    speak("Sir, Would you like to download profile picture of this account")
                    condition = input("yes or No: ")
                    if "yes" in condition:
                         mod = instaloader.Instaloader()
                         mod.download_profile(which_profile, profile_pic_only=True)
                         speak("sir, that was easy, profile picture has beed saved in our main folder")
                    else:
                         speak("")
                         pass

              


          # taking a screenshot

          elif "screenshot" in query or "take a screenshot" in query:
               speak('sir, please tell me the name for the same')
               name = takeCommand().lower()
               speak("sir, hold your screen. taking screenshot in 3, 2, 1, screen shot has been taken")
               img = pe.screenshot()
               img.save(f"{name}.png")
               speak("Screen Shot has been saved in our screenshot folder. sirrr please say thank you ")

          # Reading a pdf not working yet


          elif "read pdf" in query:
               
               pdf_reader()


          #google search 
          
          elif "search link" in query:
               search_links_on_google()
               
                    

          # google_location

          elif "location" in query:
               google_location()
     

          # In_Valid_Command

          else:
               print("invalid command.....Invalid command! Sir, I request you to go through, command.txt file" )
               speak("invalid command.....Invalid command! Sir, I request you to go through, command.txt file" )

          


      

          

               
               
          



              
