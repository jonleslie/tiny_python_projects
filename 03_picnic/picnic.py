#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2022-09-28
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("item", metavar="str", nargs="+", help="Item(s) to bring")

    parser.add_argument("-s", "--sorted", help="Sort the item", action="store_true")

    parser.add_argument(
        "-n", "--no_oxford_comma", help="Remove the Oxford comma", action="store_true"
    )

    parser.add_argument(
        "-c",
        "--character",
        help="Character to separate with",
        metavar="str",
        type=str,
        default=",",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    flag_arg = args.sorted
    items = sorted(args.item) if flag_arg else args.item
    oxford = args.no_oxford_comma
    separator = args.character + " "

    bringing = ""
    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = " and ".join(items)
    else:
        items[-1] = "and " + items[-1]
        bringing = separator.join(items)
        last_separator = separator + "and"
        bringing = bringing.replace(last_separator, " and") if oxford else bringing

    print(f"You are bringing {bringing}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
