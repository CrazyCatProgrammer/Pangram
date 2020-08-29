# 
# Step 1. Set up a basic working pangram. - DONE
# Step 2. Print whatever letters are missing. - DONE 
# Step 3. Send to the GITHUB - DONE
# -----------------------------------------------------
# REFERENCES
# I'd like to say I'm the super programmer who can pull code out of the air. But I'm a googler >.< 
# https://www.geeksforgeeks.org/python-program-to-check-if-given-string-is-pangram/
# https://www.thetopsites.net/article/55265024.shtml
# https://docs.python.org/2/tutorial/classes.html
# https://pep8.org/#module-level-dunder-names
# -----------------------------------------------------

import string 
from pangram_classes import PangramChecker

# Variable
# let user enter the sentence of their choosing. 

sentence = input("Enter your sentence here... (Steve not Pete): ")

# create object 
check = PangramChecker(sentence)

# this if sentence passes the sentence through the 'ispangram' test. Then prints True 
if(check.ispangram()): 
    print("True", "'", sentence, "'", "is a pangram.")
# if sentence fails pangram test then send it through 'missing_letters' to see what letters are missing and print them.
else: 
    print("False", "'", sentence, "'", "is NOT a pangram.", "\n",
            "You're missing: ", check.missing_letters())
