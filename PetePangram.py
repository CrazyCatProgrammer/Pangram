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
# let user enter the sentence of their choosing. lowercasing everything so it can be consistently checked against the alphabet variable.
sentence = input("Enter your sentence here... (Steve not Pete): ")


# Function that loops to check that each letter listen in the 'alphabet' variable is listed at least once. 
# if all letters are accounted for it returns True. If not it returns False
def ispangram(str): 
    for char in alphabet: 
        #letters are lowercased so they can be checked. however this won't change the sentence if any of the letters are capitlized. 
        if char not in str.lower(): 
            return False
  
    return True

# Function sorts the alphabet and the sentence then prints whatever letters are missing. 
def missing_letters(str):
    return ''.join(sorted(set(alphabet) - set(str.lower())))
      

# this if statement passes the sentence through the 'ispangram' test. Then prints True 
if(ispangram(sentence)): 
    print("True", "'", sentence, "'", "is a pangram.")
# if stat
else: 
    print("False", "'", sentence, "'", "is NOT a pangram.", "\n",
            "You're missing: ", missing_letters(sentence))
