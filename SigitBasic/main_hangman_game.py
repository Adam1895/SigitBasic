#=======================================
# Python: 3.8
# Game: HangMan game
# By: Adam shapiro
#=======================================


import random

HANGMAN_PHOTOS = {
    1: """
    x-------x
    """,
    2: """
    x-------x
    |
    |
    |
    |
    |
    """,
    3: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}

HANGMAN_ASCII_ART = """  
Welcome to Adam's Hangman game
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/
"""

MAX_TRIES = 6

secret_word = ""

old_letters_guessed = []

num_of_tries = 0


def welcome_screen() -> None:
    """
    Prints the welcome screen
    """
    print(f"{HANGMAN_ASCII_ART}\n"
          f"Max tries: {MAX_TRIES}\n")


def choose_word(file_path: str, index: int) -> str:
    """
    Chooses a secret word from a text file at the specified index.

    Args:
        file_path (str): The path to the text file containing the words.
        index (int): The position of the desired word in the file (starting from 1).

    Returns:
        str: The secret word at the specified index.
    """
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            if index < 1 or index > len(words):
                print("Picked a random word!\n")
                index = random.randint(1, len(words))
            else:
                print("Great choice!\n")
            secret_word = words[index - 1]
            return secret_word
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return ""


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
        if char in old_letters_guessed:
            result.append(char)
        else:
            result.append('_')

    return ' '.join(result)


def check_valid_input(letter_guessed: str, old_letters_guessed: list) -> bool:
    """
    Checks if the input string represents a single alphabetic character that hasn't been guessed before.

    Args:
        letter_guessed (str): The input string to be validated.
        old_letters_guessed (list): A list of previously guessed letters.

    Returns:
        bool: True if the input is a single alphabetic character that hasn't been guessed before, False otherwise.
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed: str, old_letters_guessed: list) -> bool:
    """
    Tries to update the list of guessed letters with the new guess.

    Args:
        letter_guessed (str): The character entered by the player.
        old_letters_guessed (list): The list of letters the player has guessed so far.

    Returns:
        bool: True if the character is added successfully, False otherwise.
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        print('->'.join(sorted(old_letters_guessed)))
        return False


def print_hangman(num_of_tries: int) -> None:
    """
    Prints the hangman figure based on the number of incorrect guesses.

    Args:
        num_of_tries (int): The number of incorrect guesses made by the user.
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def play_hangman(secret_word: str) -> None:
    """
    Plays the Hangman game with the given secret word.

    Args:
        secret_word (str): The secret word to be guessed by the player.
    """
    global num_of_tries, old_letters_guessed

    print(f"Let's start!\n"
          f"The word to guess has {len(secret_word)} letters\n")

    while num_of_tries < MAX_TRIES:
        print(f"Guess {num_of_tries}/{MAX_TRIES}")
        print_hangman(num_of_tries + 1)
        print(show_hidden_word(secret_word, old_letters_guessed))

        letter_guessed = input("Guess a letter: ").lower()
        print()

        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word:
                print(":(")
                num_of_tries += 1

        if check_win(secret_word, old_letters_guessed):
            print(f"You are right, the word is: {secret_word}!")
            print("WIN")
            break

        print("\n")

    if num_of_tries == MAX_TRIES:
        print(f"Guess {num_of_tries}/{MAX_TRIES}")
        print_hangman(num_of_tries + 1)
        print("LOSE")
        print(f"The word was: {secret_word}")


def main():
    global secret_word

    welcome_screen()

    while True:
        file_path = input("\nEnter file path: ")
        try:
            index = int(input("\n----if an invalid index is entered it will pick a word in random)----"
                              "\nEnter an index (starting from 1): "))
        except ValueError:
            print("Invalid index input. Please enter an integer\n")
            continue

        secret_word = choose_word(file_path, index)

        if secret_word:
            play_hangman(secret_word)

        play_again = input("Do you want to play again? (y/n): \n").lower()
        while play_again != 'y' and play_again != 'n':
            play_again = input("Invalid input, try again.\n"
                               "Do you want to play again? (y/n): \n").lower()
        if play_again != 'y':
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()