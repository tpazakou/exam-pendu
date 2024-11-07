import pytest
from generate_dicts import lire_filtrer_mots

# they are working, but they are not in the correct folder


def test_lire_filtrer_mots_longeur():
    # a bit unorthodox, but since I used a set and not a list..
    texte = "tests/data_test/filetest1.txt"
    for i in range(len(lire_filtrer_mots(texte, 6))):
        assert len(lire_filtrer_mots(texte, 6)[i]) == 6


def test_lire_filtrer_mots_fichier_vide():
    with pytest.raises(ValueError):
        lire_filtrer_mots("tests/data_test/filetest_empty.txt", 6)


def test_lire_filtrer_mots_normalisation():
    texte = "tests/data_test/filetest1.txt"
    assert sorted(lire_filtrer_mots(texte, 6)) == ["ARRETE", "CAMION", "ECOUTE"]
