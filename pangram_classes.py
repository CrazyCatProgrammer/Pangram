class PangramChecker:
    # defined variables within class
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self,sentence):
        self.pangram = sentence

    # Function that loops to check that each letter listen in the 'alphabet' variable is listed at least once. 
    # If all letters are accounted for it returns True. If not it returns False
    def ispangram(self): 
        for char in self.alphabet: 
            #Letters are lowercased so they can be checked. This won't change the sentence if any of the letters are capitlized. 
            if char not in self.pangram.lower(): 
                return False
        return True

    # Function sorts the alphabet and the sentence then prints whatever letters are missing. 
    def missing_letters(self):
        return ''.join(sorted(set(self.alphabet) - set(self.pangram.lower())))

