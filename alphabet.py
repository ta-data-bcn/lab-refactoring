import random
import string
from collections import deque


def retrieve_alphabet():
    '''
    Retrieves ASCII alphabet, splits it at the space character and returns the first string containing
    only non whitespace characters
    :return: str
    '''
    alphabet = string.printable.split(' ')[0]
    return alphabet


def shuffle_alphabet():
    '''
    Takes the alphabet from the retrieve_alphabet function and creates a new alphabet shuffled randomly
    :return: str
    '''
    key_to_shuffle = list(retrieve_alphabet())
    random.shuffle(key_to_shuffle)
    key = ''.join(key_to_shuffle)
    return key


def getKey():
    '''
    Asks the user to introduce a key for later use within the length of the alphabet
    :return: int
    '''
    key = 0
    while True:
        print(f'What number do you want to use for the cypher between -{len(retrieve_alphabet())} and {len(retrieve_alphabet())}')
        key_provided = int(input())
        if key_provided >= (-1 * len(retrieve_alphabet())) and key_provided <= len(retrieve_alphabet()):
            return key_provided


def shuffle_caesarian():
    '''
    Function takes alphabet and shuffles it to the right or to the left by the user
    provided key and returns a shuffled alphabet
    :return: str
    '''
    d = deque(retrieve_alphabet())
    d.rotate(getKey())
    key = ''.join(list(d))
    return key