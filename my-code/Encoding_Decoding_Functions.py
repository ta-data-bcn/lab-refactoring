# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:18:52 2020

@author: Alt-E-K
"""
#we import the ditionaries.
from Refactoring_Dictionaries import encode_phase3 as encoding_dictionary
from Refactoring_Dictionaries import decoded_dict as decoding_dictionary

#we define the encoder function. since it can encode virtually any sign there is no need 
#to control for the user input. It simply goes charachter by charachter translating with the 
#dictionary, puts it in a list and returns the joined strings.
def ultimate_encoder():
    new_list=[]
    message=input('Please introduce the message for encoding: ')
    for i in message:
        #here we can change the encryption level by changing the dictionary from wich we encode, so the code is flexible
        new_char=encoding_dictionary.get(i)
        new_s=str(new_char)
        new_list.append(new_s)
        joined_str = ("".join(new_list))
    print(joined_str)

#before the decoding function we need to define an
#we create the 2 empty lists and the one with all the dictionary keys for checking if 
#translation is possible.
    
def improved_decoder():
    broke_down=[]
    translated = []
    our_dict_list= list(decoding_dictionary.keys())
    #making sure that all the inputs are strings        
    message=str(input('Please introduce the message for decoding:'))

    
    #breaking the string down into parts to check if we can translate it, then translate it
    for i in range(0, len(message), 3):
        char=message[i:i+3]
        broke_down.append(char)
   
    #making sure that the input is in OUR encoding method. the wile loop is made to ensure infinite oportunities for inputting
    #the correct code are available
    while message != None:
        if set(broke_down).issubset(set(our_dict_list)):
            #if it is it will proceed to translate, print and break the loop
            for i in broke_down:
                tr_char=decoding_dictionary.get(i)
                translated.append(tr_char)
                joined_str = ("".join(translated))
            print(joined_str)
            break
        else:
            message = str(input('We are not able to decode a different encoding algorithm, please introduce a valid code:'))
            broke_down = []
            for i in range(0, len(message), 3):
                char=message[i:i+3]
                broke_down.append(char)
            
            
            continue
                #this else made sure that when the code wasnt ours you could re input a message to decode and restarted the process
                #of breaking it into pieces to check if it was ours once it has made that whole process the continue remits us back
                #to the begining of the while loop and the translation process.
                #However in the final function we had to change the order of the conditions, because the break from the enclosing
                #while loop of the other function needs to break when the translation finishes and it conflicted with this else.
