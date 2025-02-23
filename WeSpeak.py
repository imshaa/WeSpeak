import pyttsx3
if __name__== '__main__':
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)

    print("Welcome to WeSpeak 1.0. This is created to help you with conversations, Created by Imsha Nadeem. ")

    while True:
        x = input("Enter Your Text: ")
        if x.lower() == 'stop':
            engine.say(" 'GoodBye. Thanks for Your Time. '")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()