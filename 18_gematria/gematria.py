#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-12-11
Purpose: Encode words as numbers
"""

import argparse
# from functools import reduce
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Encode words as numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        print(' '.join(map(word2num, line.split())))
        
        # print(' '.join(map(word2num, line.split())))


# --------------------------------------------------
def word2num(word):
    """Convert word to number using ASCII values"""

    # Anything that is NOT in the character class is substituted with an empty string.
    # cleaned_word = re.sub('[^A-Za-z0-9]', '', word)

    # vals = [ord(char) for char in cleaned_word]

    # return str(sum(map(ord, cleaned_word)))

    # Combined in map function:
    return str(sum(map(ord, re.sub('[^A-Za-z0-9]', '', word))))


    # Alternate one-line solution as list comprehension:
    # return str(sum([ord(char) for char in re.sub('[^A-Za-z0-9]', '', word)]))
    

# --------------------------------------------------
def test_word2num():
    """Test word2num"""
    assert word2num('a') == '97'
    assert word2num('abc') == '294'  # 97 + 98 + 99
    assert word2num('ab\'c') == '294'
    assert word2num("4a-b'c,") == '346'
    assert word2num('hello') == '532'


# --------------------------------------------------
if __name__ == '__main__':
    main()
