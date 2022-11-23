#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-21
Purpose: Replace all the vowels in text with the given vowel
"""

import argparse
import sys
import os



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

    # parser.add_argument('-f',
    #                     '--file',
    #                     nargs='?',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('r'),
    #                     default=sys.stdin)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    text = args.text
    vowel = args.vowel
    replaced = ''

    # If file argument is present in argparse, run the code for the text in that file and output it to the command line.

    for char in text:
        if char in 'aeiouAEIOU':
            if char.isupper():
                replaced += vowel.upper()
            elif char.islower():
                replaced += vowel.lower()
        else:
                replaced += char
        
    print(f'{replaced}\n', end='')

    # reg_ex = re.compile('[aeiou]', re.IGNORECASE)
    # text = args.text
    # vowel = args.vowel
    # m = reg_ex.match(vowel)

    # if m:
    #     replaced = reg_ex.sub(vowel, text)
    #     print(replaced)



# --------------------------------------------------
if __name__ == '__main__':
    main()
