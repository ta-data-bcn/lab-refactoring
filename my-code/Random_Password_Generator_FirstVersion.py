#!/usr/bin/env python
# coding: utf-8

# In[2]:


from password_strength import PasswordStats #import library to test the strength of the passwords
import string #to create a string of punctuations
import random #to be able to shuffle everything
Name=input("Welcome! Let's create a random password for you! Please insert your name: ")
Birth=input(f"Ok, {Name}! I will use the letters of your name in your password! Please insert also your birth year: ")
Info=Name+Birth
passwordlength=16
Punct_number=16-len(Info) #the number of punctuation symbols I need 
punctelements="".join(random.choice(string.punctuation) for i in range (Punct_number)) #create the correct number of string of punct symbols
Passwordelements=Info+punctelements #put everything together
Password="".join(random.sample(Passwordelements, 16)) #shuffling and creating a string with 16 characters
print(f"Here is your random password: {Password}, it's a mix of the letters of your name, the numbers in your birth year and some random punctuations!")
stats = PasswordStats(Password)
y=stats.strength() #strength of the generated password
print(f"The strength of your password is: {y}. It's recommended for it to be at least 0.66 to be considered strong.")


# In[ ]:




