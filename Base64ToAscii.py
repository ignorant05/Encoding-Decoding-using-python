#Created by ignorant05 aka Oussama Baccara

#!/usr/bin/env python3

##############################################################################################################################

#Importing sys module to handle terminal, user input and errors 

##############################################################################################################################

import sys

if len(sys.argv) < 2:
    print("Usage: ./base64dDec.py <base64_string>")
    sys.exit(1)

seq = sys.argv[1]

seq = seq.rstrip("=")

##############################################################################################################################

#Get the ascii num of every character of the base64 string
#assign the result in list_one

carac_list = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", 
    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
    "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
    "8", "9", "+", "/"
    ]

def ascii_num(carac):
    if carac in carac_list:
        return carac_list.index(carac)


list_one= list(map(lambda c: ascii_num(c), seq))

##############################################################################################################################

#Getting the binary form of every ascii num 
#Assigning the result in a list called list_of_binaries 
#Contatinating the elements of the list into a string called String_of_binaries

##############################################################################################################################

list_of_binaries = list(map(lambda x: bin(x)[2:].zfill(6), list_one))

string_of_binaries = ''.join(list_of_binaries)

##############################################################################################################################

#Getting a list of 8bit binaries 

##############################################################################################################################

def slice_string(input_string):
    list_of_8bits= []
    for i in range(0, len(input_string), 8):
        list_of_8bits.append(input_string[i:i+8])
    return list_of_8bits

list_four = slice_string(string_of_binaries)
def adjust2(element):
    return element.ljust(8, "0")
    
list_four[-1] = adjust2(list_four[-1])

##############################################################################################################################

#Getting a binary_list_of_ascii  and then concatinating it's content into the final_res string 
#Print the result 

##############################################################################################################################
def binary_list_to_ascii(binary_list):
    # Convert each binary value to its corresponding ASCII character
    ascii_characters = [chr(int(bv, 2)) for bv in binary_list]
    
    # Join the characters to form the final ASCII string
    return ''.join(ascii_characters)

final_res = binary_list_to_ascii(list_four)

print(final_res)

##############################################################################################################################
