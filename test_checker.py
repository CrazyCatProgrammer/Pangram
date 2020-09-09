# Not gonna lie...this stuff is so COOL.
# Delish automation
# 
#
# Resources!!!! (yay google/youtube)
# https://www.youtube.com/watch?v=6tNS--WetLI&t=1273s
# https://docs.python.org/3/library/unittest.html
#
# 

import unittest
import pangram_classes

# command to run tests: 
# python -m unittest test_checker.py

class TestPangramChecker(unittest.TestCase):
    """Unit testing with pre set variables to check that PangramChecker is running smoothly"""
    good_sentence = "The five boxing wizards jump quickly"
    bad_sentence = "bleh"

    def test_true(self):
        check = pangram_classes.PangramChecker(self.good_sentence)
        result = check.is_pangram()
        self.assertTrue(result)

    def test_false(self):
        check = pangram_classes.PangramChecker(self.bad_sentence)
        result = check.is_pangram()
        self.assertFalse(result)