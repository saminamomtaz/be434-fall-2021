#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-10-25
Purpose: Common k-mers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')
    parser.add_argument('input2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
def count_kmers(fh, k):
    """ Count k-mers in a file """

    file_kmer = {}
    for line in fh:
        for seq in line.split():
            temp = find_kmers(seq, k)
            for kmer in temp:
                file_kmer[kmer] = file_kmer.get(kmer, 0)+1
    return file_kmer


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1_kmer = count_kmers(args.input1, args.kmer)
    file2_kmer = count_kmers(args.input2, args.kmer)
    common_kmer = set(list(file1_kmer.keys())) & set(list(file2_kmer.keys()))
    for i in common_kmer:
        print(f"{i:10}{file1_kmer.get(i):6}{file2_kmer.get(i):6}")


# --------------------------------------------------
if __name__ == '__main__':
    main()
