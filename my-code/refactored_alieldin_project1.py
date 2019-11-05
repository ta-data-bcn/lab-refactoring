#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def encrypt():
    sentence_to_encrypt = input("Input a sentance that you want to encrypt:\n")
    enclist=[]
    for letters in sentence_to_encrypt:
        encnumber = ord(letters) * 39
        enclist.append(encnumber)
    print ("\033[1m"+"\033[94m"+"Your encrypted message is:")
    for numbers in enclist: 
        print(numbers, end='')
        print(" ", end='')
    print("\n"+"\033[0m")

def decrypt():
    sentence_to_decrypt = input("Input a code that you want to decrypt:\n")
    x = sentence_to_decrypt.split(' ')
    dec_sentence=""
    for numbers in x:
        x= chr(int(int(numbers) / 39))
        dec_sentence = dec_sentence + x
    print("\033[1m"+"\033[92m"+"Your dycrypted message is:\n" f"{dec_sentence}"+"\033[0m"+"\n")
    
print("\033[1m"+"\033[94m"+"Hello user :)\nWelcome to Message Encryption and Decryption")
print("You can either choose to encrypt a message or decrypt a message that was encrypted using the same interface.\n")
print("\033[1m"+"\033[91m"+"Please follow the instructions below:")
print("- Answer the first question to choose either to encrypt or decrypt a message.")
print("- Type in your message and press 'enter' and the interface will give you either the encrypted message\n   or the decrypted message depending on which one you chose."+"\033[0m")
print("\033[1m"+"\nThat being said, let's begin :)\n"+"\033[0m")

choice = input("Do you want to encrypt or decrypt a message?\nPlease entre ""\033[1m" + "'encrypt' or 'decrypt': "+"\033[0m")
if choice == 'encrypt':
    encrypt()
elif choice == 'decrypt':
    decrypt()
else:
    while True:
        choice = input("Do you want to encrypt or decrypt a message?\nPlease entre ""\033[1m" + "'encrypt' or 'decrypt': "+"\033[0m")
        if choice == 'encrypt':
            encrypt()
        elif choice == 'decrypt':
            decrypt()
        else:
            print("\033[1m"+"\033[91m"+"Your input is incorrect, please try again!"+"\033[0m")


# In[ ]:




