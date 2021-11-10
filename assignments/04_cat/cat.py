#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-09-26
Purpose: Python cat
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')
    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    for fh in args.FILE:
        for ii, line in enumerate(fh, start=1):
            if args.number:
                print(f"{ii:6}\t{line}", end='')
            else:
                print(f"{line}", end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
