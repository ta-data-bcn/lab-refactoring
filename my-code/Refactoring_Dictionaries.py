# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:58:04 2020

@author: Alt-E-K
"""
# we are first going to import the modules we need
import string 
#we define the variable that contains all the possible charachters for our encoder.
char_list=list(string.printable)

#we do the first level of encoding by equating each charachter to the one 7 positions to the 
# left in the list, good thing about this is that it is a self-contained function and can admit
# other lists of charachters
def first_encoding(x):
    encoding_dict1 = {}
    for index, item in enumerate(x):
        encoding_dict1[item]=char_list[index-7]
    return encoding_dict1

encode_phase1=first_encoding(char_list)

#we reduce the second level of encoding from a whole function to a disctionary comprehension. 
encode_phase2 = {pair[0]:ord(encode_phase1.get(pair[0]))for pair in encode_phase1}

#to my understanding this function was too dificult for dictionary comprehension.too many ifs
def same_lenght_version(x):
    encoding_dict3 = {}
    for pair in x:
        char=str(x.get(pair[0]))
        if len(char) == 2:
            new_char=char+'@'
        elif len(char) == 1:
            new_char=char+'*/'
        else:
            new_char=char
        encoding_dict3[pair[0]]=new_char
    return encoding_dict3

encode_phase3=same_lenght_version(encode_phase2)

#the decoded dictionary can also be made with dictionary comprehension.
decoded_dict={encode_phase3.get(pair[0]):pair[0] for pair in encode_phase3}

