import dictation
import spelling
import syllables
import meaning
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QCursor, QFont, QFontDatabase
from PyQt5 import QtCore, QtGui


app = QApplication(sys.argv)

#Font
QFontDatabase.addApplicationFont("assets\\font\CrimsonText-Regular.ttf")
font = QFont("Crimson Text")
#Window
window = QWidget()
window.setWindowIcon(QtGui.QIcon("assets\img\icon.ico"))
window.setWindowTitle("Diccionario")
window.setFixedSize(964, 567)
window.setStyleSheet("background: #EBEBEB;")

#Title
title = QLabel("Diccionario", window)
title.setAlignment(QtCore.Qt.AlignCenter)
title.setGeometry(260,20,480,130)
title.setFont(font)
title.setStyleSheet(
    "font-size: 42px;"
)


#Bar
#Bar Entry
entry = QLineEdit(window)
entry.setGeometry(260, 230, 500, 30)
entry.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
entry.setFont(font)
entry.setStyleSheet(
    "border-style: solid;" +
    "border-width: 1px;" +
    "border-color: #bcbcbc;" +
    "background-color: #EBEBEB;" +
    "font-size: 16px;" +
    "color: #000000;" +
    "border-radius: 5px;"
)



#Button Widgets
#Dictate
dictate_button = QPushButton("Dictar", window)
dictate_button.setGeometry(30, 220, 180, 50)
dictate_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
dictate_button.setFont(font)
dictate_button.setStyleSheet(
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

def listen():
    text = dictation.Listen()
    if len(text.value()) > 0:
        entry.clear()
        entry.setText(text.value())
    else:
        pass

dictate_button.clicked.connect(listen)
    

#Spell
spell_button = QPushButton("Deletrear", window)
spell_button.setGeometry(150, 350, 180, 50)
spell_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
spell_button.setFont(font)
spell_button.setStyleSheet(
    "*{border-style: solid;" +
    "border-width: 1px;" +
    "border-color: #bcbcbc;" +
    "background-color: #EBEBEB;" +
    "font-size: 18px;" +
    "color: #000000;" +
    "border-radius: 5px;}"+
    "QPushButton:pressed {" +
    "background: #E4E4E4;}"
)

def spell_fun(word):
    spelling.Spell(word).spelling()
    entry.clear()
    
spell_button.clicked.connect(lambda:spell_fun(entry.text()))

#Syllables
syllables_button = QPushButton("Silabas", window)
syllables_button.setGeometry(400, 350, 180, 50)
syllables_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
syllables_button.setFont(font)
syllables_button.setStyleSheet(
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

window_syllables = syllables.Syllables()
def syllables_fun():
    window_syllables.show()

syllables_button.clicked.connect(syllables_fun)

#Meaning
meaning_button = QPushButton("Significado", window)
meaning_button.setGeometry(670, 350, 180, 50)
meaning_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
meaning_button.setFont(font)
meaning_button.setStyleSheet(
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

def meaning_fun(word):
    meaning.Scraping(word)
    entry.clear()

meaning_button.clicked.connect(lambda: meaning_fun(entry.text()))

window.show()
sys.exit(app.exec())
