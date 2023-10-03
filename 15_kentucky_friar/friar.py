#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2023-10-02
Purpose: Rock the Casbah
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args
    

# --------------------------------------------------

def fry(word):
    if word.lower() == 'you':
        match = re.match('([yY])ou', word)
        return match.group(1) + "'all"
    if word.endswith('ing'):
        match = re.search('(.+)ing$', word)
        first = match.group(1).lower()
        if re.search('[aeiouy]', first):
            # return match[:-1] + "'"
            return match.group(1) + "in'"
        else:
            return word
    else:
        return word

def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"
    assert fry('father') == "father"

def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    # print(text)

    for line in args.text.splitlines():
        # print(line.split())
        # words = []
        # print(re.split(r'(\W+)', line.rstrip()))
        # for word in re.split(r'(\W+)', line.rstrip()):
        #     words.append(fry(word))
        # words = [fry(word) for word in re.split(r'(\W+)', line.rstrip())]
        
        print(''.join(map(fry, re.split(r'(\W+)', line.rstrip()))))

# --------------------------------------------------
if __name__ == '__main__':
    main()
