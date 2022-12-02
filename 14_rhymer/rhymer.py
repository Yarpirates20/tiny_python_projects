#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-30
Purpose: Make rhyming words
"""

import argparse
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Make rhyming words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word to rhyme")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # word = args.word
    # consonants = [c for c in string.ascii_lowercase if c not in 'aeiou']
    # clusters = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'thw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph', 'spl', 'spr', 'squ', 'str', 'thr']

    prefixes = (list("bcdfghjklmnpqrstvwxyz") + (
        "bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr"
    ).split())

    start, rest = stemmer(args.word)

    if rest:
        words = "\n".join(sorted([p + rest for p in prefixes if p != start]))
        print(words)
    else:
        print(f'Cannot rhyme "{args.word}"')

    # letters = consonants + clusters
    # rhymes = []
    # s1, s2 = stemmer(word.lower())

    # rhymes = (i+s2 for i in letters if i != s1)

    # print('\n'.join(sorted(rhymes)))  if 'aeiou' in s1 or s2 else print(f'Cannot rhyme "{args.word}"')
    # print(f'{clusters[0]}{s2}')


# --------------------------------------------------
def stemmer(word):
    """Break word into consonants and the rest"""
    consonants = "".join(
        [c for c in string.ascii_lowercase if c not in "aeiou"])
    match = re.match(f"""
        ([{consonants}]+)?                      # capture one or more consonants, optional          
        ([aeiou])                               # capture at least one vowel
        (.*)                                    # zero or more of anything else
        """, word.lower(), re.VERBOSE)          # end capture
    if match:
        p1 = match.group(1) or ""
        p2 = match.group(2) or ""
        p3 = match.group(3) or ""
        return (p1, p2 + p3)
    else:
        return (word.lower(), "")


# --------------------------------------------------
def test_stemmer():
    """Test stemmer"""

    assert stemmer("") == ("", "")
    assert stemmer("cake") == ("c", "ake")
    assert stemmer("chair") == ("ch", "air")
    assert stemmer("APPLE") == ("", "apple")
    assert stemmer("RDNZL") == ("rdnzl", "")
    assert stemmer("123") == ("123", "")


# --------------------------------------------------
if __name__ == "__main__":
    main()
