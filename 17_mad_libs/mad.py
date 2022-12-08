#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-12-07
Purpose: Mad Libs
"""

import argparse
import re


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
    text = args.file.read().rstrip()
    placeholders = re.findall('(<([^<>]+?)>)', text)

    # if len(placeholders) == 0:
    if not placeholders:
        print('This text has no placeholders.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
