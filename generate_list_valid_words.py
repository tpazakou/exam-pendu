"""
Depuis le fichier Lexique383.tsv, on récupère tous les mots de 6,7,8,9,10 lettres  trouvés dans la colonne orth
et on génère 5 fichiers textes contenant les mots (un mot par ligne, séparé par un \n:
dico_6_lettres.txt
dico_7_lettres.txt
dico_8_lettres.txt
dico_9_lettres.txt
dico_10_lettres.txt
"""
import functools

from unidecode import unidecode


def lire_filtrer_mots(chemin_lexique, longueur):
    """Lit le fichier tsv, retourne une liste de mots de longueur `longueur`
    Supprime ne prends pas les mots avec les espaces, supprime les doublons
    """
    lst_mots = []
    with open(chemin_lexique, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split('\t')
            mot = line[0].strip().split()[0]
            if len(mot) == longueur and " " not in mot and "-" not in mot:
                lst_mots.append(unidecode(mot).upper())
    return list(set(lst_mots))

def ecrire_liste_mots(liste_mots, longueur):
    """Génère un fichier texte contenant tous les mots pour une longueur donné"""
    chemin_dico_ecriture = f"data/dico_{longueur}_lettres.txt"
    with open(chemin_dico_ecriture, 'w', encoding='utf-8') as file:
        file.writelines(f"{mot}\n" for mot in liste_mots)

def main(path):
    for long in range(6,11):
        # génère la liste de mot pour la longueur donné
        lst_mots = lire_filtrer_mots(chemin_lexique=path, longueur=long)

        # Génère un fichier texte correspondant
        ecrire_liste_mots(lst_mots, longueur=long)

if __name__ == '__main__':
    chemin = "data/liste_francais.txt"
    main(path = chemin)