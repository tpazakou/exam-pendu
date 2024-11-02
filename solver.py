import math
from copy import copy


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




def generate_best_letters(possible_words:list, letters_not_played:list[str]):


    letter_average = []

    for letter in letters_not_played:
        total_possibilities = 0
        letters_in_secret = []
        letters_not_in_secret = []

        for word in possible_words:
            secret_word = word
            if letter in secret_word:
                letter_pos_tuple = (letter, secret_word.index(letter))
                letters_in_secret.append(letter_pos_tuple)
            else:
                letters_not_in_secret.append(letter)

            nb_of_valid_words = len(generate_valid_words(possible_words, letters_in_secret, letters_not_in_secret))
            total_possibilities += nb_of_valid_words
        average = total_possibilities/len(possible_words)
        letter_average.append(average)

    minimum = min(letter_average)
    pos = letter_average.index(minimum)
    suggested_letter = letters_not_played[pos]
    return f"La meilleure lettre à jouer est {suggested_letter}"













