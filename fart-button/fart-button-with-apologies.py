import os
import random
from gpiozero import Button
from signal import pause

button = Button(2)

farts = os.listdir('farts')
apologies = os.listdir('apologies')

def make_fart():
    fart = random.choice(farts)
    os.system("aplay farts/{0}".format(fart))

def apologise():
    apology = random.choice(apologies)
    os.system("aplay apologies/{0}".format(apology))

button.when_pressed = make_fart
button.when_released = apologise

pause()