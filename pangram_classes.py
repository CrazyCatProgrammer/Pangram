class PangramChecker:
    # defined variables within class
    """This class uses the variable 'alphabet' to check against the input sentence with the is_pangram method. If it's false the missing_letters method can print what letters are missing."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self,sentence):
        self.sentence = sentence


    # included Dunder methods to represent the PangramChecker class. (https://dbader.org/blog/python-dunder-methods)
    def __repr__(self):
        return 'PangramChecker({!r}, {!r})'.format(self.sentence, self.alphabet)

    def __str__(self):
        return 'PangramChecker sentence {}: with alphabet {}'.format(self.sentence, self.alphabet)

    # getter method
    def get_sentence(self): 
        return self.sentence 
      
    # setter method
    def set_sentence(self, sentence): 
        self.sentence = sentence
    
    #Function that loops to check that each letter listen in the 'alphabet' variable is listed at least once. If all letters are accounted for it returns True. If not it returns False
    def is_pangram(self): 
        for char in self.alphabet: 
            #Letters are lowercased so they can be checked. This won't change the sentence if any of the letters are capitlized. 
            if char not in self.sentence.lower(): 
                return False
        return True
        
    #Subtracts sentence letters from the alphabet. Whatever remains are printed as the missing letters.
    # Function sorts the alphabet and the sentence then prints whatever letters are missing. 
    def missing_letters(self):
        return ''.join(sorted(set(self.alphabet) - set(self.sentence.lower())))

