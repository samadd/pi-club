import os
import random
from time import sleep
from gpiozero import Button

button = Button(2)

farts = ['fart1.wav', 'fart2.wav', 'fart3.wav']

while True:
  button.wait_for_press()
  fart = random.choice(farts)
  os.system("aplay fartsounds/{0}".format(fart))
  sleep(2)
