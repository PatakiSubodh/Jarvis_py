def takeCommand():
    ''' this is docstring: for a multiline comment to be a docString it should be first line of class, function, or a module   
    ** => if you hover over function call it will behave as tooltip in html and dispaly the docstring comment line. **
    can use triple= '(single quotes) or "(double quotes)
    -> use functioncall.__doc__ ==> to display the docstring
    ----------------------this is the below sentence-----------
    it takes microphone input from user and returns string output
    '''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold = 300      #minimum audio enery to consider for recording
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")    #print(e)    #=>if u want to print exception
        return "None"
    return query