# FALL 2021
# SI 206
# HW5 - Regular Expressions
# Name: Cooper Drobnich
# Who did you work with: Adam Brenner and Umang Bhojani

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
    info_dic = {}
    info = []
    regex = r'Chapter (?:\d+): (?:.*)'
    for string in string_list:
        match = re.findall(regex, string)
        for i in match:
            info.append(i)
            info_dic[int(i[8])] = i[11:]
    return info_dic

    
   


def find_capitalized_words(string_list):
    """This function finds consecutive capitalized words (at least two words, no punctuations in between). 
    For example, in the text we can find Diagon Alley, Professor Remus Lupin as qualified consecutive words.
    Example output: ["Diagon Alley", "Professor Remus Lupin"]  
    """
    capital = []
    regex = r'(?:[A-Z]\w+(?:\s[A-Z][\w-]*)+)'
    for i in string_list:
        match = re.findall(regex, i)
        for x in match:
            capital.append(x)
    return capital



def find_urls(string_list):
    """ Return a list of valid urls in the list of strings """

    urls = []
    regex = r'https?:\/\/www.\w+\.(?:com|org).*'
    for i in string_list:
        match = re.findall(regex, i)
        for a in match:
            urls.append(a)
    return urls




def find_dates(string_list):
    """ Return a list of dates in the list of strings 
        Sample format: 
        mm/dd/yyyy 
        mm/dd/yy 
        mm-dd-yyyy 
        mm-dd-yy
        Please refer to the instructions and be careful about invalid dates!
    """
    dates = []
    regex = r'((1[0-2]|0[1-9])[\/\-](3[0]|[0-2][0-9])[\/\-]((1[9][0-9][0-9]|2[0]([01][0-9]|2[0,1])|[0-9][0-9]\b)))'
    for i in string_list:
        match = re.findall(regex, i)
        for a in match:
            dates.append(a[0])
    return dates


## Extra credit
def count_mid_str(string_list, string):
    

    """ return a count of the number of times a specified strings appears in the text.
        The matched string should be in the middle of a word. 
        It should not be the start or the end of a word.

        string_list -- the list of strings to count the string in
        string -- the stirng to look for, e.g., "be"
        return -- a count of the number of times the string appears in the text
    """
    string_mid = []
    reg = rf'\w{string}\w'
    count = 0
    for line in string_list:
        match = re.findall(reg, line)
        for i in match:
            string_mid.append(i)
    count = len(string_mid)
    return count

# Implement your own tests.
class TestAllMethods(unittest.TestCase):


    def test_find_chapter_info(self):
        string_list = read_file('Harry-potter-txt.txt')
        info_dic = find_chapter_info(string_list)
        self.assertEqual(len(info_dic), 6)
        self.assertEqual(info_dic[1], "Owl Post")
        self.assertEqual(info_dic[2], "Aunt Marge's Big Mistake")

    def test_find_capitalized_words(self):
        string_list = read_file('Harry-potter-txt.txt')
        capital = find_capitalized_words(string_list)
        self.assertEqual(len(capital), 64)
        self.assertEqual(capital[3], 'Aunt Petunia')
        self.assertEqual(find_capitalized_words(['Hello how are You Doing']), ['You Doing'])
        self.assertEqual(find_capitalized_words(['hello']), [])
        self.assertEqual(find_capitalized_words(['Hello my name is Coop Drob']), ['Coop Drob'])
       


    def test_find_urls(self):
        string_list = read_file('Harry-potter-txt.txt')
        urls = find_urls(string_list)
        self.assertEqual(len(urls), 5)
        self.assertEqual(urls[0], 'https://www.apa.org/')
        self.assertEqual(find_urls(['https://www.youtube.crm/video']), [])





    def test_find_dates(self):
        string_list = read_file('Harry-potter-txt.txt')
        dates = find_dates(string_list)
        self.assertEqual(len(dates), 5)
        self.assertEqual(find_dates(['07/21/2058, 12-02-20']),['12-02-20'])
        self.assertEqual(find_dates(['07.21.2058, 07/21/1823']),([]))
        


    def test_count_mid_str(self):
        string_list = read_file('Harry-potter-txt.txt')
        self.assertEqual(count_mid_str(string_list, 'bees'), 0)
        self.assertEqual(count_mid_str(string_list, 'arr'), 47)
        self.assertEqual(count_mid_str(string_list, 'th'), 18)
        



def main():
	# Use main to test your function.
    # Run unit tests, but feel free to run any additional functions you need
    unittest.main(verbosity = 2)

if __name__ == "__main__":
    main()
