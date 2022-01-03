import pyttsx3

class Spell:
    def __init__(self, word):
        self.word = word
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        for i in range(len(voices)):
            if str(voices[i].name) == "Microsoft Sabina Desktop - Spanish (Mexico)":
                self.engine.setProperty("voice", voices[i].id)
                break
            else:
                self.engine.setProperty("voice", voices[0].id)
        
    
    def spelling(self):
        spell = str()
        for i in range(len(self.word)):
            self.engine.say(self.word[i].upper())
            self.engine.runAndWait()
            spell += self.word[i]
            if self.word[i] == (" ") or i == (len(self.word) - 1):
                self.engine.say(spell.upper())
                self.engine.runAndWait()
                spell = str()
