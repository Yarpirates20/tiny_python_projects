#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-28
Purpose: Twelve Days of Christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days',
                        metavar='days',
                        type=int,
                        default=12)

    args = parser.parse_args()

    if not 1 <= args.num <= 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout

    # for n in range(1, args.num + 1):
        # out_fh.write(verse(n) + '\n' if n == args.num else verse(n) + '\n\n')
        # print(verse(n))
        # print()

    # out_fh.close()

    # verses = [
    #     verse(day)
    #     for day in range(1, args.num + 1)
    # ]

    ###
    # Map takes function as first argument, and the second argument is something that produces a sequence, such as range function, which will produce numbers 1 - 12, each will be given as argument to verse and the output will go into verses.
    verses = map(verse, range(1, args.num + 1))
    

    print('\n\n'.join(verses), file=args.outfile)


# --------------------------------------------------
def verse(day):
    """Create a verse"""

    ordinal = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        8: 'eighth',
        9: 'ninth',
        10: 'tenth',
        11: 'eleventh',
        12: 'twelfth',
    }

    gifts = {
        1: 'And a partridge in a pear tree.',
        2: 'Two turtle doves,',
        3: 'Three French hens,',
        4: 'Four calling birds,',
        5: 'Five gold rings,',
        6: 'Six geese a laying,',
        7: 'Seven swans a swimming,',
        8: 'Eight maids a milking,',
        9: 'Nine ladies dancing,',
        10: 'Ten lords a leaping,',
        11: 'Eleven pipers piping,',
        12: 'Twelve drummers drumming,'
    }

    lines = [
        f'On the {ordinal[day]} day of Christmas,',
        'My true love gave to me,',
    ]

    for i in range(day, 0, -1):
        lines.append(gifts[i]) if day > 1 else lines.append(
            gifts[i][4:].capitalize())

    # lines.append('\n')
    return '\n'.join(lines)


# --------------------------------------------------
def test_verse():
    """ Test verse """

    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])
    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
