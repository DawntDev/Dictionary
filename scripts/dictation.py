import speech_recognition as sr
import pyttsx3

class Listen:
    def __init__(self):
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        for i in range(len(voices)):
            if str(voices[i].name) == "Microsoft Sabina Desktop - Spanish (Mexico)":
                engine.setProperty("voice", voices[i].id)
                break
            else:
                engine.setProperty("voice", voices[0].id)
                
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                self.text = r.recognize_google(audio, language="es-MX")

            except:
                try:
                    engine.say("Lo siento, no te he escuchado")
                    engine.runAndWait()
                except:
                    pass
                
    def value(self):
        try:
            return str(self.text).capitalize()
        except:
            return str()