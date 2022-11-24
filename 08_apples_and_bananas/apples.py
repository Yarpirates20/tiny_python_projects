#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-21
Purpose: Replace all the vowels in text with the given vowel
"""

import argparse
import sys
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Replace all the vowels in text with the given vowel',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        choices=['a', 'e', 'i', 'o', 'u'],
                        metavar='str',
                        type=str,
                        default='a')

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

    # replaced = ''

    # for char in text:
    #     if char in 'aeiouAEIOU':
    #         if char.isupper():
    #             replaced += vowel.upper()
    #         elif char.islower():
    #             replaced += vowel.lower()
    #     else:
    #             replaced += char

    # print(f'{replaced}\n', end='')

    # 1. Using str_replace()
    # for v in 'aeiou':
    #     text = text.replace(v, vowel).replace(v.upper(), vowel.upper())

    # print(text)

    # 2. Using str.translate
    # trans = str.maketrans('aeoiuAEIOU', vowel * 5 + vowel.upper() * 5)
    # print(text.translate(str.maketrans(trans)))

    # 3. List comprehension (rewritten as if EXPRESSIONS)
    # new_text = [
    #     vowel if char in 'aeiou' else
    #     vowel.upper() if char in 'AEIOU' else char
    #     for char in text
    # ]

    # print(''.join(new_text))

    # 4. Solution with function incorporating list comprehension.
    # def new_char(char):
    #     return vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char

    # new_text = [new_char(char) for char in text]

    # print(''.join((new_text)))

    # 5. Solution with map function.
    # text = map(lambda c: vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c, text)

    # print(''.join(text))

    # 6. Using map with a defined function
    # def new_char(char):
    #     return vowel if char in 'aeiou' else vowel.upper(
    #     ) if char in 'AEIOU' else char

    # print(''.join(map(new_char, text)))

    # 7. Regular expression solution
    text = re.sub('[AEIOU]', vowel.upper(), re.sub('[aeiou]', vowel, text))
    print(text)

    # -- My first regular expression attempt --
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
