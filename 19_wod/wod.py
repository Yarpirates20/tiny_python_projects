#!/usr/bin/env python3
"""
Author : Rob Samoraj <snailfail@vivaldi.net>
Date   : 2022-12-15
Purpose: Create Workout of (the) Day (WOD)
"""

import argparse
import csv
import io
from pprint import pprint
import random
import re
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='num',
                        type=int,
                        default=4)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)
    wod = random.sample(exercises, k=args.num)
    # print(wod) #debug 1
    new_wod = []
    for exercise in wod:
        name = exercise[0]
        chosen_reps = random.randint(exercise[1], exercise[2])
        if args.easy:
            chosen_reps = int(chosen_reps / 2)

        new_wod.append((name, chosen_reps))
        
    print(tabulate(new_wod, headers=('Exercise', 'Reps'))) # debug 2

    # random.sample(exercises, k=args.num)


# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""

    reader = csv.DictReader(fh, delimiter=',')
    exercises = []
    for rec in reader:
        name, reps = rec['exercise'], rec['reps']
        match = re.match(r'(\d+)-(\d+)', reps)
        low, high = int(match.group(1)), int(match.group(2))
        exercises.append((name, low, high))

    return exercises


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""

    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
