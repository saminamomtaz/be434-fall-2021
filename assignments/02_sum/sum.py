#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-09-15
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number',
                        metavar='int',
                        nargs = '+',
                        type=int,
                        help ='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = args.number
    indv_comps = ''
    
    if len (numbers) == 1:
        indv_comps = str (numbers [0])
    else:
        string_inps = [str (inp) for inp in numbers]
        indv_comps = ' + '.join(string_inps)

    print('{} = {}' .format(indv_comps,str(sum(numbers))))
    
# --------------------------------------------------
if __name__ == '__main__':
    main()