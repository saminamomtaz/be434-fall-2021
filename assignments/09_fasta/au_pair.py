#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-11-01
Purpose: Split interleaved/paired reads
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    os.makedirs(args.outdir, exist_ok=True)
    for files in args.FILE:
        root, ext = os.path.splitext(os.path.basename(files.name))
        forward = os.path.join(args.outdir, root + '_1' + ext)
        reverse = os.path.join(args.outdir, root + '_2' + ext)
        with open(forward, 'wt', encoding="utf8") as out_fh1:
            with open(reverse, 'wt', encoding="utf8") as out_fh2:
                reader = SeqIO.parse(files.name, 'fasta')
                flag = 0
                for rec in reader:
                    if flag == 0:
                        print('>' + rec.id, file=out_fh1)
                        print(str(rec.seq), file=out_fh1)
                        flag = 1
                    else:
                        print('>' + rec.id, file=out_fh2)
                        print(str(rec.seq), file=out_fh2)
                        flag = 0
    print(f"Done, see output in \"{args.outdir}\"")


# --------------------------------------------------
if __name__ == '__main__':
    main()
