import math
from copy import copy


def generate_valid_words(all_words: list, letter_in:list[tuple[str, int]], letter_out:list) -> list:
    exclude_set = set(letter_out)
    filtered_words = [word for word in all_words if all(letter not in exclude_set for letter in word)]

    valid_words = [word for word in filtered_words if all(word[position] == letter for letter, position in letter_in)]

    return valid_words


def generate_best_letters(valid_words:list, possible_letters:list[str], letter_in, letter_out):
    nb_valid_words = len(valid_words)
    if nb_valid_words == 1:
        best_letters = set(possible_letters).intersection(valid_words[0])
        if best_letters:
            # return best_letters.pop(), float('inf')
            return f"Meilleure lettre: { best_letters.pop()} ({float('inf'):.2f} bits)."
        else:
            return "Won"

    res: dict[str, float] = {letter: 0 for letter in possible_letters}

    # Calculate remaining valid words for each letter across all pretend secret words
    for letter in possible_letters:
        total_possibilities = 0

        for secret_word in valid_words:
            # Create copies of the letter_in and letter_out to avoid modifying original lists
            copy_in = copy(letter_in)
            copy_out = copy(letter_out)

            # Determine if the letter is in the current secret_word
            if letter not in secret_word:
                copy_out.append(letter)
            else:
                correct_positions = [pos for pos, char in enumerate(secret_word) if char == letter]
                for pos in correct_positions:
                    copy_in.append((letter, pos))

            # Generate the new set of valid words based on this scenario
            new_valid_words = generate_valid_words(valid_words, copy_in, copy_out)
            total_possibilities += len(new_valid_words)

        # Calculate the average number of possibilities left for this letter
        res[letter] = total_possibilities / nb_valid_words

    # Calculate information gain in bits for each letter using log2
    dic_bits = {
        letter: math.log2(nb_valid_words / avg) if avg > 0 else float('inf')
        for letter, avg in res.items()
    }
    sorted_dic_bits = sorted(dic_bits.items(), key=lambda x: x[1], reverse=True)
    best_letter, nb_bits = sorted_dic_bits[0]

    return f"Meilleure lettre: {best_letter} ({nb_bits:.2f} bits)."









