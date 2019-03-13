import  my_library as my


def enigma():
    """

    :return: This function returns the message encrypted or decrypted using the functions from "my_library"
    """
    selection = input("Do you want to encrypt or decrypt? E/D: ")
    # Runs if user selects E (Encrypt)
    if selection == 'E' or selection == 'e':
        encrypt_rot1 = my.rot1()
        encrypt_rot2 = my.rot2()
        enrypt_rot3 = my.rot3()
        message = my.text()
        loop1 = my.crypto(message, encrypt_rot1)
        loop2 = my.crypto(loop1, encrypt_rot2)
        loop3 = my.crypto(loop2, enrypt_rot3)
        loop4 = my.crypto(loop3, encrypt_rot2)
        print("Your encrypted message is:", my.crypto(loop4, encrypt_rot1))
    # Runs if user selects D (Decrypt)
    elif selection == 'D' or selection == 'd':
        decrypt_rot1 = my.in_rot1()
        decrypt_rot2 = my.in_rot2()
        decrypt_rot3 = my.in_rot3()
        de_message = my.in_text()
        de_loop1 = my.crypto(de_message, decrypt_rot1)
        de_loop2 = my.crypto(de_loop1, decrypt_rot2)
        de_loop3 = my.crypto(de_loop2, decrypt_rot3)
        de_loop4 = my.crypto(de_loop3, decrypt_rot2)
        print("Your decrypted message is:", my.crypto(de_loop4, decrypt_rot1))
    # Runs if user types other thing than E or D
    else:
        print(f"You tiped {selection}, please type E/D")
        enigma()
enigma()