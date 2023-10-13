#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2023-10-11
Purpose: Rock the Casbah
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs='*')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    # print(inputs)
    text = args.file.read().rstrip()

    matches = re.findall('(<([^<>]+)>)', text)
    if not matches:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    tmpl = 'Give me {} {}: '
    for placeholder, name in matches:
        # if inputs:
        #     value = inputs.pop(0)
        # else:
        #     value = input(f'Give me an {name}: ')
        article = 'an' if name.lower()[0] in 'aeiou' else 'a'
        value = inputs.pop(0) if inputs else input(tmpl.format(article, name))
        text = re.sub('(<[^<>]+>)', value, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
