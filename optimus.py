#!/usr/bin/env python3                                                                                

import speech_recognition as sr
import pyaudio
import pywhatkit
import datetime
import pyttsx3
from pygame import mixer
import wikipedia
import time
import vlc
import random
import os
from pywttr import Wttr




def choose_song():
    dirs = [r'/home/adrian/Music/Queen_-_Forever_Deluxe_Edition_2014',
            r'/home/adrian/Music/Queen_1989-2011_The_miracle_remastered/cd_1',
            r'/home/adrian/Music/Queen_1989-2011_The_miracle_remastered/cd_2_bonus',
            r'/home/adrian/Music/Guardians']
    # list to store files
    res = []
    for dir_path in dirs:
        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                if ".mp3" in path:
                    res.append(os.path.join(dir_path, path))

    song = random.choice(res)
    return song


def weather():
    engine.say("The average temperature in Vera is " + forecast.weather[0].avgtemp_c + " degrees celsius")
    engine.runAndWait()

def sound(path):
    mixer.music.load(path)
    mixer.music.play()

def say(text):
    engine.say(text)
    engine.runAndWait()
    


wttr = Wttr("Vera")
forecast = wttr.en()
engine = pyttsx3.init()
song = None
mixer.init()
recorder = sr.Recognizer()



while True:
    
    try:
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = recorder.listen(source)
        print("Recognizing:")
        text = recorder.recognize_google(audio)


        
        
        if str("Optimus") in text:
            sound("/home/adrian/Downloads/ding.mp3")
            text = text.replace("Optimus", "")
            print("you said: " + text)
            
            

            if "YouTube" in text:
                say("playing...")
                pywhatkit.playonyt(text)
            
            
            if "play music" in text:
                song = vlc.MediaPlayer("/home/adrian/Downloads/mercy.mp3")
                say("Ok, playing...")
                print("VLC is starting...")
                song.play()
                print("VLC is playing...")
                
            elif "stop music" in text:
                say("Ok, stopping...")
                print("VLC is stopping...")
                song.stop()
        
            elif "Google" in text:
                say("Ok, searching...")
                pywhatkit.search(text)
                
            elif "time" in text:
                time = datetime.datetime.now().strftime("%H:%M")
                say("curren time is " + time)
                
            elif "who is" in text:
                person = text.replace("who is", "")
                info = wikipedia.summary(person, 1)
                say(info)
                
            elif "starting my Kumon" in text:
                time = datetime.datetime.now().strftime("%H:%M")
                say("The starting time for your kumon is " + time)
                
            elif "finishing my Kumon" in text:
                time = datetime.datetime.now().strftime("%H:%M")
                say("The ending time for your kumon is " + time)
                 
            elif "fart" in text:
                list1 = ["/home/adrian/Downloads/01.mp3",
                         "/home/adrian/Downloads/02.mp3",
                         "/home/adrian/Downloads/03.mp3",
                         "/home/adrian/Downloads/04.mp3",
                         "/home/adrian/Downloads/05.mp3"]
                ranfart = random.choice(list1)
                fart = vlc.MediaPlayer(ranfart)
                time.sleep(2)
                fart.play()
                
            elif "random music" in text:
                song1 = choose_song()
                song = vlc.MediaPlayer(song1)
                song.play()
                
            elif "weather" in text:
                weather()

        
        
    except sr.UnknownValueError:
        print("UnknownValueError")
        pass
    except sr.RequestError:
        print("RequestError")
        
        
        