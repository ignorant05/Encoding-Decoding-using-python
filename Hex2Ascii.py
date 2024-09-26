#Created by ignorant05 aka Oussama Baccara

#!/usr/bin/env python3 

##############################################################################################################################

#Importing sys module to handle terminal, user input and errors 

##############################################################################################################################

import sys 

if len(sys.argv) < 2 : 
    print ("Usage : python3 ./Hex2Ascii.py <Hex_To_Decode") 
    sys.exit(1)

Hex_string = sys.argv[1]

##############################################################################################################################

#Slicing the Hex String to strings with 2-character length 
#Assigning them to a list + handling user input errors if exists 

##############################################################################################################################

list_of_bytes = [Hex_string[i:i+2] for i in range(0, len(Hex_string), 2)]

for hex_pair in list_of_bytes:
    if len(hex_pair) != 2 or any(c not in "0123456789ABCDEFabcdef" for c in hex_pair):
        print(f"Invalid hex pair: {hex_pair}")
        sys.exit(1)

##############################################################################################################################

#The conversion function 

##############################################################################################################################

def Hex2Decimal (num_string) : 

    Hex_list =  {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,"5": 5, "6": 6,"7": 7, "8": 8,
            "9": 9,"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
                }

    num = 0 
    
    for i in range(2): 
        char = num_string[1 - i]
        if char.upper() in Hex_list :
            num+=Hex_list[char.upper()]*(16**i)
        else:
            print(f"Invalid hex character: {char}")
            sys.exit(1)
        
    return num

##############################################################################################################################

#converting all the list_of_bytes to list_of_ascii_numbers and then to a list of list_of_ascii_characters 
#Making a String if ascii characters 
#Print the result 

##############################################################################################################################

list_of_ascii_nums = list(map(Hex2Decimal,list_of_bytes))

list_of_ascii_chars = [chr(x) for x in list_of_ascii_nums]

result = ''.join(list_of_ascii_chars)

print(result)

##############################################################################################################################