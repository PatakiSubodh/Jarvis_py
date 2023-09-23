# => "Engaging J.A.R.V.I.S" implies that you are activating or starting up the J.A.R.V.I.S system.
# => "Dispatching J.A.R.V.I.S" implies that you are sending J.A.R.V.I.S to a specific location or task, possibly remotely.
# => "Initiate J.A.R.V.I.S" implies that you are beginning a process or operation involving J.A.R.V.I.S.
# => check if a file exists:
    #if os.path.exists('jarvis_audio\hi-my-name-is-jarvis.wav'):
    #     print("T")
    # else:
    #     print("F")
# => instead of a adding path of brave to system variables do this ******************
        #************** add import shutil ****************************
    # brave_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'    
            # if os.path.exists(brave_path):
            #     # Register Brave as default browser
            #     webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))

            #     # Open URL in Brave
            #     webbrowser.get('brave').open('https://www.google.com')
            # else:
            #     print('Brave is not installed.')
# => 

import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyaudio
import wave         #for wav files
import wikipedia
import webbrowser
import shutil

import subprocess
import platform
import keyboard         # for the user input(function playHindiSongs) #pip install keyboard

import sys          #for exiting the program

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')           # print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current time is:")
    speak("Current time is:")
    print(time)
    speak(time)

def date():
    date =datetime.datetime.now().strftime("%d/%m/%Y")
    print("Today's date: ")
    speak("Today's date: ")
    print(date)
    speak(date)
    # print(date)
    # speak(date)

def dateMe():
    dtme = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    print("Today's date, and current time is:")
    speak("Today's date, and current time is:")
    print(dtme)
    speak(dtme)
    # dtme = datetime.datetime.now()
    # speak(dtme)
    # return dtme.strftime("%d/%m/%Y, %H:%M:%S")

def weekDay():
    from datetime import date
    today = date.today()
    if today.weekday() == 0:
        print("Today is: Monday")
        speak("Today is: Monday")
    elif today.weekday() == 1:
        print("Today is: Tuesday")
        speak("Today is: Tuesday")
    elif today.weekday() == 2:
        print("Today is: Wednesday")
        speak("Today is: Wednesday")
    elif today.weekday() == 3:
        print("Today is: Thursday")
        speak("Today is: Thursday")
    elif today.weekday() == 4:
        print("Today is: Friday")
        speak("Today is: Friday")
    elif today.weekday() == 5:
        print("Today is: Saturday")
        speak("Today is: Saturday")
    else: 
        print("Today is: Sunday")
        speak("Today is: Sunday")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning sir!")
        speak("Good Morning sir!")
    
    elif hour>=12 and hour<18:
        print("Good Afternoon sir!")
        speak("Good Afternoon sir!")

    else:
        print("Good Evening sir!")
        speak("Good Evening sir!")
    print("I am Jarvis. Please tell me how may I help you")
    speak("I am Jarvis. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("\nInitiating JARVIS...")
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 0.1
        audio = r.listen(source, 0, 8)  #listens for the duration of 8seconds

    try:
        print("\nDispatching JARVIS...")
        print("Recognizing...")
        query = r.recognize_google(audio, language='auto')  # Language='en-in'
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

def startEng():
    while True:
        se = sr.Recognizer()
        with sr.Microphone() as source:
            se.adjust_for_ambient_noise(source)
            print("\nSay something...")
            srtE = se.listen(source, 0, 5)
            print("done...")

        try:
            print("in try...")
            text = se.recognize_google(srtE, language='auto')
            print(f"u: {text}\n")
            if "wake up Jarvis" in text:
                # os.chdir("jarvis_audio")
                wav_file = wave.open('D:\\Critical\\code\\myProjects\\Jarvis\\Jarvis PY\\jarvis_audio\\welcome-back.wav', 'rb')
                
                p = pyaudio.PyAudio()
                stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
                channels=wav_file.getnchannels(),
                rate=wav_file.getframerate(),
                output=True)
                data = wav_file.readframes(1024)
                while data:
                    stream.write(data)
                    data = wav_file.readframes(1024)
                stream.stop_stream()
                stream.close()
                p.terminate()
                wav_file.close()
                return
            elif "who are you" in text:
                # os.chdir("jarvis_audio")
                from pydub import AudioSegment
                from pydub.playback import play
                mp3_file = AudioSegment.from_mp3("jarvis_audio/NameJarvis.mp3")
                play(mp3_file)
                mp3_file.close()
                return
            else:
                print("in else...")
        
        except Exception as e:
            return "none"

        speak("\nsry say again!\n")
        return text

def wakeJarvis():
    se = sr.Recognizer()
    with sr.Microphone() as source:
        se.adjust_for_ambient_noise(source)
        print("\nSay something...")
        srtE = se.listen(source, 0, 5)
        print("done...")

    try:
        print("in try...")
        text = se.recognize_google(srtE, language='auto')
        print(f"u: {text}\n")
        if "wake up Jarvis" in text:
            # os.chdir("jarvis_audio")
            wav_file = wave.open('D:\\Critical\\code\\myProjects\\Jarvis\\JarvisPY\\jarvis_audio\\welcome-back.wav', 'rb')
            
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
            channels=wav_file.getnchannels(),
            rate=wav_file.getframerate(),
            output=True)
            data = wav_file.readframes(1024)
            while data:
                stream.write(data)
                data = wav_file.readframes(1024)
            stream.stop_stream()
            stream.close()
            p.terminate()
            wav_file.close()
            return
        elif "who are you" in text:
            # os.chdir("jarvis_audio")
            from pydub import AudioSegment
            from pydub.playback import play
            mp3_file = AudioSegment.from_mp3("jarvis_audio/NameJarvis.mp3")
            play(mp3_file)
            mp3_file.close()
            return
        else:
            print("in else...")
    except Exception as e:
        return "none"
    speak("\nsry say again!\n")
    return text

"""Concrete date type.

    Constructors:

    __new__()
    fromtimestamp()
    today()
    fromordinal()

    Operators:

    __repr__, __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __hash__
    __add__, __radd__, __sub__ (add/radd only with timedelta arg)

    Methods:

    timetuple()
    toordinal()
    weekday()
    isoweekday(), isocalendar(), isoformat()
    ctime()
    strftime()

    Properties (readonly):
    year, month, day
    """

def chailsa():
    wav_file = wave.open('D:\\Critical\\code\\myProjects\\Jarvis\\hanuman_god(wav).wav', 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
    channels=wav_file.getnchannels(),
    rate=wav_file.getframerate(),
    output=True)
    data = wav_file.readframes(1024)
    while data:
        stream.write(data)
        data = wav_file.readframes(1024)
    stream.stop_stream()
    stream.close()
    p.terminate()
    wav_file.close()

def god():
    god_dir = 'D:\\Critical\\code\\songs\\godSongs'
    godSongs = os.listdir(god_dir)
    print(godSongs)
    os.startfile(os.path.join(god_dir, godSongs[0]))

def mail():
    if 'open zero mail' or 'open zero email' in query:
        speak('opening default mail sir...')
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    elif 'open Tech mail' or 'open tech email' in query:
        speak('opening tech mail sir...')
        webbrowser.open('https://mail.google.com/mail/u/1/#inbox')
    elif 'open College mail' or 'open college email' in query:
        speak('opening ollege mail sir...')
        webbrowser.open('https://mail.google.com/mail/u/2/#inbox')
    elif 'open study mail' or 'open study email' in query:
        speak('opening studious mail sir...')
        webbrowser.open('https://mail.google.com/mail/u/3/#inbox')
    elif 'open second mail' or 'open second email' in query:
        speak('opening second mail sir...')
        webbrowser.open('https://mail.google.com/mail/u/4/#inbox')
    else:
        speak("I did not find anything on that name sir...")

def playHindiSongs():
    
    # #---------code with harry--------------
    # music_dir_hindi = 'D:\\Critical\\code\\songs\\audioHindiSongs'
    # audioHindiSongs = os.listdir(music_dir_hindi)
    # print(audioHindiSongs)
    # speak('playing hindi songs...')
    # os.startfile(os.path.join(music_dir_hindi,audioHindiSongs[0])

    #--------------version 2(written below)-----------------------
    #this takes user input
    #*******for all operating system***********
    # Define the folder path where the videos are stored
    video_folder = "D:\\Critical\\code\\songs\\hindiSongs"
    # Call the function to play videos from the folder
    play_video_from_folder(video_folder)
    #written below(version 2)

#----------------------version 2----------------------------
#------for all operating systems---------
def play_video_from_folder(folder_path):
    # Create a playlist
    playlist = []
    # Iterate over all files in the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp4"):
                # Add the complete file path to the playlist
                video_path = os.path.join(root, file)
                playlist.append(video_path)
    # Play the videos sequentially
    for video_path in playlist:
        print(f"Now playing: {video_path}")
        # Open the video in the default media player
        if platform.system() == "Windows":
            subprocess.Popen(['start', '', video_path], shell=True)
        elif platform.system() == "Darwin":         #for mac
            subprocess.Popen(['open', video_path])
        elif platform.system() == "Linux":
            subprocess.Popen(['xdg-open', video_path])
        # Wait for the video to finish playing
        #this will execute the songs part first the the rest
        input("Press Enter to continue...")
        # # from here: press enter to continue and esc to go to rest o program
        # while True:
        #     if keyboard.is_pressed('enter'):
        #         # Continue playing the next video
        #         break
        #     elif keyboard.is_pressed('esc'):
        #         # Exit the current execution and continue with the rest of the program
        #         return


if __name__ == "__main__":
    # clap.detect_claps()     #print("dataType of q2: ",  type(q2))
    # startEng()

    # print("\nEngaging JARVIS...")
    # wishMe()
    # dateMe()

    running = True
    speak('Engaging Jarvis...')
    while running:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wake up Jarvis' in query:
            wakeJarvis()

            # startEng()
        elif 'terminate' in query:
            running = False
            sys.exit(0)
        elif "what's the time" in query:
            time()
        elif "what's today's date" in query:
            date()
        elif 'day' and 'today' in query:
            weekDay()
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:    
            # url = ''
            webbrowser.open('https://youtube.com')  
         # ***** added brave, chrome to line 548 to webbrowser module and added path in system varibles *****
        elif 'open google' in query:
            webbrowser.open('https://google.com')
        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')
        elif 'open github' in query:
            webbrowser.open('https://github.com')
        elif 'mail' in query:
            mail()
        # elif 'engage incognito mode' in query:
            # webbrowser.open('https://.com')
        elif 'play hindi songs' in query:
            playHindiSongs()
        elif 'play god songs' in query:
            god()
        elif 'play hanuman chailsa' in query:
            chailsa()