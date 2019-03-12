import random
import string
from collections import deque

def retrieve_alphabet():
    '''

    :return:
    '''
    alphabet = string.printable.split(' ')[0]
    return alphabet

# Function that allows to create your own key with any characters that a language might use
# if you provide a list of characters to be used

def shuffle_alphabet():
    '''

    :return:
    '''
    key_to_shuffle = list(retrieve_alphabet())
    random.shuffle(key_to_shuffle)
    key = ''.join(key_to_shuffle)
    return key


def getKey():
    '''

    :return:
    '''
    key = 0
    while True:
        print(f'What number do you want to use for the cypher between -{len(retrieve_alphabet())} and {len(retrieve_alphabet())}')
        key_provided = int(input())
        if key_provided >= (-1 * len(retrieve_alphabet())) and key_provided <= len(retrieve_alphabet()):
            return key_provided

# Function to create Caesarian cypher translation table using the key
def shuffle_caesarian():
    '''
    Function takes alphabet and shuffles it to the right or to the left by the user
    provided key and returns a shuffled alphabet
    :return: str
    '''
    d = deque(retrieve_alphabet())
    d.rotate(getKey())
    key_caesar = ''.join(list(d))
    return key_caesar