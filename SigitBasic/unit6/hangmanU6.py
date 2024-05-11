
#q6_4_1
def check_valid_input(letter_guessed: str, old_letters_guessed: str) -> bool:
    """
    Checks if the input string represents a single alphabetic character that hasn't been guessed before.

    Args:
        letter_guessed (str): The input string to be validated.
        old_letters_guessed (list): A list of previously guessed letters.

    Returns:
        bool: True if the input is a single alphabetic character that hasn't been guessed before, False otherwise.
    """

    letter_guessed = letter_guessed.lower()
    length = len(letter_guessed)
    has_multiple_chars = (length > 1)
    has_non_alphabetic = (not letter_guessed.isalpha())

    if ((has_multiple_chars or has_non_alphabetic) or (letter_guessed in old_letters_guessed)):
        return False
    else:
        return True


#q6_4_2
def try_update_letter_guessed(letter_guessed: str, old_letters_guessed: str) -> bool:
    """
    Tries to update the list of guessed letters with the new guess.

    Args:
        letter_guessed (str): The character entered by the player.
        old_letters_guessed (list): The list of letters the player has guessed so far.

    Returns:
        bool: True if the character is added successfully, False otherwise.
    """

    letter_guessed = letter_guessed.lower()
    if (check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        sorted_guesses = sorted(old_letters)
        arrow_separated = ' -> '.join(sorted_guesses)
        print(arrow_separated)
        return False

if __name__ == '__main__':
    """old_letters = ['a', 'b', 'c']
    print(f"Already guessed letters = {old_letters}\n"
          f"Checking validation for 'C': {check_valid_input('C', old_letters)}\n"
          f"Checking validation for 'ep': {check_valid_input('ep', old_letters)}\n"
          f"Checking validation for '$': {check_valid_input('$', old_letters)}\n"
          f"Checking validation for 's': {check_valid_input('s', old_letters)}")"""

    old_letters = ['a', 'p', 'c', 'f']

    result = try_update_letter_guessed('A', old_letters)
    print(f"{result}\n")

    result = try_update_letter_guessed('s', old_letters)
    print(f"{result}\n")

    print(f"old_letters = {old_letters}\n")

    result = try_update_letter_guessed('$', old_letters)
    print(f"{result}\n")

    result = try_update_letter_guessed('d', old_letters)
    print(f"{result}\n")

    print(f"old_letters = {old_letters}\n")
