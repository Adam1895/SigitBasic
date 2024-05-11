
#q7_3_1
def show_hidden_word(secret_word: str, old_letters_guessed: list) -> str:
    """
    Returns a string representing the secret word with correctly guessed letters revealed and unguessed letters replaced by underscores.

    Args:
        secret_word (str): The secret word to be guessed.
        old_letters_guessed (list): A list of letters that have been guessed so far.

    Returns:
        str: A string representing the secret word with correctly guessed letters revealed and unguessed letters replaced by underscores separated by spaces.
    """
    result = []
    for char in secret_word:
        if (char in old_letters_guessed):
            result.append(char)
        else:
            result.append('_')

    return ' '.join(result)


#q7_3_2
def check_win(secret_word: str, old_letters_guessed: list) -> bool:
    """
    Check if the player has successfully guessed all the letters in the secret word.

    Args:
        secret_word (str): The secret word to be guessed.
        old_letters_guessed (list): A list of letters that have been guessed so far.

    Returns:
        bool: True if all the letters in the secret word are present in the list of guessed letters, False otherwise.
    """
    for char in set(secret_word):
        if char not in old_letters_guessed:
            return False
    return True

if __name__ == '__main__':
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))

    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))

    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))