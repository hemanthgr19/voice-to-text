import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("say something")
        audio = r.listen(source)
        try:
            print("you have said: \n"+ r.recognize_google(audio))
            print("audio successfull")
        except Exception as e:
            print("error: "+str(e))


if __name__ == "__main__":
    main()