#!/usr/bin/env python3
"""
Author : jon <jon@localhost>
Date   : 2023-07-08
Purpose: Rock the Casbah
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Heap abuse", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        help="Number of adjectives",
        metavar="adjectives",
        type=int,
        default=2,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="Number of insults",
        metavar="adjectives",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="seed", type=int, default=None
    )

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    assert len(adjectives) == 36
    assert len(nouns) == 39

    adj_arg = args.adjectives
    ins_arg = args.number
    # seed_arg = args.seed

    for _ in range(ins_arg):
        noun_list = random.choice(nouns)
        # adjective_list = random.sample(adjectives.split(), k=adj_arg)
        adj = ", ".join(random.sample(adjectives, k=adj_arg))
        print(f"You {adj} {noun_list}!")


adjectives = """
bankrupt base caterwauling corrupt cullionly detestable dishonest false 
filthsome filthy foolish foul gross heedless indistinguishable infected 
insatiate irksome lascivious lecherous loathsome lubbery old peevish 
rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced 
toad-spotted unmannered vile wall-eyed
""".strip().split()

nouns = """
Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle 
coward coxcomb cur dandy degenerate fiend fishmonger food gull harpy jack
jolthead knave liar lunatic maw milksop minion ratcatcher recreant rogue 
scold slave swine traitor varlet villain worm
""".strip().split()


# --------------------------------------------------
if __name__ == "__main__":
    main()
