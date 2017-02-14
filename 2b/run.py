from numpy import genfromtxt
from keyboard import FancyKeyboard

# using numpy for easier csv parsing
steps = genfromtxt('input.txt', delimiter=',', dtype='str', autostrip=True)

keyboard = FancyKeyboard()
keyboard.apply_steps(steps)

print keyboard.get_code()