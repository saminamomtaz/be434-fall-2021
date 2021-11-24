#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-11-19
Purpose: Python grep
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')
    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        default=False,
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_file = len(args.files)
    for fh in args.files:
        for lines in fh:
            if args.insensitive:
                temp = re.search(args.pattern, lines, re.I)
            else:
                temp = re.search(args.pattern, lines)
            if temp:
                if num_file > 1:
                    print(f"{fh.name}:{lines}", end='', file=args.outfile)
                else:
                    print(lines, end='', file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
