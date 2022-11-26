#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-25
Purpose: Telephone
"""

import argparse
import random
import os
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if not 0 <= args.mutations < 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    # args = get_args()
    # text = args.text
    # random.seed(args.seed)
    # alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    # len_text = len(text)
    # num_mutations = round(args.mutations * len_text)
    # new_text = text

    # for i in random.sample(range(len_text), num_mutations):
    #     new_char = random.choice(alpha.replace(new_text[i], ''))
    #     new_text = new_text[:i] + new_char + new_text[i + 1:]

    # print(f'You said: "{text}"\nI heard : "{new_text}"')

    args = get_args()
    text = args.text
    random.seed(args.seed)
    
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    num_mutations = round(len(text) * args.mutations)
    
    new_text = text

    for i in random.sample(range(len(text)), num_mutations):
        new_char = random.choice(alpha.replace(new_text[i], ''))
        new_text = new_text[:i] + new_char + new_text[i + 1:] 

    # indexes = random.sample(range(len(text)), num_mutations)

    # for char in text:
    #     new_text += random.choice(alpha) if text.index(
    #         char) in indexes else char

    print(f'You said: "{text}"')
    print(f'I heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
