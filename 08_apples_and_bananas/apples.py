#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-21
Purpose: Replace all the vowels in text with the given vowel
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Replace all the vowels in text with the given vowel',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        choices=['a', 'e', 'i', 'o', 'u'],
                        metavar='str',
                        type=str,
                        default='a')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    reg_ex = re.compile('[aeiou]')
    text = args.text
    vowel = args.vowel
    m = reg_ex.match(vowel)

    if m:
        replaced = reg_ex.sub(vowel, text)
        print(replaced)



# --------------------------------------------------
if __name__ == '__main__':
    main()
