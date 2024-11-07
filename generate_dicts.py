from unidecode import unidecode

"""
Depuis le fichier liste_mots.txt, on récupère tous les mots de 6,7,8,9,10 lettres.
et on génère 5 fichiers textes contenant les mots en fonction de leur taille (un mot par ligne, séparé par un \n):
dico_6_lettres.txt
dico_7_lettres.txt
dico_8_lettres.txt
dico_9_lettres.txt
dico_10_lettres.txt
On enlève les accents, les espaces, les tirets et les mots en double.
"""


def lire_filtrer_mots(chemin_lexique: str, longueur: int) -> list[str]:
    """
    Lit le fichier du lexique trouvé dans le chemin indiqué et retourne une liste de mots de la longueur donnée,
    en majuscules, sans accents, apostrophes et tirets.

    Args:
        chemin_lexique (str): Chemin d'accès au fichier de lexique contenant les mots
        longueur (int): Longueur des mots

    Returns:
        list: Une liste de mots filtrés, en majuscules et sans accents,
              correspondant à la longueur spécifiée.

    Raises:
        ValueError: Si le fichier est vide.

    """
    with open(chemin_lexique, 'r', encoding='utf8') as f:
        # set pour éviter les doublons
        liste_mots = set()
        texte = f.readlines()
        if texte == []:
            raise ValueError("Votre fichier est vide.")
        else:
            for line in texte:
                # choisir le premier mot de la ligne
                mot = line.strip()
                mot = mot.split(" ")[0]
                if len(mot) == longueur and "'" not in mot and "-" not in mot:
                    liste_mots.add(unidecode(mot.upper()))
    return list(liste_mots)


def ecrire_liste_mots(liste_mots: list, longueur: int) -> None:
    """Génère un fichier texte contenant tous les mots pour une longueur donné"""

    chemin_dico_ecriture: str = f"data/dico_{longueur}_lettres.txt"

    with open(chemin_dico_ecriture, 'w', encoding='utf-8') as file:
        file.writelines(f"{mot}\n" for mot in liste_mots)


def main(chemin: str) -> None:
    for long in range(6, 11):
        # génère la liste de mot pour la longueur donné
        lst_mots = lire_filtrer_mots(chemin_lexique=chemin, longueur=long)

        # Génère un fichier texte correspondant
        ecrire_liste_mots(lst_mots, longueur=long)


if __name__ == '__main__':
    chemin = "data/liste_mots.txt"
    main(chemin=chemin)
