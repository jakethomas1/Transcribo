#Jake Thomas
#February 1st, 2019
#Speech to text with any size .wav file 
#Use README.txt for troubleshoot

import speech_recognition as sr
from os import path
from pydub import AudioSegment

max_slice = 20000 #25000ms = 25s
pathtoaudio = "Audio"

open('rawfile.txt', 'w+').close() #THIS WILL MAKE SURE EMPTY FILE EXISTS
sound = AudioSegment.from_file(pathtoaudio + "/wholeaudio.wav")
lengthms = len(sound)
divs = lengthms/max_slice
divs = int(divs) + 1
r = sr.Recognizer()

print("\n\nMAX CLIP LENGTH: ["+ str(max_slice/1000) + "s]")
print("Portioning [.../Audio/wholeaudio.wav] ..\n")

for i in range(divs):
  pthn = pathtoaudio + "/target" + str(i) + ".wav"  
  if divs-1 == i:
    partial_section = sound[-(lengthms-(i*max_slice)):] 
  else:
    partial_section = sound[i*max_slice:((i+1)*max_slice)]
  partial_section.export(path.join(path.dirname(path.realpath(__file__)),pthn),format="wav") 
  print(pthn)
for i in range(divs):
  pathname = (pathtoaudio + "/target" + str(i) + ".wav")
  AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), pathname)
  print(AUDIO_FILE)
  with sr.AudioFile(AUDIO_FILE) as source:
    print("\nConverting target" + str(i) + ".wav\n..\n")
    audio = r.record(source)
  with open('rawfile.txt', 'a') as myfile:
    try: 
      myfile.write(r.recognize_google(audio,))
    except:
      pass
    myfile.write(" // ")
    #myfile.write(r.recognize_google(audio))
print("--Finshed\nSaved to [rawfile.txt]\n")

#"/home/jikjik/Documents/develop/Audio/target.wav" 


