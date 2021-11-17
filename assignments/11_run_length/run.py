#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-11-16
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text). read().rstrip()
    return args


# --------------------------------------------------
def rle(seq):
    """ Create RLE """
    final = []
    count = 1
    for ind, base in enumerate(seq):
        if ind == len(seq)-1:
            final += base
            if count > 1:
                final += str(count)
        elif base == seq[ind+1]:
            count = count+1
        else:
            final += base
            if count > 1:
                final += str(count)
            count = 1
    return ''.join(final)


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for seq in args.text.splitlines():
        print(rle(seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
