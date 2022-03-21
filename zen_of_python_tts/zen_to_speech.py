import gtts
from playsound import playsound

with open('zen.txt') as zen:
    speech = gtts.gTTS(zen.read())
    speech.save('zen.mp3')

playsound('zen.mp3')
