#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-12-07
Purpose: Mad Libs
"""

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs for testing',
                        metavar='str',
                        type=str,
                        nargs='*')

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().rstrip()
    # print('inputs =', args.inputs)
    blanks = re.findall('(<([^<>]+?)>)', text)

    # if len(placeholders) == 0:
    if not blanks:
        # print(f'"{args.file.name}" has no placeholders.', file=sys.stderr)
        # sys.exit(1)
        sys.exit(f'"{args.file.name}" has no placeholders.')


    for placeholder, name in blanks:
        article = 'an' if name[0].lower() in 'aeiou' else 'a'
        answer = inputs.pop(0) if inputs else input(f'Give me {article} {name}: ')
        text = re.sub(placeholder, answer, text, count=1)

    print(text)
        


# --------------------------------------------------
if __name__ == '__main__':
    main()
