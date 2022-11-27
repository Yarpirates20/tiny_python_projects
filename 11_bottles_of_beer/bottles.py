#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-26
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Bottles of beer song",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("-n",
                        "--num",
                        help="Number of bottles",
                        metavar="number",
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(verse(args.num))


# --------------------------------------------------
def verse(bottle):
    """Sing a verse"""

    return str(bottle)


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == "\n".join([
        "1 bottle of beer on the wall,",
        "1 bottle of beer,",
        "Take one down, pass it around,",
        "No more bottles of beer on the wall!",
    ])


    two_bottles = verse(2)
    assert two_bottles == "\n".join([
        "2 bottles of beer on the wall,",
        "2 bottles of beer,",
        "Take one down, pass it around,",
        "1 bottle of beer on the wall!",
    ])


# --------------------------------------------------
if __name__ == "__main__":
    main()
