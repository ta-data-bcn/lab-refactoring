{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing random, string and collections libraries\n",
    "import random\n",
    "import string\n",
    "from collections import deque"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# getting the cleaned ascii\n",
    "alph = string.printable\n",
    "alphabet_split = alph.split(\" \")\n",
    "alphabet = alphabet_split[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function that allows to create your own key with any characters that a language might use \n",
    "# if you provide a list of characters to be used\n",
    "\n",
    "def shuffle_alphabet(base = alphabet):\n",
    "    key_to_shuffle = list(base)\n",
    "    random.shuffle(key_to_shuffle)\n",
    "    key = ''.join(key_to_shuffle)\n",
    "    return key\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Finding maximum key size for Caesar cypher\n",
    "max_key_size = len(alphabet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to get ask for key to use in Caesar cypher\n",
    "\n",
    "def getKey():\n",
    "    key = 0\n",
    "    while True:\n",
    "        print(f'What number do you want to use for the cypher between -{max_key_size} and {max_key_size}) ')\n",
    "        key_c = int(input())\n",
    "        if key_c >= (-1 * max_key_size) and key_c <= max_key_size:\n",
    "            return key_c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to create Caesarian cypher translation table using the key\n",
    "def shuffle_caesarian(base=alphabet):\n",
    "    d = deque(alphabet)\n",
    "    d.rotate(getKey())\n",
    "    key_caesar = ''.join(list(d))\n",
    "    return key_caesar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function takes 3 variables to encrypt or decrypt the message\n",
    "\n",
    "def encrypt_decrypt(m, a, k):\n",
    "    translation_table = m.maketrans(a, k)\n",
    "    encrypt_decrypt_message = m.translate(translation_table)\n",
    "    print(encrypt_decrypt_message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type 1 for encrypting a message. \n",
      "Type 2 for decripting a message. \n",
      "Type 3 to exit the program 1\n",
      "Type 1 for Caesarean cypher. \n",
      "Type 2 for Translation table 1\n",
      "What is your message Hello pequenin\n",
      "What number do you want to use for the cypher between -94 and 94) \n",
      "30\n",
      "d;\\\\_ `;{0;^?^\n",
      "Type 1 for encrypting a message. \n",
      "Type 2 for decripting a message. \n",
      "Type 3 to exit the program 2\n",
      "Type 1 for Caesarean cypher. \n",
      "Type 2 for Translation table 1\n",
      "What is your message d;\\\\_ `;{0;^?^\n",
      "What number do you want to use for the cypher between -94 and 94) \n",
      "30\n",
      "Hello pequenin\n",
      "Type 1 for encrypting a message. \n",
      "Type 2 for decripting a message. \n",
      "Type 3 to exit the program 4\n",
      "Options are only 1, 2 or 3\n",
      "Type 1 for encrypting a message. \n",
      "Type 2 for decripting a message. \n",
      "Type 3 to exit the program hekjsgd\n",
      "Options are only 1, 2 or 3\n"
     ]
    }
   ],
   "source": [
    "choose_action=0\n",
    "key = shuffle_alphabet()\n",
    "while choose_action != 3:\n",
    "    choose_action = input(\"Type 1 for encrypting a message. \\nType 2 for decripting a message. \\nType 3 to exit the program \")\n",
    "    if choose_action == \"1\":\n",
    "        choose_encryption = input(\"Type 1 for Caesarean cypher. \\nType 2 for Translation table \")\n",
    "        message = input(\"What is your message \")\n",
    "        if choose_encryption == \"1\":\n",
    "            #caesarian(message, alphabet, alphabet_caesar)\n",
    "            key_caesar = shuffle_caesarian()\n",
    "            encrypt_decrypt(message, alphabet, key_caesar)\n",
    "        elif choose_encryption == \"2\":\n",
    "            encrypt_decrypt(message, alphabet, key)\n",
    "        else:\n",
    "            print(\"Only two methods available: 1 or 2\")\n",
    "    elif choose_action == \"2\":\n",
    "        choose_encryption = input(\"Type 1 for Caesarean cypher. \\nType 2 for Translation table \")\n",
    "        message = input(\"What is your message \")\n",
    "        if choose_encryption == \"1\":\n",
    "            key_caesar = shuffle_caesarian()\n",
    "            encrypt_decrypt(message, key_caesar, alphabet)\n",
    "            #caesarian(message, alphabet, alphabet_caesar)\n",
    "        elif choose_encryption == \"2\":\n",
    "            encrypt_decrypt(message, key, alphabet)\n",
    "        else:\n",
    "            print(\"Only two methods available: 1 or 2\")\n",
    "    elif choose_action == \"3\":\n",
    "        break\n",
    "    else:\n",
    "        print(\"Options are only 1, 2 or 3\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
