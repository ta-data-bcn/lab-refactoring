#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string


# In[ ]:


password_length = int(input("Input the number of characters for your password: "))
letter_boolean = input("Do you want letters in your password? True or False? (Caps sensitive) " )
number_boolean = input("Do you want numbers in your password? True or False? (Caps sensitive) " )
special_boolean = input("Do you want special characters in your password? True or False? (Caps sensitive) " )
unique_password = input("Do you only want unique characters in your password? True or False? (Caps sensitive) " )
  
print(letter_boolean)
def random_password():
    stored_password = []
    all_characters = string.ascii_letters + string.digits + string.punctuation
    letter_and_number = string.ascii_letters + string.digits
    letter_and_special = string.ascii_letters + string.punctuation
    number_and_special = string.digits + string.punctuation
    
    for i in range(password_length):
        #check each possible combination of boolean if they are true or false
        if letter_boolean =="True" and number_boolean =="True" and special_boolean =="True" and unique_password =="True":
            stored_password.append(random.sample(all_characters))
        elif letter_boolean =="True" and number_boolean =="True" and special_boolean =="True" and unique_password =="False":
            stored_password.append(random.choice(all_characters))
            
        elif letter_boolean =="True" and number_boolean =="True" and special_boolean =="False" and unique_password =="True":
            stored_password.append(random.sample(letter_and_number))
        elif letter_boolean =="True" and number_boolean =="True" and special_boolean =="False" and unique_password =="False":
            stored_password.append(random.choice(letter_and_number))
            
        elif letter_boolean =="True" and special_boolean =="True" and number_boolean =="False" and unique_password =="True":
            stored_password.append(random.sample(letter_and_special))
        elif letter_boolean =="True" and special_boolean =="True" and number_boolean =="False" and unique_password =="False":
            stored_password.append(random.choice(letter_and_special)) 
            
        elif number_boolean =="True" and special_boolean =="True" and letter_boolean =="False" and unique_password =="True":
            stored_password.append(random.sample(number_and_special))
        elif number_boolean =="True" and special_boolean =="True" and letter_boolean =="False" and unique_password =="False":
            stored_password.append(random.choice(number_and_special))    
        
    return stored_password

random_password()

final_password = "".join(random_password())


# In[ ]:


print("Your strong and randomly generated password is:", final_password)


# In[ ]:




