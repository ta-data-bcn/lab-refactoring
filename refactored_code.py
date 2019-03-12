import alphabet
import encryption


choose_action=0
key = alphabet.shuffle_alphabet()
while choose_action != 3:
    choose_action = input("Type 1 for encrypting a message. \nType 2 for decripting a message. \nType 3 to exit the program ")
    if choose_action == "1":
        choose_encryption = input("Type 1 for Caesarean cypher. \nType 2 for Translation table ")
        message = input("What is your message ")
        if choose_encryption == "1":
            key_caesar = alphabet.shuffle_caesarian()
            encryption.encrypt_decrypt(message, alphabet, key_caesar)
        elif choose_encryption == "2":
            encryption.encrypt_decrypt(message, alphabet, key)
        else:
            print("Only two methods available: 1 or 2")
    elif choose_action == "2":
        choose_encryption = input("Type 1 for Caesarean cypher. \nType 2 for Translation table ")
        message = input("What is your message ")
        if choose_encryption == "1":
            key_caesar = alphabet.shuffle_caesarian()
            encryption.encrypt_decrypt(message, key_caesar, alphabet)
        elif choose_encryption == "2":
            encryption.encrypt_decrypt(message, key, alphabet)
        else:
            print("Only two methods available: 1 or 2")
    elif choose_action == "3":
        break
    else:
        print("Options are only 1, 2 or 3")

