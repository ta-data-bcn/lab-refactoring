#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("\033[1m"+"\033[94m"+"Hello user :)\nWelcome to Message Encryption and Decryption")
print("You can either choose to encrypt a message or decrypt a message that was encrypted using the same interface.\n")
print("\033[1m"+"\033[91m"+"Please follow the instructions below:")
print("- Answer the first question to choose either to encrypt or decrypt a message.")
print("- If you enter a wrong input (encrypt/decrypt) you have only four trials after which you will have to run the code again.")
print("- Type in your message and press 'enter' and the interface will give you either the encrypted message\n   or the decrypted message depending on which one you chose.")
print("- The interface will terminate after your message is encrypted/decrypted.\n- To encrypt/decrypt another message, you will have to run the code again."+"\033[0m")
print("\033[1m"+"\nThat being said, let's begin :)\n"+"\033[0m")

choice = input("Do you want to encrypt or decrypt a message?\nPlease entre ""\033[1m" + "'encrypt' or 'decrypt': "+"\033[0m")
if choice == 'encrypt':
    def encrypt(user_input):
        enclist=[]
        for letters in user_input:
            encnumber = ord(letters) * 39
            enclist.append(encnumber)
        print ("\033[1m"+"\033[94m"+"Your encrypted message is:")
        for numbers in enclist: 
            print(numbers, end='')
            print(" ", end='')
    def main1 ():
        sentence_to_encrypt = input("Input a sentance that you want to encrypt:\n")
        encrypt(sentence_to_encrypt)
    if __name__ == '__main__':
        main1 ()
    
elif choice == 'decrypt':
    def decrypt(user_input2):
        dec_sentence=""
        for numbers in user_input2:
            x= int(numbers)
            x= int(x / 39)
            x= chr(x)
            dec_sentence = dec_sentence + x
        print("\033[1m"+"\033[92m"+"Your dycrypted message is:")
        print(dec_sentence)
        
    def main2():
        sentence_to_decrypt = input("Input a code that you want to decrypt:\n")
        x = sentence_to_decrypt.split(' ')
        decrypt(x)
    if __name__ == "__main__":
        main2 ()
    
else:
    print("Your input is incorrect, please try again!")
    choice = input("Do you want to encrypt or decrypt a message?\nPlease entre ""\033[1m" + "'encrypt' or 'decrypt': "+"\033[0m")
    if choice == 'encrypt':
        def encrypt(user_input):
            enclist=[]
            for letters in user_input:
                encnumber = ord(letters) * 39
                enclist.append(encnumber)
            print ("\033[1m"+"\033[94m"+"Your encrypted message is:")
            for numbers in enclist: 
                print(numbers, end='')
                print(" ", end='')
        def main1 ():
            sentence_to_encrypt = input("Input a sentance that you want to encrypt: \n")
            encrypt(sentence_to_encrypt)
        if __name__ == '__main__':
            main1 ()
    
    elif choice == 'decrypt':
        def decrypt(user_input2):
            dec_sentence=""
            for numbers in user_input2:
                x= int(numbers)
                x= int(x / 39)
                x= chr(x)
                dec_sentence = dec_sentence + x
            print("\033[1m"+"\033[92m"+"Your dycrypted message is:")
            print(dec_sentence)
        
        def main2():
            sentence_to_decrypt = input("Input a code that you want to decrypt: \n")
            x = sentence_to_decrypt.split(' ')
            decrypt(x)
        if __name__ == "__main__":
            main2 ()
    else:
        print("Your input is incorrect, please try again! (2)")
        choice = input("Do you want to encrypt or decrypt a message?\nPlease entre ""\033[1m" + "'encrypt' or 'decrypt': "+"\033[0m")
        if choice == 'encrypt':
            def encrypt(user_input):
                enclist=[]
                for letters in user_input:
                    encnumber = ord(letters) * 39
                    enclist.append(encnumber)
                print ("\033[1m"+"\033[94m"+"Your encrypted message is:")
                for numbers in enclist: 
                    print(numbers, end='')
                    print(" ", end='')
            def main1 ():
                sentence_to_encrypt = input("Input a sentance that you want to encrypt: \n")
                encrypt(sentence_to_encrypt)
            if __name__ == '__main__':
                main1 ()
    
        elif choice == 'decrypt':
            def decrypt(user_input2):
                dec_sentence=""
                for numbers in user_input2:
                    x= int(numbers)
                    x= int(x / 39)
                    x= chr(x)
                    dec_sentence = dec_sentence + x
                print("\033[1m"+"\033[92m"+"Your dycrypted message is:")
                print(dec_sentence)
        
            def main2():
                sentence_to_decrypt = input("Input a code that you want to decrypt: \n")
                x = sentence_to_decrypt.split(' ')
                decrypt(x)
            if __name__ == "__main__":
                main2 ()
        else:
            print("Your input is incorrect, please try again! (1)")
            choice = input("Do you want to encrypt or decrypt a message?\nPlease entre ""\033[1m" + "'encrypt' or 'decrypt': "+"\033[0m")
            if choice == 'encrypt':
                def encrypt(user_input):
                    enclist=[]
                    for letters in user_input:
                        encnumber = ord(letters) * 39
                        enclist.append(encnumber)
                    print ("\033[1m"+"\033[94m"+"Your encrypted message is:")
                    for numbers in enclist: 
                        print(numbers, end='')
                        print(" ", end='')
                def main1 ():
                    sentence_to_encrypt = input("Input a sentance that you want to encrypt: \n")
                    encrypt(sentence_to_encrypt)
                if __name__ == '__main__':
                    main1 ()
    
            elif choice == 'decrypt':
                def decrypt(user_input2):
                    dec_sentence=""
                    for numbers in user_input2:
                        x= int(numbers)
                        x= int(x / 39)
                        x= chr(x)
                        dec_sentence = dec_sentence + x
                    print("\033[1m"+"\033[92m"+"Your dycrypted message is:")
                    print(dec_sentence)
        
                def main2():
                    sentence_to_decrypt = input("Input a code that you want to decrypt: \n")
                    x = sentence_to_decrypt.split(' ')
                    decrypt(x)
                if __name__ == "__main__":
                    main2 ()
            else:
                print("Your input was incorrect, again!\n""\033[1m"+"\033[91m"+"This was your last try, please run the code again.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




