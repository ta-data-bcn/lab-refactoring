import string

# Encryption dictionaries

ALLCHARACTERS = []
ALLCHARACTERS += list(string.printable)

RANDCHARACTERS = ['\n', ':', 'W', '.', '`', '>', '<', 'E', '}', '5', 'i', 'n', 'u', 'X', 'a', '2', ';', '*', '!', 'K', 'U', 'S', '+', 'V', 'Q', 'p', '9', 'P', ',', '?', '7', 'o', '(', 'Z', '#', 'A', '\\', '^', 'I', '=', '$', '4', 'm', 'v', '-', '3', '1', '\x0b', '8', 'H', 'O', '"', 'r', 'T', 'F', 'b', '6', 'z', 'l', 'D', ']', '_', 'q', 'j', '%', "'", 'L', 'R', 'C', '[', 'e', '&', '~', 't', 'k', '@', 'x', 'h', '|', 'G', 's', 'M', 'g', '\t', 'Y', '\r', 'd', '/', ')', 'c', ' ', '\x0c', 'w', 'y', 'N', 'B', '{', 'J', 'f', '0']
RANDCHARACTERS1 = ['{', 'S', '9', '%', 'N', '^', '&', '\x0c', '\r', '7', '\n', 'H', '>', '-', 'A', 'Z', 'y', 'b', '`', ' ', 'n', '<', 'J', '=', 'I', 'D', 'z', 'Y', '*', 'Q', 'e', '}', 'p', 'R', 'k', 'C', '\\', ')', '(', '@', 'G', '1', '#', 'l', 'F', 'L', 'K', '[', 'h', 'E', '$', ';', ']', '_', '2', '5', '8', 'V', '4', 'u', 'x', '6', '0', '!', 'r', 'i', 'a', 'w', "'", 'v', 'o', 'd', 'j', 'M', 't', '|', '/', 'm', 's', 'W', ',', 'U', 'X', ':', '\x0b', 'P', '~', '\t', 'f', 'q', 'O', 'c', '"', '+', 'B', '3', '.', 'T', '?', 'g']
RANDCHARACTERS2 = ['C', 'J', '8', 'u', '.', 'r', '{', 'f', ';', '"', 'Q', 'b', 'm', 'T', '0', 't', '=', ' ', '\t', '(', 'S', "'", '\x0b', '\\', ':', '^', '>', '_', '6', '?', 'l', 'v', 'p', '[', 'c', 's', 'h', 'n', '!', 'L', '7', 'g', '@', 'D', 'G', '<', '\n', 'k', 'w', 'o', ')', 'Z', 'A', 'O', '*', 'R', 'e', ',', '`', 'U', '1', '-', '~', 'j', 'V', '}', 'P', '|', '2', ']', 'M', 'i', '\x0c', 'I', '9', 'x', '4', '5', 'z', 'd', 'a', 'Y', '%', 'F', 'y', '/', '3', 'E', 'H', '#', '+', 'q', 'K', '&', 'N', '$', 'B', '\r', 'X', 'W']
RANDCHARACTERS3 = [')', '!', 'x', '-', 'G', 'l', '>', ';', ',', '{', 'h', '[', 'i', '3', '(', 'r', 'q', '~', 'S', 'R', 'p', 'c', '#', 'n', '$', '=', 's', 'W', '@', '1', 'a', '.', 'I', '*', '2', 'P', 't', 'f', '\x0c', '+', 'e', 'A', 'U', 'k', 'V', 'O', 'Q', 'D', '\x0b', 'N', '<', '/', 'Y', '0', ']', 'K', 'b', 'J', '\t', 'y', '5', '}', '\n', ' ', 'Z', 'T', 'm', 'u', '6', '?', "'", 'C', '|', '7', '_', '`', '^', 'M', 'z', '"', 'E', '%', 'F', '9', 'X', '\r', '8', '&', 'v', 'L', 'o', 'j', ':', 'd', 'B', 'w', 'g', '4', 'H', '\\']

DICTENCRYPTED = {}
DICTENCRYPTED1 = {}
DICTENCRYPTED2 = {}
DICTENCRYPTED3 = {}

for i in range(len(ALLCHARACTERS)):
    DICTENCRYPTED[ALLCHARACTERS[i]] = RANDCHARACTERS[i]
    DICTENCRYPTED1[ALLCHARACTERS[i]] = RANDCHARACTERS1[i]
    DICTENCRYPTED2[ALLCHARACTERS[i]] = RANDCHARACTERS2[i]
    DICTENCRYPTED3[ALLCHARACTERS[i]] = RANDCHARACTERS3[i]

# Decryption dictionaries

DECRYPTEDDICT = {}
DECRYPTEDDICT1 = {}
DECRYPTEDDICT2 = {}
DECRYPTEDDICT3 = {}

for i in range(len(ALLCHARACTERS)):
    DECRYPTEDDICT[RANDCHARACTERS[i]] = ALLCHARACTERS[i]
    DECRYPTEDDICT1[RANDCHARACTERS1[i]] = ALLCHARACTERS[i]
    DECRYPTEDDICT2[RANDCHARACTERS2[i]] = ALLCHARACTERS[i]
    DECRYPTEDDICT3[RANDCHARACTERS3[i]] = ALLCHARACTERS[i]

# Encrypt and decrypt functions

def encrypt(text):
    lstenc = []
    if len(text) % 5 == 0:
        for i in range(len(text)):
            lstenc.append(DICTENCRYPTED[text[i]])
    else:
        if len(text) % 3 == 0:
            for i in range(len(text)):
                lstenc.append(DICTENCRYPTED1[text[i]])
        else:
            if len(text) % 2 == 0:
                for i in range(len(text)):
                    lstenc.append(DICTENCRYPTED2[text[i]])
            else:
                for i in range(len(text)):
                    lstenc.append(DICTENCRYPTED3[text[i]])
    enctext = ''.join(lstenc)
    return print('Your encrypted text:', enctext)

def decrypt(text):
    lstdec = []
    if len(text) % 5 == 0:
        for i in range(len(text)):
            lstdec.append(DECRYPTEDDICT[text[i]])
    else:
        if len(text) % 3 == 0:
            for i in range(len(text)):
                lstdec.append(DECRYPTEDDICT1[text[i]])
        else:
            if len(text) % 2 == 0:
                for i in range(len(text)):
                    lstdec.append(DECRYPTEDDICT2[text[i]])
            else:
                for i in range(len(text)):
                    lstdec.append(DECRYPTEDDICT3[text[i]])
    dectext = ''.join(lstdec)
    return print('Your decrypted text:', dectext)