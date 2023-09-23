# import speech_recognition as sr
# import playsound

# # Define a function to listen for claps and play a sound
# def play_sound():
#     print("Clap detected!")
#     playsound.playsound("JARVIS.wav")

# # Initialize the recognizer
# r = sr.Recognizer()

# # Set the microphone as the audio source
# with sr.Microphone() as source:
#     print("Say something...")
#     while True:
#         # Listen for audio input
#         audio = r.listen(source, 0, 5)

#         # Use the recognizer to convert audio to text
#         try:
#             text = r.recognize_google(audio)
#             print("You said:", text)
#         except sr.UnknownValueError:
#             print("Sorry, could not understand audio")
#             continue
#         except sr.RequestError as e:
#             print("Could not request results from Google Speech Recognition service; {0}".format(e))
#             continue

#         # Check for two claps in the audio input
#         if 'clap' in text.lower():
#             clap_count = text.lower().count('clap')
#             if clap_count == 2:
#                 play_sound()
#                 break
#             else:
#                 print("Please clap twice to trigger the sound.")
#         else:
#             print("Sorry, could not detect claps.")




# import sounddevice as sd
# from scipy.io.wavfile import write
# import numpy as np
# import math
# import time
# from playsound import playsound

# # Constants
# fs = 44100  # Sampling frequency
# duration = 3  # Duration of recording
# threshold = 0.03  # RMS threshold for detecting claps

# # Record sound from microphone
# def record_sound():
#     print("Recording started...")
#     myrecording = sd.rec(duration * fs, samplerate=fs, channels=1)
#     sd.wait()
#     print("Recording stopped.")
#     return myrecording[:, 0]

# # Detect human claps
# def detect_claps():
#     while True:
#         data = record_sound()
#         rms = np.sqrt(np.mean(np.square(data)))
#         if rms > threshold:
#             time.sleep(0.1)  # Wait for a moment to detect the second clap
#             data = record_sound()
#             rms = np.sqrt(np.mean(np.square(data)))
#             if rms > threshold:
#                 print("Clap detected!")
#                 playsound('JARVIS.wav')
#                 return
#         else:
#             print("Not detected.")

# # Run the program
# detect_claps()



import os
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import math
import time
from playsound import playsound
import speech_recognition as sr

# Constants
fs = 44100  # Sampling frequency
duration = 3  # Duration of recording
threshold = 0.5  # RMS threshold for detecting claps

# Record sound from microphone
def record_sound():
    print("Recording started...")
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=1)
    sd.wait()
    print("Recording stopped.")
    return myrecording[:, 0]

# Detect human claps and the sentence "wake up Jarvis"
def detect_sound():
    while True:
        data = record_sound()
        rms = np.sqrt(np.mean(np.square(data)))
        if rms > threshold:
            time.sleep(0.1)  # Wait for a moment to detect the second clap
            data = record_sound()
            rms = np.sqrt(np.mean(np.square(data)))
            if rms > threshold:
                print("Clap detected!")
                playsound('JARVIS.wav')
                return
        else:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say something...")
                audio = r.listen(source, 0, 5)
                print("done...")
            try:
                print("in try..")
                text = r.recognize_google(audio)
                if "wake up Jarvis" in text:
                    print("Wake up Jarvis detected!")
                    os.chdir('jarvis_audio')
                    playsound('JARVIS.wav')
                    return
            except:
                pass
            print("Not detected.")

# Run the program
detect_sound()




