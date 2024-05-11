
def is_valid_input(letter_guessed: str) -> bool:
    """
    Checks if the input string represents a single alphabetic character.

    Args:
        letter_guessed (str): The input string to be validated.

    Returns:
        bool: True if the input is a single alphabetic character, False otherwise.
    """

    letter_guessed = letter_guessed.lower()
    length = len(letter_guessed)
    has_multiple_chars = (length > 1)
    has_non_alphabetic = (not letter_guessed.isalpha())

    if has_multiple_chars or has_non_alphabetic:
        return False
    else:
        return True

if __name__ == '__main__':
    print(f"For input 'a': {is_valid_input('a')}\n"
          f"For input 'A': {is_valid_input('A')}\n"
          f"For input '$': {is_valid_input('$')}\n"
          f"For input 'ab': {is_valid_input('ab')}\n"
          f"For input 'app$': {is_valid_input('app$')}\n\n")

    help(is_valid_input)