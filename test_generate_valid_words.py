import pytest
from solver import generate_valid_words

# need to write docstrings
# not in the right place
def test_generate_valid_words_start_d():
    """On sait que la première lettre du mot est un D"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]

def test_generate_valid_words_vide():
    assert generate_valid_words(
        possible_words=[],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == []

def test_generate_valid_words_valid_words():
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[],
        letters_not_in_secret=[]
    ) == ["DEVANT", "ENTREE", "PORTER", "GAUCHE"]

def test_generate_valid_words_exclues_et_presentes():
    """"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE", "POTION"],
        letters_in_secret=[('P', 0)],
        letters_not_in_secret=["U", "E"]
    ) == ["POTION"]