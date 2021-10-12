#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-10-11
Purpose: Common words between the files
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')
    parser.add_argument('input2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')
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
    file1_word = []
    file2_word = []
    for line in args.input1:
        file1_word += line.split()
    for line in args.input2:
        file2_word += line.split()
    common_word = sorted(set(file1_word) & set(file2_word))
    for word in common_word:
        print(word, file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
