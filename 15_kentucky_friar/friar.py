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

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    for line in args.text.splitlines():
        print(line.split())


# --------------------------------------------------
def fry(word):
    if word == 'you':
        return "y'all"
    elif word == 'You':
        return "Y'all"

# --------------------------------------------------
def test_fry():
    """Test"""
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"




# --------------------------------------------------
if __name__ == '__main__':
    main()
