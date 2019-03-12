import alphabet


def encrypt_decrypt(m, a, k):
    '''
    Function takes 3 variables (a message, an alphabet, and shifted or randomized alphabet
    to encrypt or decrypt the message
    :param m: str
    :param a: str
    :param k: str
    :return:
    '''
    translation_table = m.maketrans(a, k)
    encrypt_decrypt_message = m.translate(translation_table)
    print(encrypt_decrypt_message)



def return_message_encrypted(alph, key):
    '''
    Function asks for one of two encryption methods and returns encrypted message using selected method
    :param alph: str
    :param key: str
    :return: str
    '''
    choice = input("Type 1 for Caesarean cypher. \nType 2 for Translation table")
    if choice != "1" and choice != "2":
        print("Only two methods available: 1 or 2")
    else:
        message = input("What is your message ")
        if choice == "1":
            key = alphabet.shuffle_caesarian()
        encrypted_message = encrypt_decrypt(message, alph, key)
        print(encrypted_message)

def return_message_decrypted(alph, key):
    '''
    Function asks for one of two encryption methods and returns encrypted message using selected method
    :param alph: str
    :param key: str
    :return: str

    '''
    choice = input("Type 1 for Caesarean cypher. \nType 2 for Translation table")
    if choice != "1" and choice != "2":
        print("Only two methods available: 1 or 2")
    else:
        message = input("What is your message ")
        if choice == "1":
            key = alphabet.shuffle_caesarian()
        decrypted_message = encrypt_decrypt(message, key, alph)
        print(decrypted_message)



