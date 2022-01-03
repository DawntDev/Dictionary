from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5 import QtGui
import pyttsx3

class FunButtonVowels(QWidget):
    def __init__(self, parent, vowel, ax, ay):
        super(FunButtonVowels).__init__()
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        for i in range(len(voices)):
            if str(voices[i].name) == "Microsoft Sabina Desktop - Spanish (Mexico)":
                self.engine.setProperty("voice", voices[i].id)
                break
            else:
                self.engine.setProperty("voice", voices[0].id)
        self.vowel = vowel
        QFontDatabase.addApplicationFont("assets\\font\CrimsonText-Regular.ttf")
        font = QFont("Crimson Text")
        button = QPushButton(f"{self.vowel}".capitalize(), parent)
        button.setGeometry(ax, ay, 80, 50)
        button.setFont(font)
        button.setStyleSheet(
            "*{border-style: solid;" +
            "border-width: 1px;" +
            "border-color: #bcbcbc;" +
            "background-color: #EBEBEB;" +
            "font-size: 18px;" +
            "color: #000000;" +
            "border-radius: 5px;}" +
            "QPushButton:pressed {" +
            "background: #E4E4E4;}"
        )
        
        button.clicked.connect(lambda: self.say())
        
    def say(self):
        if "a" in self.vowel and not "w" in self.vowel: self.vowel = f"{self.vowel}".replace("a", "á")
        elif "e" in self.vowel and not "w" in self.vowel: self.vowel = f"{self.vowel}".replace("e", "é")
        elif "i" in self.vowel: self.vowel = f"{self.vowel}".replace("i", "í")
        elif "o" in self.vowel: self.vowel = f"{self.vowel}".replace("o", "ó")
        elif "u" in self.vowel and not "ué" in self.vowel and not "uí" in self.vowel and not "w" in self.vowel: self.vowel = f"{self.vowel}".replace("u", "ú")
        if "r" in self.vowel and not "rr" in self.vowel and not "h" in self.vowel or "we" in self.vowel and not "h" in self.vowel: self.vowel = f"h{self.vowel}"
        try:
            self.engine.say(self.vowel)
            self.engine.runAndWait()
        except:
            pass
        

class Buttons(QWidget):
    def __init__(self, parent, letter, x, ax, ay):
        super(Buttons, self).__init__()
        self.letter = [letter]
        self.vowels = ["aeiou", "lalelilolu", "rareriroru","hahehihohu", "ueui"]
        QFontDatabase.addApplicationFont("assets\\fonts\CrimsonText-Regular.ttf")
        font = QFont("Crimson Text")
        parent = QPushButton((f"{self.letter[0]}").upper(), parent)
        parent.setGeometry(ax, ay, 80, 80)
        parent.setFont(font)
        parent.setStyleSheet(
            "*{border-style: solid;" +
            "border-width: 1px;" +
            "border-color: #bcbcbc;" +
            "background-color: #EBEBEB;" +
            "font-size: 18px;" +
            "color: #000000;" +
            "border-radius: 5px;}" +
            "QPushButton:pressed {" +
            "background: #E4E4E4;}"
        )
        parent.clicked.connect(lambda: self.vowel_creation_window(x))
        
    def vowel_creation_window(self, x):
        self.vowel_window = QWidget()
        self.vowel_window.setWindowIcon(QtGui.QIcon("assets\img\icon.ico"))
        self.vowel_window.setWindowTitle((f"{self.letter[0]}").upper())
        self.vowel_window.setFixedSize(520, 260)
        self.vowel_window.setStyleSheet("background: #EBEBEB;")

        self.vowel_creation_button(x)

    def vowel_creation_button(self, x):
        if not x == 13: self.letter += [(f"{self.letter[0]}{i}") for i in self.vowels[0]]
        if x == 1: self.letter += [(f"{self.letter[0]}{self.vowels[3][i:i+ 2]}") for i in range(0, len(self.vowels[3]), 2)]
        if x in [0, 1, 3, 4, 8, 12, 16]: self.letter += [(f"{self.letter[0]}{self.vowels[1][i:i+ 2]}") for i in range(0, len(self.vowels[1]), 2)]
        if x in [0, 1, 2, 3, 4, 12, 14, 16]: self.letter += [(f"{self.letter[0]}{self.vowels[2][i:i+ 2]}") for i in range(0, len(self.vowels[2]), 2)]
        if x in [4,13]: self.letter += [(f"{self.letter[0]}{self.vowels[4][i:i+ 2]}") for i in range(0, len(self.vowels[4]), 2)]
        
        ax = 20
        ay = 10
        
        for i in range(1, len(self.letter)):
            try:
                if i in [6, 11, 16]:
                    ax = 20
                    ay += 60
                if i == 1: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 2: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 3: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 4: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 5: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 6: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 7: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 8: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 9: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 10: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 11: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 12: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 13: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 14: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 15: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 16: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 17: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 18: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 19: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                elif i == 20: FunButtonVowels(self.vowel_window, self.letter[i], ax, ay)
                ax += 100
            except:
                pass
            
        self.vowel_window.show()
        self.letter = [self.letter[0]]



class Syllables(QWidget):
    def __init__(self):
        super(Syllables, self).__init__()
        self.setWindowIcon(QtGui.QIcon("assets\img\icon.ico"))
        self.setWindowTitle("Silabas")
        self.setFixedSize(435, 567)
        self.setStyleSheet("background: #EBEBEB;")
        self.buttons()
        
    def buttons(self):
        self.alphabet = "bcdfghjklmnñpqrstvwxyz"
        ax = 22
        ay = 12
        for x in range(len(self.alphabet)):
            if x % 4 == 0 and x > 0:
                ax = 22
                ay += 92
            if x == 0: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 1: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 2: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 3: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 4: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 5: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 6: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 7: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 8: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 9: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 10: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 11: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 12: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 13: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 14: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 15: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 16: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 17: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 18: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 19: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 20: Buttons(self, self.alphabet[x], x, ax, ay)
            elif x == 21: Buttons(self, self.alphabet[x], x, ax, ay)
            ax += 102
