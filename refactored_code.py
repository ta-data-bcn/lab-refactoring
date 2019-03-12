
# Importing random, string and collections libraries
import alphabet
import encryption




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

