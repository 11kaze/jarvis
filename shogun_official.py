# imported libraries
import tkinter as tk
import pyglet
import time
import random
import pygame 
import datetime
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
#---------------------------------------------------------------------------------------------------------------------
# properties of engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 130)    # rate of talking
engine.setProperty('volume', 0.9)  # Volume lies between 0-1
#-------------------------------------------------------------------------------------------------------------
#voice_id = " HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20-DSK"
#-->we cannot set new voice because we only have one voice id present in my installed module 
# And that voice is may be default bruhhhh..
#-----------------------------------------------------------------------------------------------------

# speaking part *********************************
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#------------------------------------
#-----------------------------------------------------------------------------
def takeCommand():
    r = sr.Recognizer()
   
    with sr.Microphone() as source:
        print("listening......")
        
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        speak("analyzing the given command ")
        query = r.recognize_google(audio)
        print(f"query : {query}\n")
    except Exception:
        print("okay, lets try agian with a high pitch\n")
        speak("okay, lets try agian with a high pitch")
        time.sleep(4)
        return takeCommand()
    return query   
greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
gre_rep =['wassup','yup']
question = ['How are you?', 'How are you doing?']
var1 = ['who made you', 'who created you']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is your name']
cmd1 = ['open browser', 'open google']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: I am sorry but you suffer from a terminal illness and have only 10 to live. Patient : What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video']
bye = ['exit', 'close', 'goodbye', 'see you later','bye','shut down','shut down yourself']
bye_rep =['okay, i will keep myself quiet till next command','okay tada','huh, i am going to sleep','see you again']
your_color = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
praise_rep = ['you are such a nice guy','i am grateful to have you as my owner','you are always nice to me','you are very polite']       
praise = ['praise me','say something about me','speak about me','what uou think about me']
face = ['show me your face','how does you look like','your face','what is your shape','your shape']
data = ['what i told you to remember','what i ask you to remember','do you remember anything']
ability = [" what you can do",'what you can perform','task you can perform']
rem_data = ["speak out everything ","tell me everything"]
remember_data = []
#----------------------------------------------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------------------------------------------
def search():

    query = takeCommand().lower() 
        
    if 'wikipedia' in query:
        speak("searching wikipedia.....")
        query = query.replace('Wikipedia'," " )
        results = wikipedia.summary(query, sentences=1)
        speak("According to wikipedia ")
        print(results)
        speak(results)
        
    elif query in cmd1:
        speak("Hold on a second please")
        webbrowser.open_new("https://www.google.com")
        speak("done")       
    elif query in greetings:
        speak(random.choice(gre_rep))
        print(random.choice(gre_rep))
    elif query in cmd4:
        speak("Hold on a second please")
        webbrowser.open_new("youtube.com")
        speak("done")       
    elif "open facebook" in query:
        speak("wait")
        webbrowser.open_new("https://www.facebook.com")
        speak("done")                      
    elif "open whatsapp" in query:
        speak("Hold on a second please")   
        webbrowser.open_new("https://www.whatsapp.com")
        speak("done")                      
    elif "open notepad" in query:
        speak("wait")
        note_pad = r'c:\\windows\\notepad.exe'
        os.system(note_pad)
        speak("done")
    elif query in var3:
        T_now = datetime.datetime.now().strftime('%h : %m')
        speak(f"time is {T_now}")
        print(f"time is {T_now}\n")
    elif query in var4:
        speak("I am your friend jarvis")
        speak("i was born on 23 september 2019")
        print("I am your friend Jarvis")
        print("i was made on 23 september 2019")        
    elif query in ability:
        speak("well i am able to perform some simple tasks like")
        speak( "open youtube, google, notepad and some other stuffs also")
        print("well i am able to perform some simple tasks like open youtube,google,notepad and some other stuffs also")                     
    elif query in question:
        speak("well, a little bit stressed because of online trafficking")
        speak("but rest of the things are good")            
    elif query in bye:
        speak(random.choice(bye_rep))
        print(random.choice(bye_rep))
        quit()
    elif query in var1:
        speak("well, i am created by a group of SRM University students")
        speak("there names are harshit setia, pawan, uday virat and ashutosh tiwari")
        print("well, i am created by a group of SRM University students")
        print("there names are harshit setia, pawan, uday virat and ashutosh tiwari")
    elif query in cmd3:
        jokrep = random.choice(jokes)
        speak(jokrep)
        print(jokrep)
    elif query in your_color:
        speak(random.choice(colrep))
        print(random.choice(colrep))
    elif query in praise:
        speak(random.choice(praise_rep))
        print(random.choice(praise_rep))
    elif query in face:
        facelook()
    elif 'remember' in query:
        query = query.replace("remember",'')
        query = query.replace(" i ",' you ')
        query = query.replace(" am ",' are ')
        remember_data.append(query) 
        speak("okay, got it")
    elif query in rem_data:
        speak("i know, few things that you told me to remember, like")
        print(remember_data)
        for x in remember_data:
            speak(x)
    else:
        query = query.replace("google","")
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % query)
        speak("here are the founded results")
#------------------------------------------------------------------------------------------
# To See the real face of virtual assistant *************************************** 
def facelook():
    animation = pyglet.image.load_animation(r'C:\\Users\\pawan\\Desktop\\jarvis.gif')
    animSprite = pyglet.sprite.Sprite(animation)
 
 
    w = animSprite.width
    h = animSprite.height
  
    window = pyglet.window.Window(width=w, height=h)
 
    r,g,b,alpha = 0.5,0.5,0.8,0.5
    pyglet.gl.glClearColor(r,g,b,alpha)
 
    @window.event
    def on_draw():         # to draw VA FACE **********
       window.clear()
       animSprite.draw()
 
    def close(event):
       window.close()

    pyglet.clock.schedule_once(close, 8.0)   # run close event fo VA face right after 8 seconds ("automatically")
    pyglet.app.run()
#-----------------------------------------------------------------------------------------------------------------------------------------
# For Front end of software ****************************
def quit():
    root.destroy()
root = tk.Tk()
root.title('Jarvis')
# pick a .gif image file you have in the working directory
fname = "C:\\Users\\pawan\\Desktop\\listening.png"
bg_image = tk.PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()
# size the window so the image will fill it
root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')
# add canvas text at coordinates x=15, y=20
# anchor='nw' implies upper left corner coordinates
# now add some button widgets
btn1 = tk.Button(cv, text="ask me",command=search)
btn1.pack(side='left', anchor='sw')
btn2 = tk.Button(cv, text="Quit", command=root.destroy)
btn2.pack(side='left', anchor='sw')


#-----------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
speak("please wait till i boot up")
# To play introductry music ****************************************
pygame.mixer.init()
pygame.mixer.music.load(r"D:\\music\\jarvis_voice.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
   continue 
speak("how can i help you")                      
root.mainloop()        