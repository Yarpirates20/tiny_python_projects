#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-12-24
Purpose: Generate random password from input file
"""

import argparse
import random
import re
import string


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
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    # for num in args.num:
    passwords = [''.join(random.sample(words, k=args.num_words)) for _ in range(args.num)]

    if args.l33t:
        encoded = map(l33t, passwords)
        print('\n'.join(encoded))
    # print(''.join(random.sample(words, k=args.num)))
    else:
        print('\n'.join(passwords))

# --------------------------------------------------
def clean(word):
    """Remove non-letters from words"""

    sub = re.sub(r"[^A-Za-z]", '', word)
    return sub


#--------------------------------------------------
def ransom(word):
    ransom_word = [x.upper() if random.choice([False, True]) else x.lower() for x in word]

    return ''.join(ransom_word)


# --------------------------------------------------
def l33t(text):
    
    l33t_code = {
        'a': '@',
        'A': '4',
        'O': '0',
        't': '+',
        'E': '3',
        'I': '1',
        'S': '5'
    }
    # leet_speak = []
    # for char in text:
    #     ransom(char)
    #     l33t_code.get(char, char)
    #     leet_speak.append(char)

    # leet_speak.append(random.choice(string.punctuation))

    # return ''.join(leet_speak)
    ransomed_text = ransom(text)
    leet_speak = [l33t_code.get(char, char) for char in ransomed_text]
    leet_speak.append(random.choice(string.punctuation))

    return ''.join(leet_speak)
    # punctuation = random.choice(string.punctuation)
    # leet_speak.append(punctuation)

    # return (''.join(ransom(leet_speak))) 


# --------------------------------------------------
if __name__ == '__main__':
    main()
