#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2023-07-11
Purpose: Rock the Casbah
"""

import argparse
import random
import os
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()

    num_mutations = round(len(args.text) * args.mutations)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    
    random.seed(args.seed, version=0)

    indexes = random.sample(range(len(args.text)), num_mutations)

    print(f'You said: "{args.text}"')

    for i in indexes:
        avail_alpha = "".join([x for x in alpha if x not in args.text[i]])
        # print(f' {i:2} {args.text[i]} changes to {random.choice(avail_alpha)}')
        args.text = args.text[:i] + random.choice(avail_alpha) + args.text[i+1:]

    print(f'I heard : "{args.text}"')



# --------------------------------------------------
if __name__ == '__main__':
    main()
