#!/usr/bin/env python
# coding: utf-8

# In[1]:


# We import Cryptex, a library containing the formulas and dictionaries needed to encrypt and decrypt

import Cryptex


# In[3]:


# We generate the flow of the program, where we define if we are doing an encryption 
    # or a decryption and then run the optimal formula
decision=input("Do you want to encrypt or decrypt a message? (please type encrypt/decrypt)")
while (decision!="encrypt") and (decision!="decrypt"):
    decision=input("Oops! I didn't understand! Do you want to encrypt or decrypt?"
                   "(please type encrypt or decrypt)")
if decision == "encrypt":
    print(Cryptex.encryption())
else:
    print(Cryptex.decryption())

