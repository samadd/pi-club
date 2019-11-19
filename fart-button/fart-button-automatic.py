import os
import random
from gpiozero import Button

button = Button(2)

farts = os.listdir('farts')

def make_fart:
  fart = random.choice(farts)
  os.system("aplay farts/{0}".format(fart))

button.when_pressed = make_fart
  
pause()