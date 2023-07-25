#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2023-07-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if not isinstance(args.num, int):
        parser.error(f"invalid int value: '{args.num}'")

    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------

def main():
    """Make a jazz noise here"""

    args = get_args()
    num_arg = args.num

    # for i in range(num_arg, 0, -1):
    #     print(verse(i))

    print('\n\n'.join(map(verse, range(num_arg, 0, -1))))


def verse(bottle):
    """Sing a verse"""

    n = bottle
    n_1 = 'No more' if n == 1 else n-1
    b1 = "bottle" if n == 1 else "bottles"
    b2 = "bottle" if n - 1 == 1 else "bottles"

    return '\n'.join([
        f'{n} {b1} of beer on the wall,',
        f'{n} {b1} of beer,',
        'Take one down, pass it around,',
        f'{n_1} {b2} of beer on the wall!'
    ])


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
