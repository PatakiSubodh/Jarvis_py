import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:

    # adjust ambient noise levels
    r.adjust_for_ambient_noise(source)

    # prompt the user to speak
    print("Speak something...")
    audio = r.listen(source)

    try:
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print(f"user said: {text}")

    except sr.UnknownValueError:
        # handle unrecognized speech
        print("Sorry, I could not understand what you said.")

    except sr.RequestError as e:
        # handle error while retrieving transcription results
        print(f"Could not request results from Google Speech Recognition service; {e}")
