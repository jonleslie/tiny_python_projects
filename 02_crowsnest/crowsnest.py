#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2022-09-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")

    parser.add_argument('-s',
                        '--side',
                        metavar="side",
                        help="starboard or larboard",
                        default='larboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.side.lower()
    article = ""
    if word[0].isupper():
        article = "An" if word[0].lower() in "aeiou" else "A"
    else:
        article = "an" if word[0].lower() in "aeiou" else "a"
    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
