# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:54:19 2020

@author: Usuario
"""
#We import the functions we are going to use.
from Encoding_Decoding_Functions import ultimate_encoder
from Encoding_Decoding_Functions import improved_decoder

#we write the now way simpler script
answer1=input('Do you wish to encode or decode?')
while answer1 != None:

    if answer1 == 'encode':
        ultimate_encoder()
        
        break
        
    elif answer1 == 'decode':
        improved_decoder()
        break
                #don't know if the continue is in the right place because the loop that 
    else:
        answer1=input('Please select a valid option:')
        continue

