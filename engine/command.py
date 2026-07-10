import time
import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #print(voices)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

@eel.expose #  to make this function accessible from frontend 
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1 # to set time of silence to make assistant talk
        r.adjust_for_ambient_noise(source) # to adjust for ambient noise
        audio = r.listen(source,# to set mic as iinput source 
            timeout=10, # time out mean the listening will stop after 10 sec
            phrase_time_limit=6 # set max phrase time is 6 sec
        )  
    try : 
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-ar')# use google web speech api to recognize audio and store recognized text in query
        print(f"User said: {query}")
        #speak(query)
        time.sleep(2)
        eel.DisplayMessage(query)



    except Exception as e : 
        return ""
    
    return query.lower() # to make query in lower case to make it easier to compare with commands




@eel.expose
def allCommands():
    query = takeCommand()
    print(query)

    if 'open' in query:
        from engine.features import openCommand
        openCommand(query)
    elif 'on google' in query or query.startswith('google') or query.startswith('search'):
        from engine.features import SearchGoogle
        SearchGoogle(query)
    elif 'on youtube' in query :
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
        print ('not run ')
    eel.ShowHood()
    
@eel.expose
def runTextCommand(text):
    query = (text or "").lower()
    print(query)
    if 'open' in query:
        from engine.features import openCommand
        openCommand(query)
    elif 'on google' in query or query.startswith('google') or query.startswith('search'):
        from engine.features import SearchGoogle
        SearchGoogle(query)
    elif 'on youtube' in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
        print('not run ')
    eel.ShowHood()
    
