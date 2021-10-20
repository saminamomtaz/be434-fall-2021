#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-10-18
Purpose: Expand IUPAC codes
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequences',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

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
    iupac_code = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T', 'U': 'U',
                  'R': 'AG', 'Y': 'CT', 'S': 'GC', 'W': 'AT', 'K': 'GT',
                  'M': 'AC', 'B': 'CGT', 'D': 'AGT', 'H': 'ACT', 'V': 'ACG',
                  'N': 'ACGT'}
    for items in args.sequences:
        temp = ''
        for keys in items:
            if len(iupac_code.get(keys)) == 1:
                temp += iupac_code.get(keys)
            else:
                temp += '[' + iupac_code.get(keys) + ']'
        print(f"{items} {temp}", file=args.outfile)
    if args.outfile.name != '<stdout>':
        print(f"Done, see output in \"{args.outfile.name}\"")


# --------------------------------------------------
if __name__ == '__main__':
    main()
