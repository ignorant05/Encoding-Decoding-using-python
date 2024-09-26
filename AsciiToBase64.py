#Created by ignorant05 aka Oussama Baccara

#! /usr/bin/env python3 

##############################################################################################################################

import sys 

if len(sys.argv) < 2 : 

    print("Usage : python3 AsciiToBase64.py <Text-TO-Encode")
    sys.exit(1)

txt = sys.argv[1]

##############################################################################################################################

#Removing the '0b' from the every binary number + padding every single one with zeros to the right 
#Convert every single character of the user-input to it's ascii number
#Convert every elment of the user-input 'txt' into a string of binaries
#Slicing the string into strings of 6 characters and padding the last element if necessary by zeros to the left

##############################################################################################################################

def convert2Binary(num): 

    return bin(num)[2:].zfill(8)

binary_string= ''.join(map(convert2Binary, map(ord, txt)))

l=len(binary_string)

list_of_bi = [binary_string[i:i+6] for i in range(0, l, 6)]

if len(list_of_bi[-1])!=6:

    list_of_bi[-1]=list_of_bi[-1].ljust(6,'0')

##############################################################################################################################

#Convert every element of the list 'list_of_bi' to a 'list_of_decimals'

##############################################################################################################################

def BinaryTo10(binary_str):

    return int(binary_str, 2)

list_of_decimals = list(map(BinaryTo10,list_of_bi))

##############################################################################################################################

#The encoding function
#The print statement

##############################################################################################################################

def encode(list):

    string = ""

    carac_list = [
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", 
                "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9", "+", "/"
                ]

    return ''.join(carac_list[element] for element in list_of_decimals)
    
print(encode(list_of_decimals))

##############################################################################################################################