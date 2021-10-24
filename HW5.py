# FALL 2021
# SI 206
# HW5 - Regular Expressions
# Name:
# Who did you work with:　

import re
import os
import unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines


def find_chapter_info(string_list):
    """ This function finds and returns 
    a dictionary with the chapter number as the keys and the title of the chapter as the value
    Example output: {1: “Owl Post”, 2: “Aunt Marge's Big Mistak”, … }
    """
    pass

def find_capitalized_words(string_list):
    """This function finds consecutive capitalized words (at least two words, no punctuations in between). 
    For example, in the text we can find Diagon Alley, Professor Remus Lupin as qualified consecutive words.
    Example output: ["Diagon Alley", "Professor Remus Lupin"]  
    """
    pass



def find_urls(string_list):
    """ Return a list of valid urls in the list of strings """

    pass


def find_dates(string_list):
    """ Return a list of dates in the list of strings 
        Sample format: 
        mm/dd/yyyy 
        mm/dd/yy 
        mm-dd-yyyy 
        mm-dd-yy
        Please refer to the instructions and be careful about invalid dates!
    """

    pass


## Extra credit
def count_mid_str(string_list, string):
    """ return a count of the number of times a specified strings appears in the text.
        The matched string should be in the middle of a word. 
        It should not be the start or the end of a word.

        string_list -- the list of strings to count the string in
        string -- the stirng to look for, e.g., "be"
        return -- a count of the number of times the string appears in the text
    """
    pass


# Implement your own tests.
class TestAllMethods(unittest.TestCase):


    def test_find_chapter_info(self):
        pass

    def test_find_capitalized_words(self):
        pass

    def test_find_urls(self):
        pass

    def test_find_dates(self):
        pass


    def test_count_mid_str(self):
        pass



def main():
	# Use main to test your function.
    # Run unit tests, but feel free to run any additional functions you need
    unittest.main(verbosity = 2)

if __name__ == "__main__":
    main()
