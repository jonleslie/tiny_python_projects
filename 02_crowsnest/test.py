#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = "./crowsnest.py"
consonant_words = [
    "brigantine",
    "clipper",
    "dreadnought",
    "frigate",
    "galleon",
    "haddock",
    "junk",
    "ketch",
    "longboat",
    "mullet",
    "narwhal",
    "porpoise",
    "quay",
    "regatta",
    "submarine",
    "tanker",
    "vessel",
    "whale",
    "xebec",
    "yatch",
    "zebrafish",
]
vowel_words = ["aviso", "eel", "iceberg", "octopus", "upbound"]
template = "Ahoy, Captain, {} {} off the larboard bow!"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("a", word)


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("an", word)


# --------------------------------------------------
def test_article_consonant_upper():
    """Brigatine -> A Brigatine"""

    for word in consonant_words:
        out = getoutput(f"{prg} {word.title()}")
        assert out.strip() == template.format("A", word.title())


# --------------------------------------------------
def test_article_vowel_upper():
    """Octopus -> An Octopus"""

    for word in vowel_words:
        out = getoutput(f"{prg} {word.title()}")
        assert out.strip() == template.format("An", word.title())


# --------------------------------------------------
def test_side_parses():
    """-s -> Ahoy, Captain, ...off the starboard bow!"""

    for flag in ["-s", "--starboard"]:
        out = getoutput(f'{prg} {"octopus"} {flag}')
        template2 = "Ahoy, Captain, {} {} off the {} bow!"
        assert out.strip() == template2.format("an", "octopus", "starboard")
