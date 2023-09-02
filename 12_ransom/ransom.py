#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2023-08-29
Purpose: Rock the Casbah
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    # print(args.text)
    # seed_arg = args.seed
    # text_arg = args.text

    # new_text = ''
    # for char in args.text:
    #     new_text += choose(char=char)
    # print(new_text)
    # print(''.join([choose(char) for char in args.text]))
    print(''.join(map(choose, args.text)))


def choose(char):
    '''Randomly choose an upper or lowercase letter to return'''
    return char.upper() if random.choice([0, 1]) else char.lower()


def test_choose():
    """Test choose()"""
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'c'
    assert choose('d') == 'd'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
