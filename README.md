<h1>Dictionary</h1>
<p>
 <a href="https://discord.com/channels/@me/GeimerDroiid#0359">
     <img alt="GeimerDroiid | Discord" width="24px" align="right" raw=true HSPACE="5" src="https://raw.githubusercontent.com/GeimerDroiid/GeimerDroiid/main/assets/discord.svg"></a>
 <a href="https://open.spotify.com/playlist/6eDl0FX1pNcaFXgYIBOobX?si=aewrQ2nJTuSgkMSip3d8-Q&utm_source=copy-link">
     <img alt="GeimerDroiid | Spotify" width="24px" align="right" raw=true HSPACE="5" src="https://raw.githubusercontent.com/GeimerDroiid/GeimerDroiid/main/assets/spotify.svg"></a>
 <a href="https://github.com/GeimerDroiid">
    <img alt="GeimerDroiid | Github" width="24px" align="right" raw=true HSPACE="5" src="https://raw.githubusercontent.com/GeimerDroiid/GeimerDroiid/main/assets/github.svg"></a>
 <a href="mailto:jmanuelhv9@gmail.com">
    <img alt="Email | jmanuelhv9@gmail.com" width="24px" align="right" raw=true HSPACE="5" src="https://raw.githubusercontent.com/GeimerDroiid/GeimerDroiid/main/assets/gmail.svg"></a>
</p>
<h3>About</h3>
<p align="left">
Application focused on searching the meaning of words through web scraping, besides having more functions such as Dictation, Spelling and Syllables.<br>
I created this application as a way to test the knowledge that I have started to acquire so I decided to make this dictionary with some basic functions like spelling but from there more ideas came up, like implementing a method that would tell me the meanings of the words that I didn't understand, or a way in which I didn't have to write the word and just by telling the computer I could write it. When I created this application I was just starting to learn Python (it is the language I used for this application) so I may have a lot of bad practices in the code that I am correcting for future versions. During the creation of this application I learned how to make user interfaces, I dabbled a bit in web scraping and besides investigating a method with which I can change text to sound and play it also at the end I used object oriented programming to facilitate the creation of the interface.
<div align="center">
<img alt="Dictionary | GUI" width="720px" align="center" src="assets/img-readme/gui.png">
</div>

---

<h3>Functions</h3>
<h4>Dictate</h4>
<p align="left">
For the creation of the dictation function I looked for a way to access the device's microphone. For this I relied on the <a href="https://pypi.org/project/SpeechRecognition/">speech_recognition</a> library which listens through the microphone and then converts the audio to text.
Then I store the text in a variable and insert it into the bar so that the user can apply any of the other functions on the collected text. You can see all this in the line 9 and in the dictate function inside the code. 
</p>
<img alt="Dictionary | Dictate" width="180px" align="center" src="assets/img-readme/dictate.png">

<h4>Spell</h4>
<p align="left">
The function of spelling I made it with a for loop, by means of which I iterate the word received in the bar. When iterating I store the word letter by letter and when we detect a space within the string we ask it to tell us the complete word and so repeatedly until spelling all the text entered in the bar.
You can see more in the spell function at line 47 of the code
</p>
<img alt="Dictionary | Spell" width="180px" align="center" src="assets/img-readme/spell.png">

<h4>Syllables</h4>
<p align="left">
In order to make the syllables function I decided to use POO since at that time it was the subject I was looking at and it would make it easier for me to create buttons, plus it was a way to test the knowledge I had acquired. This function and the whole interface was made with the <a href="https://docs.python.org/3/library/tkinter.html">tkinter</a> library as well as <a href="https://pypi.org/project/pyttsx3/">pyttsx3</a> for text-based sound playback. You can see more from line 61 of the code
</p>
<img alt="Dictionary | Syllables" width="180px" align="center" src="assets/img-readme/syllables.png">

<h4>Meaning</h4>
<p align="left">
The meaning function was a bit more difficult since I had to do some research and learn a bit of webscraping to make it work, but in the end I managed to find a method with which I could get the result I wanted for this I used the <a href="https://dem.colmex.mx/">DEM</a> dictionary because it has a little simpler definition and examples, I also relied on the <a href="https://pypi.org/project/beautifulsoup4/">BeautifulSoup</a> library and <a href="https://docs.python-requests.org/en/latest/">request</a> to get the text of the results of the dictionary. I leave the webscraping.py file so you can see in an easier way how I did the webscraping part.
</p>
<img alt="Dictionary | Meaning" width="180px" align="center" src="assets/img-readme/meaning.png">

---

<h3>Requirements</h3>
<p align="left">
To have a good performance of the application I recommend downloading "Microsoft Sabina Desktop - Spanish (Mexico)" which is a voice provided by Microsoft for the devices.<br>
<h3>How to download "Microsoft Sabina Desktop - Spanish (Mexico)".</h3>
In order to download the necessary voice for the program, the first thing to do is to go to:
</p>

- Settings

- Time and language

- Voice

- Manage voices

- Add voices

<p align="left">
In the search bar type Spanish and download the one that says "Spanish (Mexico)". And with that, everything would be ready to use the application correctly and avoid any pronunciation error. 
<p>
 
**If you want to download the dependencies to be able to edit the code use the command:**

    py pip install -r requirements.txt
 
---

<h3>Contribution</h3>
<p align="left">
Pull requests are welcome, I would appreciate your support to contribute to a better development of this application. For major changes, please open an issue to discuss what you would like to change.
</p>
