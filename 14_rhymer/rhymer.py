#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2023-09-18
Purpose: Rock the Casbah
"""

import argparse
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make ryming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word

    consonant_clusters = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl',
                          'gr', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn',
                          'sp', 'st', 'sw', 'th', 'tr', 'tw', 'thw', 'wh',
                          'wr', 'sch', 'scr', 'shr', 'sph', 'spl', 'spr',
                          'squ', 'str', 'thr']
    # consonants = ''.join([c for c in string.ascii_lowercase if c not in 'aeiou'])
    consonant_clusters.extend([c for c in string.ascii_lowercase if c not in 'aeiou'])
    consonant_clusters.sort()
    # print(f'positional = "{word}"')
    # print(stemmer(word))
    lead, rest = stemmer(word.lower())
    if rest:
        print('\n'.join([c + rest for c in consonant_clusters if c != lead]))
    else:
        print(f'Cannot rhyme "{word}"')


def stemmer(word):
    """Return leading consonants (if any), and the 'stem' of word"""
    consonants = ''.join([c for c in string.ascii_lowercase if c not in 'aeiou'])
    vowels = 'aeiou'
    pattern = (
        '([' + consonants + ']+)?'
        '([' + vowels     + '])'
        '(.*)'
    )
    
    match = re.match(pattern, word)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)
    else:
        return (word, '')


def test_stemmer():
    """Test stemmer"""
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
