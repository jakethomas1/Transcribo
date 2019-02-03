# VoicetoText

README.md for totext.py

totext.py is a python3 script using Google Speech Recognition API 

jakethomas1.com
github.com/jakethomas1.com
February 1, 2019

Instructions: (must have pip3 already installed)
  first acquire dependencies:
    sudo pip3 install SpeechRecognition
    sudo pip3 install pydub
    
Then create a file named [wholeaudio.wav] and place it in a directory such that: 
  if this script were saved in /home/user/Documents [wholeaudio.wav] would be saved in /home/user/Documents/Audio

Run:
  python3 totext.py

Output:
  Console output will include the filenames of sliced portions given max size of each slice (~25s) 
  Speech to text output will be saved in the directory where [totext.py] is saved in the file named [rawfile.txt]

*Note the speech to text api is not flawless and will require proofreading*
