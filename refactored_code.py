import alphabet
import encryption

alph = alphabet.retrieve_alphabet()
key = alphabet.shuffle_alphabet()
choose_action = 0
while choose_action != 3:
    choose_action = input("Type 1 for encrypting a message. \nType 2 for decripting a message. \nType 3 to exit the program ")
    if choose_action == "1":
        encryption.return_message_encrypted(alph, key)
    elif choose_action == "2":
        encryption.return_message_decrypted(alph, key)
    elif choose_action == "3":
        break
    else:
        print("Options are only 1, 2 or 3")
