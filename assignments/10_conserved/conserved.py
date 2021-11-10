#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-11-08
Purpose: Find conserved bases
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for sequences in args.FILE:
        print(sequences, end='')
    args.FILE.seek(0)
    seqs1 = [list(seqs.rstrip()) for seqs in args.FILE]
    pipe = list('|' * len(seqs1[0]))
    for cc in range(len(seqs1[0])):
        for rr in range(1, len(seqs1)):
            if seqs1[rr][cc] != seqs1[rr-1][cc]:
                pipe[cc] = 'X'
                break
    print(''.join(pipe))


# --------------------------------------------------
if __name__ == '__main__':
    main()
