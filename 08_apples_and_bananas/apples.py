#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2022-10-26
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel to substitute",
        metavar="vowel",
        type=str,
        default="a",
        choices=list("aeiou"),
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    text = args.text
    # vowels = 'aeiou'
    lookup = str.maketrans("aeiouAEIOU", vowel * 5 + vowel.upper() * 5)

    # new_text = [
    #     vowel if c in vowels else vowel.upper() if c in vowels.upper() else c
    #     for c in text
    # ]

    text = text.translate(lookup)

    # text = ''
    # print(text.join(new_text))
    print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
