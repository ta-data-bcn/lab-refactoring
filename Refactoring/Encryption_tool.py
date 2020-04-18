# Encryption function
def encryption():
    message_to_encrypt = str(input("Please insert your message to encrypt: "))
    s = int(input("Please insert the key to use for cipher "))
    result = ""      
    # Encrypting text 
    for i in range(len(message_to_encrypt)): 
        char = message_to_encrypt[i]   
        # Encrypt uppercase characters according to ASCII codes
        if (char.isupper()): 
            result += chr((ord(char) + s - 65) % 26 + 65)  
        # Encrypt lowercase characters according to ASCII codes
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97)
    return print(f"Your encrypted text is: {result}")

# Decryption function
def decryption():
    txt_result = "" 
    message_to_decrypt = str(input("Please insert your message to decrypt: "))
    s = int(input("Please insert the key to use for decipher "))  
    # decrypting text 
    for i in range(len(message_to_decrypt)): 
        char = message_to_decrypt[i]   
        # Decrypt uppercase characters 
        if (char.isupper()): 
            txt_result += chr((ord(char) - s - 65) % 26 + 65)  
        # Decrypt lowercase characters 
        else: 
            txt_result += chr((ord(char) - s- 97) % 26 + 97)   
    return print(f"your decrypted text is {txt_result}")

# Welcome and selecting function
hi = str(input("Ave Caesar! Please insert (e) for (e)ncryption or (d) for decryption: "))
if hi == "e":
    encryption()
elif hi == "d":
    decryption()
else:
    print("Couldn't perform. Please insert (e) or (d). Ad astra per aspera!")

print("Thanks for using the cypher tool. But remember 'Acta deos numquam mortalia fallunt.'")