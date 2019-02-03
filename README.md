# README.md -> totext.py

totext.py is a python3 script using Google Speech Recognition API <br />

jakethomas1.com <br />
github.com/jakethomas1.com<br />
February 1, 2019<br />

<h3> Instructions: <h3> 
(must have pip3 installed)<br />
first acquire dependencies:<br />
&nbsp&nbsp  sudo pip3 install SpeechRecognition<br />
&nbsp&nbsp sudo pip3 install pydub<br />  
    
Then create a file named [wholeaudio.wav] and place it in a directory such that:<br /> 
&nbsp&nbsp  if this script were saved in /home/user/Documents [wholeaudio.wav] would be saved in /home/user/Documents/Audio <br />

Run: <br />
&nbsp&nbsp  python3 totext.py<br />

Output:<br />
&nbsp&nbsp  Console output will include the filenames of sliced portions given max size of each slice (~25s)<br />
&nbsp&nbsp  Speech to text output will be saved in the directory where [totext.py] is saved in the file named [rawfile.txt]<br />

*Note the speech to text api is not flawless and will require proofreading*
