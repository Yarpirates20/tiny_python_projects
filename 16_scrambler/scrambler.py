#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-12-04
Purpose: Scramble words
"""

import argparse
import os
import random
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    splitter = re.compile(r"([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    for line in args.text.splitlines():
        # print(''.join([scramble(word) for word in splitter.split(line)]))
        print(''.join(map(scramble, splitter.split(line))))
        

# --------------------------------------------------
def scramble(word):
    """Scramble a word"""

    if len(word) >= 3 and re.match(r'\w+', word):
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]

    return word

    # middle = list(word[1:-1])
    # random.shuffle(middle)
    # return f"{word[0]}{''.join(middle)}{word[-1]}" if len(word) > 3 else word


# --------------------------------------------------
def test_scramble():
    """Test scramble()"""
    state = random.getstate()
    random.seed(1)
    assert scramble('a') == 'a'
    assert scramble('ab') == 'ab'
    assert scramble('abc') == 'abc'
    assert scramble('abcd') == 'acbd'
    assert scramble('abcde') == 'acbde'
    assert scramble('abcdef') == 'aecbdf'
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
