#!/usr/bin/env python3
"""tests for picnic.py"""

from ast import arg
from doctest import OutputChecker
import os
from subprocess import getoutput

prg = "./picnic.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["", "-h", "--help"]:
        out = getoutput(f"{prg} {flag}")
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f"{prg} chips")
    assert out.strip() == "You are bringing chips."


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == "You are bringing soda and french fries."


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f"{prg} {arg}")
    expected = (
        "You are bringing potato chips, coleslaw, " "cupcakes, and French silk pie."
    )
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f"{prg} -s soda candy")
    assert out.strip() == "You are bringing candy and soda."


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = "bananas apples dates cherries"
    out = getoutput(f"{prg} {arg} --sorted")
    expected = "You are bringing apples, bananas, cherries, and dates."
    assert out.strip() == expected


# --------------------------------------------------
def test_removal_of_oxford_comma():
    """Oxford comma removed with optional arguement"""

    arg = "bananas apples dates cherries"
    out = getoutput(f"{prg} {arg} --no_oxford_comma")
    expected = "You are bringing bananas, apples, dates and cherries."
    assert out.strip() == expected


# --------------------------------------------------
def test_alternative_separator():
    """Different separator incorporated"""

    arg = "bananas apples dates cherries"
    out = getoutput(f"{prg} {arg} -c _")
    expected = "You are bringing bananas_ apples_ dates_ and cherries."
    assert out.strip() == expected
