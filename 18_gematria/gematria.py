#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2023-10-16
Purpose: Rock the Casbah
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def word2num(word):
    """Sum the ordinal values of all the characters"""
    return str(sum(map(ord, re.sub('[^A-Za-z0-9]', '', word))))


def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


def main():
    """Make a jazz noise here"""

    args = get_args()
    # print(args.text)

    for line in args.text.splitlines():
        print(' '.join(map(word2num, line.split())))


# --------------------------------------------------
if __name__ == '__main__':
    main()
