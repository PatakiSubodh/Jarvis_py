#s1- pip install speechrecognition
#s2 - pip install googletrans==3.1.0a0a
#s3 - fn'set
# 1. listen
# 2. translate
# 3. connect all

# import speech_recognition as sr
# from googletrans import Translator 

# def Listen():
#     r = sr.Recognizer() 
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source, 0, 8)

#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language='auto')
#             print(f"usr said: {query}\n")

#         except:
#             return "None"

#         query = str(query).lower()
#         return query

# def TranslationH2E(Text):
#     line = str(Text)
#     translate = Translator()
#     result = translate.translate(line, 'hi')  #default is english, if want to translate to any other the type => (line, 'lang u want to translate to')
#     data = result.text
#     print(f"translated usr text: {data}.")
#     return data

# def MicExecute():
#     query = Listen()
#     data = TranslationH2E(query)
#     return data


# if __name__ == "__main__":
#     MicExecute()





# ******************chatGPT***********************************

import speech_recognition as sr
from googletrans import Translator
import indic_transliteration as it

# initialize the recognizer and translator objects
r = sr.Recognizer()
translator = Translator()

# set the source language and target language
source_language = 'auto'  # automatic language detection
target_language = 'hi'    # Hindi

# use the microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source, 0, 8)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language=source_language)
        print("You said:", text)

        # translate the text to Hindi
        translated_text = translator.translate(text, dest=target_language).text
        print("Translation:", translated_text)

        # transliterate the translated text to Hindi using English alphabet
        transliterated_text = it.transliterate(translated_text, 'hi')
        print("Transliteration:", transliterated_text)

    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))















