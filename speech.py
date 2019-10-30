import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone() as source:
    print("Please say something: ")
    audio = listener.listen(source)

    try:
        text = listener.recognize_google(audio)
        print("Audio transcription: {}".format(text))
    except:
        print("Sorry, could not recognize your voice")

