from numpy import genfromtxt
from keyboard import Keyboard

# using numpy for easier csv parsing
steps = genfromtxt('input.txt', delimiter=',', dtype='str', autostrip=True)

keyboard = Keyboard()
keyboard.apply_steps(steps)

print keyboard.get_code()