#Created by ignorant05 aka Oussama Baccara

#! /usr/bin/env python3

#####################################################################################################################

#Importing sys module to handle terminal, user input and errors 

#####################################################################################################################

import sys 

if len(sys.argv)< 2 :
    print("Usage : python3 Ascii2Base32.py <Text-To-Encode> ")
    sys.exit(1)

txt = sys.argv[1]

#####################################################################################################################

#getting the num of the every ascii character + converting it to binary + padding it with zeros to the right

#####################################################################################################################
  
binary_string = ''.join(map(lambda x: bin(ord(x))[2:].zfill(8), txt))

#####################################################################################################################

#slicing the binary string into five bit length strings 
#handling the last element if it doesn't verify the length condition 

#####################################################################################################################

l = len(binary_string)

list_of_5bits =[binary_string[i:i+5] for i in range(0, l, 5)]

list_of_5bits[-1]=list_of_5bits[-1].ljust(5, '0')

#####################################################################################################################

#convertion every five bit string to it's Decimal value 
#using the indexes of each character of the base32 string, i made a string of base32's charcters

#####################################################################################################################

list_of_nums = [int(x,2) for x in list_of_5bits]

base32 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

output_string = ''.join(base32[num] for num in list_of_nums)

#####################################################################################################################

#padding the string with '=' if it's length isn't devidable by zero 
#print the output 

#####################################################################################################################

while len (output_string)%8!=0 :
    
    output_string=output_string+"="


print(output_string)

#####################################################################################################################