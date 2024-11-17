import pytest
from solver import generate_valid_words

# à éxécuter depuis exam-pendu


def test_generate_valid_words_start_d():
    """On sait que la première lettre du mot est un D"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]


def test_generate_valid_words_vide():
    """Vérifie que la fonction retourne une liste vide si possible_words est vide."""
    assert generate_valid_words(
        possible_words=[],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == []


def test_generate_valid_words_valid_words():
    """
    Vérifie que, lorsque l'utilisateur n'a joué aucune lettre, la liste des mots
    possibles reste inchangée
    """
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[],
        letters_not_in_secret=[]
    ) == ["DEVANT", "ENTREE", "PORTER", "GAUCHE"]


def test_generate_valid_words_exclues_et_presentes():
    """
    Vérifie que les mots dont une lettre se trouve dans letters_not_in_secret
    et les mots qui n'ont pas des lettres jouées dans la bonne position
    ne sont pas inclus dans la liste des mots valides
    """
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE", "POTION"],
        letters_in_secret=[('P', 0)],
        letters_not_in_secret=["U", "E"]
    ) == ["POTION"]
