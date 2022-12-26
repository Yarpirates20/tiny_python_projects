#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-12-24
Purpose: Generate random password from input file
"""

import argparse
import random
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Generate random password from input file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words per password',
                        metavar='word',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum length of word',
                        metavar='min',
                        type=int,
                        default=3)
    
    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum length of word',
                        metavar='max',
                        type=int,
                        default=6)
    
    parser.add_argument('-s',
                        '--seed',
                        help='Seed for random',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate the password',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = {}

    for fh in args.file:
        for line in fh:
            for word in map(clean, line.lower().split()):
                words[word] = 1

    print(words)


# --------------------------------------------------
def clean(word):
    """Remove non-letters from words"""

    sub = re.sub(r"[^\w]", '', word)
    return sub

# --------------------------------------------------
def test_clean():
    """Test clean() function"""
    assert clean('') == ''
    assert clean('states') == 'states'
    assert clean("Don't") == 'Dont'



# --------------------------------------------------
if __name__ == '__main__':
    main()
