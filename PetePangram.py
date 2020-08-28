# 
# Step 1. Set up a basic working pangram. - DONE
# Step 2. Print whatever letters are missing. - DONE 
# Step 3. Send to the GITHUB - DONE
# -----------------------------------------------------
# REFERENCES
# I'd like to say I'm the super programmer who can pull code out of the air. But I'm a googler >.< 
# https://www.geeksforgeeks.org/python-program-to-check-if-given-string-is-pangram/
# https://www.thetopsites.net/article/55265024.shtml
# 
# -----------------------------------------------------

import string 

# Variables

# set alphabet  
alphabet = "abcdefghijklmnopqrstuvwxyz"
# let user enter the sentence of their choosing. 
sentence = input("Enter your sentence here... (Steve not Pete): ")


# Function that loops to check that each letter listen in the 'alphabet' variable is listed at least once. 
# If all letters are accounted for it returns True. If not it returns False
def ispangram(str): 
    for char in alphabet: 
        #Letters are lowercased so they can be checked. This won't change the sentence if any of the letters are capitlized. 
        if char not in str.lower(): 
            return False
    return True

# Function sorts the alphabet and the sentence then prints whatever letters are missing. 
def missing_letters(str):
    return ''.join(sorted(set(alphabet) - set(str.lower())))
      

# this if sentence passes the sentence through the 'ispangram' test. Then prints True 
if(ispangram(sentence) == True): 
    print("True", "'", sentence, "'", "is a pangram.")
# if sentence fails pangram test then send it through 'missing_letters' to see what letters are missing and print them.
else: 
    print("False", "'", sentence, "'", "is NOT a pangram.", "\n",
            "You're missing: ", missing_letters(sentence))
