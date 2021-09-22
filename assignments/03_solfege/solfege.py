#!/usr/bin/env python3
"""
Author : saminamomtaz <saminamomtaz@localhost>
Date   : 2021-09-15
Purpose: Solfege with dictionaries
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('music',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dict_music = {'Do': 'A deer, a female deer',
                  'Re': 'A drop of golden sun',
                  'Mi': 'A name I call myself',
                  'Fa': 'A long long way to run',
                  'Sol': 'A needle pulling thread',
                  'La': 'A note to follow sol',
                  'Ti': 'A drink with jam and bread'}
    for elements in args.music:
        temp = dict_music.get(elements, 'I don\'t know')
        if elements in dict_music.keys():
            print(elements + ', ' + temp)
        else:
            print(temp + ' \"' + elements + '\"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
