from tkinter import*
import pyttsx3
import PyPDF2
from pytube import YouTube
import random
from pygame import mixer
from pyparsing import srange
import speech_recognition as sr
import instaloader

def main():
    root=Tk()
    root.title("Project")
    root.geometry("300x300")
    root["bg"]="darkolivegreen2"
    
    f=("Times new Roman",25,"bold")
    
    lbl_wlc=Label(root,text="Welcome",font=f)
    lbl_wlc.pack(pady=20)
    
    def next():
        root.destroy()
        second()
    
    f1=("Times new Roman",16,"bold")
    btn_next=Button(root,text="Next",font=f1,command=next)
    btn_next.pack(padx=90)
    root.mainloop()


def second():
    root=Tk()
    root.title("Menu")
    root.geometry("400x300")
    root["bg"]="darkolivegreen2"

    f=("Times new Roman",25,"bold")
    f1=("Times new Roman",16,"bold")
    
    lbl_opt=Label(root,text="Choose your option",font=f1)
    lbl_opt.pack(pady=10)
    
    def show():
        lbl_opt.config( text=clicked.get() )
        
    #dropdown menu options
    options=["Youtube video downloader","Story generator","Instagram profile picture downloader","Music Player","Speech to text","Audiobook","Exit"]
    
    #datatype of menu text
    clicked=StringVar()
    
    #initial menu text
    
    clicked.set("Select Option")
    
    #create dropdown menu
    drop=OptionMenu(root,clicked,*options)
    drop.pack()

    def nextpage():
        
            
            if clicked.get()=="Youtube video downloader":
                l=input("enter the link")
                #link = "https://www.youtube.com/watch?v=PaoeGgJs3Ac"
                link=l
                yt = YouTube(link)  

                try:
                    yt.streams.filter(progressive = True, 
                    file_extension = "mp4").first().download(output_path = "E:\Trupti\pytube", 
                    filename = "")
                except:
                    print("Some Error!")
                print('Task Completed!')
            
            elif clicked.get()=="Story generator":
                Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
                character = [' there lived a king.',' there was a man named Jack.',
                        ' there lived a farmer.']
                time = [' One day', ' One full-moon night']
                story_plot = [' he was passing by',' he was going for a picnic to ']
                place = [' the mountains', ' the garden']
                second_character = [' he saw a man', ' he saw a young lady']
                age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
                work = [' searching something.', ' digging a well on roadside.']

                # Selecting an item from each list and concatenating them.
                print(random.choice(Sentence_starter)+random.choice(character)+
                    random.choice(time)+random.choice(story_plot) +
                    random.choice(place)+random.choice(second_character)+
                    random.choice(age)+random.choice(work))

            elif clicked.get()=="Music Player":
                mixer.init()
                # --------------------------Path of your music
                m=input("enter the song file path  in mp3 format only..")
                mixer.music.load(m)

                mixer.music.set_volume(0.5)
                mixer.music.play()

                while True:
                    print("Press 'p' to pause")
                    print("Press 'r' to resume")
                    print("Press 'v' set volume")
                    print("Press 'e' to exit")

                    ch = input("['p','r','v','e']>>>")

                    if ch == "p":
                        mixer.music.pause()
                    elif ch == "r":
                        mixer.music.unpause()
                    elif ch == "v":
                        v = float(input("Enter volume(0 to 1): "))
                        mixer.music.set_volume(v)
                    elif ch == "e":
                        mixer.music.stop()
                        break

            elif clicked.get()=="Audiobook":
                
                book = open('oop.pdf', 'rb')
                pdfReader = PyPDF2.PdfFileReader(book)
                #pages = pdfReader.numPages
                start=int(input("Enter the page number from where it should start reading"))
                stop=int(input("enter the page number where it should stop"))

                speaker = pyttsx3.init()
                for num in range(start, stop):
                    page = pdfReader.getPage(num)
                    text = page.extractText()
                    speaker.say(text)
                    speaker.runAndWait()

            elif clicked.get()=="Speech to text":
                r = sr.Recognizer()


                with sr.Microphone() as source:
                    # read the audio data from the default microphone
                    print("speak anything")
                    audio_data = r.listen(source)
                    print("Recognizing...")
                    # convert speech to text
                    try:
                        text = r.recognize_google(audio_data)
                        print("you said:{}", format(text))
                    except:
                        print("sorry could not recognize your voice")

            elif clicked.get()=="Instagram profile picture downloader":
                ig = instaloader.Instaloader()
                dp = input("Enter Insta username : ")
                ig.download_profile(dp , profile_pic_only=True)

            elif clicked.get()=="Exit":
                exit()
            else:
                exit()

    submit=Button(root,text="submit",command=nextpage)
    submit.pack()
    
    #create buttons,it will change label text
    #btn_menu=Button(root,text="Click Me",command=show)
    #btn_menu.pack()
    
main()