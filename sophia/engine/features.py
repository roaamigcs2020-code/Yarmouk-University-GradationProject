import webbrowser
from playsound import playsound
import eel
import os
from .command import speak
from .config import ASSISTANT_NAME

import re
import sqlite3
from urllib.parse import quote as urlquote

con =sqlite3.connect("sophia.db")
cur=con.cursor()


#function to play sound
def playAssistantSound():
    music_dir='www\\assets\\audio\\start_sound.mp3'
    playsound(music_dir)

@eel.expose
#sound for click mic 
def playClickSound():
    music_dir='www\\assets\\audio\\click_sound.mp3'
    playsound(music_dir)


def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","").strip().lower()

    if query!="":
        # try in sys_commands
        cur.execute(f"SELECT path FROM sys_commands WHERE LOWER(name) = '{query}'")
        result=cur.fetchall()
        if len(result)!=0:
            speak("Opening " + query)
            os.startfile(result[0][0])
            return
        #if not found in sys_commands try in web_commands
        cur.execute(f"SELECT url FROM web_commands WHERE LOWER(name) = '{query}'")
        result=cur.fetchall()
        if len(result)!=0:
            speak("Opening " + query)
            webbrowser.open(result[0][0])
            return
        #if not found in web_commands or sys_commands try os.system
        speak("opening " + query)
        try:
            os.system('start ' + query)
        except Exception as e :
            speak(f"sorry i can't open {query}")
        
        

def PlayYoutube(query):
    search_term=extract_yt_term(query)
    if search_term:
        speak("playing " +search_term + " on youtube")
        kit.playonyt(search_term)
    else:
        speak("sorry i can't play that")

def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command,re.IGNORECASE)
    return match.group(1).strip() if match else None

def SearchGoogle(query):
    term = extract_google_term(query)
    if term:
        speak("searching " + term + " on google")
        webbrowser.open(f"https://www.google.com/search?q={urlquote(term)}")
    else:
        speak("sorry i can't search that")

def extract_google_term(command):
    patterns = [
        r'(?:search\s+for|search)\s+(.*?)\s*(?:on\s+google)?$',
        r'google\s+(.*)$',
        r'(.*?)\s+on\s+google$',
    ]
    for p in patterns:
        m = re.search(p, command, re.IGNORECASE)
        if m:
            term = m.group(1).strip()
            if term:
                return term
    return None
