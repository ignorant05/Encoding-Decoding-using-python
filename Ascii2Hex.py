#Created by ignorant05 aka Oussama Baccara

#! /usr/bin/env python3 

#Importing sys module to handle terminal, user input and errors 

#####################################################################################################################

import sys 

if len(sys.argv) < 2 : 
    print("Usage : python3 Ascii2Hex.py <Text-to-encode>")
    sys.exit(1)

txt = sys.argv[1]

#####################################################################################################################

#The conversion function 

#####################################################################################################################
def encode (txt):

    hex_string = ''.join(hex(ord(i))[2:].upper().zfill(2) for i in txt)
    return hex_string

print(encode(txt))

#####################################################################################################################








