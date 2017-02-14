from numpy import genfromtxt
from navigator import Navigator

# using numpy for easier csv parsing
steps = genfromtxt('input.txt', delimiter=',', dtype='str', autostrip=True)

nav = Navigator()
nav.apply_steps(steps)

print nav.get_distance_to_first_duplicate()