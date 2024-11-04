from typing import Optional
def generate_valid_words(possible_words: list[str], letters_in_secret: list[tuple[str, int]], letters_not_in_secret: list[str]):
    """
    Génère une liste des mots valides.
    Mots valides : Mots qui ne contiennent pas des lettres exclues et ayant les lettres déjà dévinées
    à la bonne position.

    Args:
        possible_words (List[str]): Une liste de tous les mots potentiellement valides.

        letters_in_secret (List[Tuple[str, int]]): Une liste de tuples représentant les lettres déjà trouvées par
        l'utilisateur ainsi que leur position dans le mot.

        letters_not_in_secret (List[str]): Une liste des lettres déjà essayées par l'utilisateur mais qui ne sont
         pas dans le mot.

    Returns:
        List[str]: Une liste de mots valides qui répondent aux critères spécifiés.
    """

    valid_words = []

    for word in possible_words:
        valid = True
        for letter in word:
            if letter in letters_not_in_secret:
                valid = False
                break
        for letter, pos in letters_in_secret:
            if word[pos] != letter:
                valid = False
                break
        if valid:
            valid_words.append(word)
    return valid_words




def generate_best_letters(possible_words: list[str], letters_not_played: list[str], letters_in_secret: Optional[list[str]] = None,
    letters_not_in_secret: Optional[list[str]] = None) -> str:
    """
    Calcule la meilleure lettre à jouer en fonction de sa fréquence moyenne dans les mots restants.

    Arguments:
        possible_words (list[str]): Liste des mots restants.
        letters_not_played (list[str]): Liste des lettres pas encore jouées.

    Retourne:
        str: Message indiquant la meilleure lettre à jouer avec sa fréquence moyenne.
    """
    freq_moyennes = []
    for letter in letters_not_played:
        occ_total = 0
        for word in possible_words:
            occ_lettre = word.count(letter)
            occ_total += occ_lettre
        freq_moyenne = occ_total/len(possible_words)
        freq_moyennes.append(freq_moyenne)
    index = freq_moyennes.index(max(freq_moyennes))

    return (f"La meilleure lettre à jouer est {letters_not_played[index]}.")















