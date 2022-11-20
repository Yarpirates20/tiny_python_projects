#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-11-18
Purpose: Word count emulator
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Word count emulator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        help="Input files",
        metavar="FILE",
        nargs="*",  # 0 or more
        type=argparse.FileType("r"),
        default=[sys.stdin],  # Allows piping this program into cli
    )

    parser.add_argument(
        "-l",
        "--line",
        help="Line count",
        action='store_true'
    )

    parser.add_argument(
        "-w",
        "--word",
        help="Word count",
        action='store_true'
    )

    parser.add_argument(
        "-c",
        "--chars",
        help="Byte/character count",
        action='store_true'
    )        

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_words, total_bytes = 0, 0, 0

    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)

        if args.line or args.word or args.chars:
            print(f'{num_lines:8}' if args.line else '', end='')
            print(f'{num_words:8}' if args.word else '', end='')
            print(f'{num_bytes:8}' if args.chars else '', end='')
            print(f' {fh.name}')
        else:
            print(f"{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}")
        
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes

    if len(args.file) > 1:
        print(f"{total_lines:8}{total_words:8}{total_bytes:8} total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
