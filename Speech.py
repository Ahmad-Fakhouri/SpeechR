import speech_recognition as sr
import sys
rec = sr.Recognizer()

with sr.Microphone() as src:
    while True:
        print("say something...")
        audio = rec.listen(src)
        text = rec.recognize_google(audio)

        if text in ["hello","hi","test"]:
            print("hi , how are you doing ")
        elif text in ["i am fine " , "good","i'm good"]:
            print("i hope your always good ")
        elif text in ["bad","angry","sad"]:
            print("oh im sorry to hear that let me try to cheer you up with reminding you that everything will be okay in the end you got this ")
        elif text in ["close","end"]:
            sys.exit(0)
        else:
            print("i dont understand you ")


