#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-12-04
Purpose: Scramble words
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    for line in args.text.splitlines():
        print(line)


# --------------------------------------------------
def scramble(word):
    """Scramble a word"""

    pass


# --------------------------------------------------
def test_scramble():
    """Test scramble()"""
    state = random.getstate()
    random.seed(1)
    assert scramble('a') == 'a'
    assert scramble('ab') == 'ab'
    assert scramble('abc') == 'abc'
    assert scramble('abcd') == 'abcd'
    assert scramble('abcde') == 'abcde'
    assert scramble('abcdef') == 'abcdef'
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate()
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
