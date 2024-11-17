import pytest
from generate_dicts import lire_filtrer_mots

# à éxécuter depuis exam-pendu


def test_lire_filtrer_mots_longeur():
    """Vérifie que la fonction retourne uniquement les mots de 6 lettres"""
    texte = "tests/data_test/filetest1.txt"
    for i in range(len(lire_filtrer_mots(texte, 6))):
        assert len(lire_filtrer_mots(texte, 6)[i]) == 6


def test_lire_filtrer_mots_fichier_vide():
    """Vérifie que la fonction retourne une erreur lorsque le fichier est vide"""
    with pytest.raises(ValueError):
        lire_filtrer_mots("tests/data_test/filetest_empty.txt", 6)


def test_lire_filtrer_mots_normalisation():
    """Vérifie que les mots avec des accents, des espaces ou des tirets sont bien exclus de la liste."""
    texte = "tests/data_test/filetest1.txt"
    assert sorted(lire_filtrer_mots(texte, 6)) == ["ARRETE", "CAMION", "ECOUTE"]
