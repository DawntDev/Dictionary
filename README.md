<h1>Dictionary</h1>
<p>
 <a href="https://discord.com/channels/@me/@GeimerDroiid#0359">
     <img alt="GeimerDroiid | Discord" width="24px" align="right" raw=true HSPACE="5" src="https://raw.githubusercontent.com/GeimerDroiid/GeimerDroiid/main/assets/discord.svg"></a>
 <a href="https://open.spotify.com/playlist/6eDl0FX1pNcaFXgYIBOobX?si=aewrQ2nJTuSgkMSip3d8-Q&utm_source=copy-link">
     <img alt="GeimerDroiid | Spotify" width="24px" align="right" raw=true HSPACE="5" src="https://raw.githubusercontent.com/GeimerDroiid/GeimerDroiid/main/assets/spotify.svg"></a>
 <a href="https://github.com/GeimerDroiid">
    <img alt="GeimerDroiid | Github" width="24px" align="right" raw=true HSPACE="5" src="https://raw.githubusercontent.com/GeimerDroiid/GeimerDroiid/main/assets/github.svg"></a>
 <a href="mailto:jmanuelhv9@gmail.com">
    <img alt="Email | jmanuelhv9@gmail.com" width="24px" align="right" raw=true HSPACE="5" src="https://raw.githubusercontent.com/GeimerDroiid/GeimerDroiid/main/assets/gmail.svg"></a>
</p>
<h3>About</h3>

Application focused on searching the meaning of words through web scraping, besides having more functions such as Dictation, Spelling and Syllables.<br>
I created this application as a way to test the knowledge that I have started to acquire so I decided to make this dictionary with some basic functions like spelling but from there more ideas came up, like implementing a method that would tell me the meanings of the words that I didn't understand, or a way in which I didn't have to write the word and just by telling the computer I could write it. When I created this application I was just starting to learn Python (it is the language I used for this application) so I may have a lot of bad practices in the code that I am correcting for future versions. During the creation of this application I learned how to make user interfaces, I dabbled a bit in web scraping and besides investigating a method with which I can change text to sound and play it also at the end I used object oriented programming to facilitate the creation of the interface.

<div align="center">
<img alt="Dictionary | GUI" width="720px" src="https://raw.githubusercontent.com/DawntDev/Dictionary/master/assets/img-readme/gui.png">
<img alt="Dictionary | GUI" height="450px" width="720px" src="https://raw.githubusercontent.com/DawntDev/Dictionary/master/assets/img-readme/syllables.png">
</div>

---

<h3>What's new in v1.5</h3>

- **Interface improvements**
    
    Better interface with buttons and colors that contrast better with each other as well as better typography, more minimalist animations for a better user experience.

- **Bugs fixed**

    Correction of errors mainly of grammar among the most outstanding is the elimination of "Gua" and "Guo" since that conjugation of letters does not belong to the grammar of the Spanish language. Also improvement in the application startup time.

- **Code improvement**

    I have focused on the almost total reconstruction of the application so all the code is new, I have looked for the way to preserve the readability of the same for it I have divided each function in different files. Besides looking for the most efficient and easy way to do each one (All the code is in English).

- **The dictation function has been disabled**

    I have decided to disable the dictation feature in the final version, as it gave me a lot of problems when packaging the application, so I decided to keep it disabled until I find a way to build this feature and have as few bugs as possible as well as a proper functioning.

---

<h3>Functions</h3>

- Dictation

    The dictation function listens and converts your voice into text that will be entered into the search bar of the application, thanks to this you can apply some other function to that text. For this function I have used the <a href="https://pypi.org/project/SpeechRecognition/">SpeechRecognition</a> library that allows us to use the microphone of our computer to convert audio to text. All the code is in the file spelling.py

- Spelling

    The spelling function breaks the sentence into words and spells it letter by letter, and when it reaches the end of a word, it spells it out in full

- Syllables
    
    Syllables function has a menu containing all the conjugations of letters and syllables together with their respective sounds.

- Meaning

    This function by means of websracping looks up the meaning of a word in the <a href="https://dem.colmex.mx/">DEM</a> dictionary and tells us its meaning with its respective examples, although if it does not find it, it tells you search alternatives. For this function I used the <a href="https://pypi.org/project/beautifulsoup4/">BeautifulSoup4</a> library for web scraping as well as <a href="https://pypi.org/project/pyttsx3/">pyttsx3</a> to convert text to audio.

---

<h3>Requirements</h3>
<p>

- It is important not to delete the executable file from the folder, as this will cause errors. The best option is to create a shortcut and move it to the desktop or anywhere else you want to place it.

- To have a good performance of the application I recommend downloading <b>"Microsoft Sabina Desktop - Spanish (Mexico)"</b> which is a voice provided by Microsoft for the devices.
</p>

<h4>How to download "Microsoft Sabina Desktop - Spanish (Mexico)".</h4>
<p>In order to download the necessary voice for the program, the first thing to do is to go to:</p>

**Settings> Time and language> Voice> Manage voices> Add voices**

In the search bar type Spanish and download the one that says "Spanish (Mexico)". And with that, everything would be ready to use the application correctly and avoid any pronunciation error.

<h4>If you wish to contribute to the development of the application:</h4>

- **First clone the repository**

        git clone https://github.com/GeimerDroiid/Dictionary.git

- **Then create a branch with your user name**

        git checkout -b <UserName>

- **And finally install the requirements**

        py pip install -r requirements.txt

---

<h3>Contribution</h3>
Pull requests are welcome, I would appreciate your support to contribute to a better development of this application. For major changes, please open an issue to discuss what you would like to change.
