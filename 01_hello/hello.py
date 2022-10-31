#! /usr/bin/env python3
# Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
args = parser.parse_args()
name = args.name
print('Hello, ' + name + '!')