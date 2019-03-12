import random
import string
from collections import deque

# getting the cleaned ascii
alph = string.printable
alphabet_split = alph.split(" ")
alphabet = alphabet_split[0]

# Function that allows to create your own key with any characters that a language might use
# if you provide a list of characters to be used

def shuffle_alphabet(base = alphabet):
    key_to_shuffle = list(base)
    random.shuffle(key_to_shuffle)
    key = ''.join(key_to_shuffle)
    return key

# Function to create Caesarian cypher translation table using the key
def shuffle_caesarian(base=alphabet):
    d = deque(alphabet)
    d.rotate(getKey())
    key_caesar = ''.join(list(d))
    return key_caesar