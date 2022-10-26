#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2022-10-19
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter", metavar="letter", nargs="+", help="Letter(s)", type=str
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    d = {}

    # for line in args.file:
    #     key = line[0].lower()
    #     d[key] = line.rstrip()
    d = {line[0].lower(): line.rstrip() for line in args.file}

    for letter in args.letter:
        if letter.lower() not in d:
            print(f'I do not know "{letter}".')
        else:
            print(d.get(letter.lower()))


# --------------------------------------------------
if __name__ == "__main__":
    main()
