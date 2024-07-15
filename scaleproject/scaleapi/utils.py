import random

# Randomly returns a mode, Inonian and Aeolian have been replaced with their common names Major and Minor respectively
def getScale():
    scales = ['Major', 'Dorian', 'Phryigian', 'Lydian', 'Mixolydian', 
    'Minor', 'Locrian']
    return scales[random.randrange(0, len(scales)-1)]

# Randomly returns a key
def getKey():
    root = ['C', 'D', 'E', 'F', 'G', 'A', 'B'] # Root notes
    mod = ['', 'b', '#'] # Modifiers
    result = root[random.randrange(0, 6)] + mod[random.randrange(0, 2)]
    if (result=='Cb'): result='B'
    elif (result=='B#'): result='C'
    elif (result=='Fb'): result='E'
    elif (result=='E#'): result='F'
    
    return result

# Test Logic Here
# print("Your key is: " + getKey() + ' ' + getScale())