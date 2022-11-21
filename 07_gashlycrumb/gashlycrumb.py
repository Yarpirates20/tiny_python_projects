#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-20
Purpose: Prints line from a file starting with given letter
"""

import argparse
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Prints line from a file starting with given letter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letters', metavar='letter', nargs='+', help='Letters')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lookup = {line[0].upper(): line.rstrip() for line in args.file}

    for letter in args.letters:
        print(lookup.get(letter.upper(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
