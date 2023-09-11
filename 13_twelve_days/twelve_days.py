#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2023-09-03
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if not 1 <= args.num <= 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # print('\n\n'.join([verse(day + 1) for day in range(args.num)]),
    #       file=args.outfile)
    verses = map(verse, range(1, args.num + 1))
    print('\n\n'.join(verses), file=args.outfile)


def verse(day):
    """Create a new verse"""
    ordinal = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"
    ]

    gifts = [
        'A partridge in a pear tree',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,'
    ]

    last_line = "A partridge in a pear tree." if day == 1 else\
        "And a partridge in a pear tree."

    first_line = f'On the {ordinal[day - 1]} day of Christmas,'
    second_line = "My true love gave to me,"
    verse_list = [first_line, second_line]
    # for i in reversed(range(day)):
    #     if i > 0:
    #         verse_list.append(gifts[i])
    #     else:
    #         verse_list.append(last_line)
    # verse_list.append(gifts[i]) for i in reversed(range(1, day))
    # verse_list.append(last_line)

    verse_list.extend(reversed(gifts[1:day]))
    verse_list.append(last_line)

    return '\n'.join(verse_list)


def test_verse():
    """Test verse"""
    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])

    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
