
# Importing random, string and collections libraries
import random
import string
from collections import deque


# In[2]:


# getting the cleaned ascii
alph = string.printable
alphabet_split = alph.split(" ")
alphabet = alphabet_split[0]


# In[3]:


# Function that allows to create your own key with any characters that a language might use 
# if you provide a list of characters to be used

def shuffle_alphabet(base = alphabet):
    key_to_shuffle = list(base)
    random.shuffle(key_to_shuffle)
    key = ''.join(key_to_shuffle)
    return key


# In[4]:


# Finding maximum key size for Caesar cypher
max_key_size = len(alphabet)


# In[5]:


# Function to get ask for key to use in Caesar cypher

def getKey():
    key = 0
    while True:
        print(f'What number do you want to use for the cypher between -{max_key_size} and {max_key_size}) ')
        key_c = int(input())
        if key_c >= (-1 * max_key_size) and key_c <= max_key_size:
            return key_c


# In[6]:


# Function to create Caesarian cypher translation table using the key
def shuffle_caesarian(base=alphabet):
    d = deque(alphabet)
    d.rotate(getKey())
    key_caesar = ''.join(list(d))
    return key_caesar


# In[7]:


# Function takes 3 variables to encrypt or decrypt the message

def encrypt_decrypt(m, a, k):
    translation_table = m.maketrans(a, k)
    encrypt_decrypt_message = m.translate(translation_table)
    print(encrypt_decrypt_message)


# In[ ]:


choose_action=0
key = shuffle_alphabet()
while choose_action != 3:
    choose_action = input("Type 1 for encrypting a message. \nType 2 for decripting a message. \nType 3 to exit the program ")
    if choose_action == "1":
        choose_encryption = input("Type 1 for Caesarean cypher. \nType 2 for Translation table ")
        message = input("What is your message ")
        if choose_encryption == "1":
            #caesarian(message, alphabet, alphabet_caesar)
            key_caesar = shuffle_caesarian()
            encrypt_decrypt(message, alphabet, key_caesar)
        elif choose_encryption == "2":
            encrypt_decrypt(message, alphabet, key)
        else:
            print("Only two methods available: 1 or 2")
    elif choose_action == "2":
        choose_encryption = input("Type 1 for Caesarean cypher. \nType 2 for Translation table ")
        message = input("What is your message ")
        if choose_encryption == "1":
            key_caesar = shuffle_caesarian()
            encrypt_decrypt(message, key_caesar, alphabet)
            #caesarian(message, alphabet, alphabet_caesar)
        elif choose_encryption == "2":
            encrypt_decrypt(message, key, alphabet)
        else:
            print("Only two methods available: 1 or 2")
    elif choose_action == "3":
        break
    else:
        print("Options are only 1, 2 or 3")

