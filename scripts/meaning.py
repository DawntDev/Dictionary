from bs4 import BeautifulSoup
import requests
import pyttsx3

class Scraping:
    def __init__(self, word):
        self.word = word
        url = f"https://dem.colmex.mx/Ver/{self.word}"
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, "html.parser")
        self.word = self.soup.find_all("span", id="MainContent_lblTitulo")
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        for i in range(len(voices)):
            if str(voices[i].name) == "Microsoft Sabina Desktop - Spanish (Mexico)":
                self.engine.setProperty("voice", voices[i].id)
                break
            else:
                self.engine.setProperty("voice", voices[0].id)
        self.validation()
    
    def validation(self):
        for i in self.word:
            if i.text == "Su búsqueda no tuvo resultados":
                self.word = self.soup.find_all("span", id="MainContent_lblTituloPalabrasSimilares")
                self.word = [x.text for x in self.word]
            else:
                self.word = i.text
                if "*" in self.word:
                    self.word = str(self.word).strip("*")
        self.answer()
    
    def answer(self):
        if type(self.word) == type(list()):
            suggestion = self.soup.find_all("p", class_="p2")
            suggestion = [x.text for x in suggestion]
            suggestion = list(map(lambda w: w.strip(), suggestion))
            
            self.engine.say(f"La palabra, {self.word[0]} no se ha encontrado, Tal vez lo que estas buscando es: ")
            self.engine.runAndWait()
            suggestion = [[[self.engine.say(x)], [self.engine.runAndWait()]] for x in suggestion]
        else:
            definition = []
            example = []
            for i in range(6):
                checking = self.soup.find_all("span", id=f"MainContent_repeater_lblDefinicion_{i}")
                checking = [x.text for x in checking]
                definition.append(checking)
                checking = self.soup.find_all("span", id=f"MainContent_repeater_lblEjemplo_{i}")
                checking = [x.text for x in checking]
                example.append(checking)
            self.engine.say(f"{self.word}")
            self.engine.runAndWait()
            for i in range(6):
                    self.engine.say(f"{definition[i]}")
                    self.engine.runAndWait()
                    if example[i] == [""] or example[i] == []:
                        continue
                    else:
                        self.engine.say("Algunos ejemplos son:")
                        self.engine.runAndWait()
                        self.engine.say(f"{example[i]}")
                        self.engine.runAndWait()
