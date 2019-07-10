"""

PROJECT - 1 - Message Encryption & Decryption

1. Title and program description
2. Prompt for encryption or decryption
3. Prompt the user for the message he wants to envrypt / decrypt
4. Prompt the user for the picture used to encrypt (GUI prompt)
5. Save variables for message and path
6. Square crop, pixelate (max mosaic 64x64) and save the picture.
7. Get values for each pixel in the image and convert it to list
8. Sum The RGB values to get a number
9. Iterate each letter of the message by index, depending with the relative pixel index
10. Create a string again and print the message encrypted /decrypred

FUNCTIONS:

def ask_user_encrypt_or_decrypt:
def ask_for_the picture:
def image_to_values()
def encrypt:
def decrypt:


"""

from functions import WhatToDo                                    # import all functions needed

no_quit = "1"
no_errors = "1"

while no_quit == "1" or no_errors == "1":

    get_user_answer, get_message, no_errors = WhatToDo.ask_user_encrypt_or_decrypt()         # ask user message

    if no_errors == "0" or no_quit == "0":

        break

    get_user_picture = WhatToDo.ask_for_the_picture()                             # ask user image hash

    get_image_hash = WhatToDo.image_to_values(get_user_picture)                   # convert image to a list

    final_message = WhatToDo.encrypt_or_decrypt(get_message, get_image_hash, get_user_answer)       # encrypt message

    WhatToDo.show_final_message(final_message)                                    # show result

if no_quit == "0":

    print("You Exit the program")

if no_errors == "0":

    print("\nThis is not for you, I don't even think you can read. Bye ")

WhatToDo.ask_user_encrypt_or_decrypt()

print(quit())
