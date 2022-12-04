#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.bet>
Date   : 2022-12-02
Purpose: Southern fry text
"""

import argparse
import os
import re
import string
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
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
        print(''.join([fry(word) for word in re.split(r'(\W+)', line)]))
 
        # words = []
        # for word in re.split(r'(\W+)', line.rstrip()):
        #     words.append(fry(word))
        # print(''.join(words))


# --------------------------------------------------
def fry(word):
    """ Drop the 'g' from a word ending in 'ing' and replace it with an apostrophe. Replace 'you' with 'y'all' """

    you_match = re.match('([yY])ou$', word)
    ing_match = re.search('(.+)ing$', word)

    if you_match:
        return you_match.group(1) + "'all"

    if ing_match:
        # return word[:-1] + "'"
        prefix = ing_match.group(1)
        if re.search('[aeiouy]', prefix, re.IGNORECASE):
            return prefix + "in'"

    return word


# --------------------------------------------------
def test_fry():
    """Test"""
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('your') == 'your'
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"


# --------------------------------------------------
if __name__ == '__main__':
    main()
