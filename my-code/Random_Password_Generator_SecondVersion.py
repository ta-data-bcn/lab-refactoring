#!/usr/bin/env python
# coding: utf-8

# In[2]:
# to test the strength of the passwords:
from password_strength import PasswordStats
# to create a string of punctuations:
import string
# to shuffle characters:
import random

# get the desired input from the user
name = input("Welcome! Let's create a random password for you!\
     Please insert your name: ")
birth = input(f"Ok, {Name}! I will use the letters of your name in\
     your password! Please insert also your birth year: ")
info = name + birth

# determine password length and the number of punctuation symbols I need:
passwordlength = 16
punct_number = 16 - len(info)

# create the correct number of string of punct symbols:
punctelements = "".join(random.choice(string.punctuation) for i in range(punct_number))

# merge the user input and punctuation symbols:
passwordelements = info+punctelements

# shuffle the string created above:
password = "".join(random.sample(passwordelements, 16))

print(f"Here is your random password: {password}, it's a mix of the\
    letters of your name, the numbers in your birth year\
         and some random punctuations!")
stats = PasswordStats(password)
# strength of the generated password:
y = stats.strength()
print(f"The strength of your password is: {y}. It's recommended for it to be\
     at least 0.66 to be considered strong.")

# In[ ]:
