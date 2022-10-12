#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2022-10-06
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Emulate wc (word count)"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="*",
        default=[sys.stdin],
        type=argparse.FileType("rt"),
        help="Input file(s)",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    tot_lines, tot_words, tot_bytes = 0, 0, 0

    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        tot_lines += num_lines
        tot_words += num_words
        tot_bytes += num_bytes
        print(f"{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}")

    if len(args.file) > 1:
        print(f"{tot_lines:8}{tot_words:8}{tot_bytes:8} total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
