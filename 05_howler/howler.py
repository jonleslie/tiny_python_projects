#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2022-10-04
Purpose: Rock the Casbah
"""

import os
import sys
import argparse
from genericpath import isfile


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", type=str, help="Input string or file")

    parser.add_argument(
        "-o", "--outfile", help="Output filename", metavar="str", type=str, default=""
    )

    # parser.add_argument(
    #     "-o", "--outdir", help="Output directory", metavar="str", type=str, default=""
    # )

    parser.add_argument("-e",
                        "--ee",
                        help="Convert to lowercase",
                        action='store_true')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, "wt") if args.outfile else sys.stdout
    out_fh.write((args.text.lower() if args.ee else args.text.upper()) + "\n")
    out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
