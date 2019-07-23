#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random
import string


# In[14]:


def random_password():
    password_length = int(input("Input the number of characters for your password: "))
    letter_boolean = input("Do you want letters in your password? True or False? (Caps sensitive) " )
    number_boolean = input("Do you want numbers in your password? True or False? (Caps sensitive) " )
    special_boolean = input("Do you want special characters in your password? True or False? (Caps sensitive) " )
    unique_password = input("Do you only want unique characters in your password? True or False? (Caps sensitive) " )

    stored_password = []
    all_characters = string.ascii_letters + string.digits + string.punctuation
    letter_and_number = string.ascii_letters + string.digits
    letter_and_special = string.ascii_letters + string.punctuation
    number_and_special = string.digits + string.punctuation
    
    for i in range(password_length):
        #check if each possible combination of booleans are true or false
        if letter_boolean == "True" and special_boolean == "True" and number_boolean == "True":
            if unique_password == "True":
                stored_password.append(random.sample(all_characters))            
            else:
                stored_password.append(random.choice(all_characters))
            
        elif letter_boolean == "True" and special_boolean == "False" and number_boolean == "True":
            if unique_password == "True":
                stored_password.append(random.sample(letter_and_number))
            else:
                stored_password.append(random.choice(all_characters))
                
        elif letter_boolean == "True" and special_boolean == "True" and number_boolean == "False":
            if unique_password == "True":
                stored_password.append(random.sample(letter_and_special))
            else:
                stored_password.append(random.choice(letter_and_special)) 
            
        elif letter_boolean =="False" and special_boolean =="True" and number_boolean =="True":
            if unique_password == "True":
                stored_password.append(random.sample(number_and_special))
            else:
                stored_password.append(random.choice(number_and_special)) 

    final_password = "".join(random_password())
    return final_password
#number_boolean == "True" and special_boolean == "True" and letter_boolean == "False" and unique_password == "True":


# In[15]:


print(random_password())


# In[ ]:




