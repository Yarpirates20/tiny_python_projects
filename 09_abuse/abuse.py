#!/usr/bin/env python3
"""
Author : Rob Samoraj, <snailfail@vivaldi.net>
Date   : 2022-11-23
Purpose: Create insults
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create insults',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='The number of insults',
                        metavar='int',
                        type=int,
                        default=3)
    parser.add_argument('-a',
                        '--adjectives',
                        help='The number of adjectives per insult',
                        metavar='int',
                        type=int,
                        default=2)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false 
    filthsome filthy foolish foul gross heedless indistinguishable infected insatiate irksome 
    lascivious lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous scurvy 
    slanderous sodden-witted thin-faced toad-spotted unmannered vile wall-eyed
    """.split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool gull harpy jack jolthead knave liar lunatic maw milksop minion ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.split()

    random.seed(args.seed)

    for _ in range(args.number):
        random_adjective = random.sample(adjectives, args.adjectives)
        random_noun = random.choice(nouns)
        
        formatted = ''
        if args.adjectives == 1:
            formatted = random_adjective[0]
        elif args.adjectives == 2:
            formatted = ', '.join(random_adjective)
        else:
            formatted = ', '.join(random_adjective[:-1]) + ', ' + random_adjective[-1]

        print(f'You {formatted} {random_noun}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
