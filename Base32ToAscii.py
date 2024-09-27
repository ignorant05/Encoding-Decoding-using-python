#! /usr/bin/env python3 

#################################################################################################################################

#Importing sys module to handle terminal, user input and errors 

#################################################################################################################################

import sys 

if len(sys.argv)< 2 :
    print("Usage : python3 Base32ToAscii <Base32-String>")
    sys.exit(1)

txt = sys.argv[1]

#################################################################################################################################

#removing the "=" sign 
#using the index to map each base32 character an then getting it's index 
#converting each character to binary and then padd it with zeos to the right if it's length is less than 5 

#################################################################################################################################

core_txt = txt.rstrip("=")

Base32 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

list_of_bi = [Base32.index(x) for x in core_txt]

string_of_binary = "".join(map(lambda x : bin(x)[2:].zfill(5),list_of_bi))

#################################################################################################################################

#grouping each byte string + handling the case of the last syte string 

#################################################################################################################################
l = len(string_of_binary)

list_of_bytes = [string_of_binary[i:i+8] for i in range(0,l,8)]

list_of_bytes[-1]=list_of_bytes[-1].ljust(8,"0")

#################################################################################################################################

#converting each byte to decimal and each decimal to ascii  

#################################################################################################################################

list_of_decimals = [int(x,2)for x in list_of_bytes]

output_string = ''.join(chr(x)for x in list_of_decimals)

print(output_string)

#################################################################################################################################