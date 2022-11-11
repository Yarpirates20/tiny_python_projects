#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-11
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', type=str, help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Encode text using Jump the Five"""

    args = get_args()
    text = args.text
    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    for char in text:
        if char in jumper:
            print(jumper.get(char), end='')
        else:
            print(char, end='')

    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
