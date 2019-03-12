import  my_library as my

# Actual program

def enigma():
    """

    :return:
    """
    selection = input("Do you want to encrypt or decrypt? E/D: ")
    if selection == 'E' or selection == 'e':
        res_rot1 = my.rot1()
        res_rot2 = my.rot2()
        res_rot3 = my.rot3()
        message = my.text()
        loop1 = my.crypto(message, res_rot1)
        loop2 = my.crypto(loop1, res_rot2 )
        loop3 = my.crypto(loop2, res_rot3)
        loop4 = my.crypto(loop3, res_rot2)
        print("Your encrypted message is:",my.crypto(loop4,res_rot1))
    elif selection == 'D' or selection == 'd':
            in_res_rot1 = my.in_rot1()
            in_res_rot2 = my.in_rot2()
            in_res_rot3 = my.in_rot3()
            in_message = my.in_text()
            in_loop1 = my.crypto(in_message, in_res_rot1)
            in_loop2 = my.crypto(in_loop1, in_res_rot2 )
            in_loop3 = my.crypto(in_loop2, in_res_rot3)
            in_loop4 = my.crypto(in_loop3, in_res_rot2)
            print("Your decrypted message is:",my.crypto(in_loop4,in_res_rot1))
    else:
        print(f"You tiped {selection}, please type E/D")
        enigma()
enigma()

























