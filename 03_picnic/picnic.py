#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-07
Purpose: Print items on picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print items on picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='item',
                        type=str,
                        nargs='+',
                        help='Item(s) to bring')


    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Output formatted list of items to bring to picnic"""

    args = get_args()
    items = args.items
    # print(args.items)
    # print(args.sorted)

    if len(items) == 1:
        print(f'You are bringing {items[0]}.')
    elif len(items) == 2:
        print(f'You are bringing {items[0]} and {items[1]}.')
    else:
        print('You are bringing ' + ', '.join(items[:-1]) + ', and ' + items[-1] + '.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
