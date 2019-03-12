import string

# Function takes 3 variables to encrypt or decrypt the message

def encrypt_decrypt(m, a, k):
    '''

    :param m: str
    :param a: str
    :param k: str
    :return:
    '''
    translation_table = m.maketrans(a, k)
    encrypt_decrypt_message = m.translate(translation_table)
    print(encrypt_decrypt_message)
