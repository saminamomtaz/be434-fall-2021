#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-10-01
Purpose: Translate DNA/RNA to AA
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')
    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    codon_table = {}
    for line in args.codons:
        temp = line.rstrip().split()
        codon_table[temp[0]] = temp[1]
    k = 3
    seq = args.sequence
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        print(f"{codon_table.get(codon.upper(), '-')}",
              end='', file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()