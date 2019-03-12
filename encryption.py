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



def encrypt_message():
    choice = input("Type 1 for Caesarean cypher. \nType 2 for Translation table ")
    message = input("What is your message ")
    if choice == "1":
        key_caesar = alphabet.shuffle_caesarian()
        e = encrypt_decrypt(message, alph, key_caesar)
    elif choice == "2":
        e = encrypt_decrypt(message, alph, key)
    else:
        print("Only two methods available: 1 or 2")
    return e

def decrypt_message():
    choice = input("Type 1 for Caesarean cypher. \nType 2 for Translation table ")
    message = input("What is your message ")
    global alph
    global key
    if choice == "1":
        key_caesar = alphabet.shuffle_caesarian()
        d = encrypt_decrypt(message, key_caesar, alph)
    elif choice == "2":
        d = encrypt_decrypt(message, key, alph)
    else:
        print("Only two methods available: 1 or 2")
    return d