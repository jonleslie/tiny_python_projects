#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2022-10-04
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Jump the Five"""

    args = get_args()
    invalue = args.input

    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    out = ""
    for char in invalue:
        out += jumper.get(char, char)

    print(out)


# --------------------------------------------------
if __name__ == "__main__":
    main()
