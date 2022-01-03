import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)

for i in range(len(voices)):
    if str(voices[i].name) == "Microsoft Sabina Desktop - Spanish (Mexico)":
        print(voices[i].name, "Sabina encontrado")
    print(str(voices[i].name))
engine.say("Hola Mundo")
engine.runAndWait()