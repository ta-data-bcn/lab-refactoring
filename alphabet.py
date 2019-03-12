import random
import string
from collections import deque

def retrieve_alphabet():
    alphabet = string.printable.split(' ')[0]
    return alphabet

# Function that allows to create your own key with any characters that a language might use
# if you provide a list of characters to be used

def shuffle_alphabet():
    key_to_shuffle = list(retrieve_alphabet())
    random.shuffle(key_to_shuffle)
    key = ''.join(key_to_shuffle)
    return key


def getKey():
    key = 0
    while True:
        print(f'What number do you want to use for the cypher between -{len(retrieve_alphabet())} and {len(retrieve_alphabet())}')
        key_c = int(input())
        if key_c >= (-1 * len(retrieve_alphabet())) and key_c <= len(retrieve_alphabet()):
            return key_c

# Function to create Caesarian cypher translation table using the key
def shuffle_caesarian(base = alphabet):
    d = deque(retrieve_alphabet())
    d.rotate(getKey())
    key_caesar = ''.join(list(d))
    return key_caesar