HANGMAN_PHOTOS = {
    0: """
x-------x
""",
    1: """
x-------x
|
|
|
|
|
""",
    2: """
x-------x
|       |
|       0
|
|
|
""",
    3: """
x-------x
|       |
|       0
|       |
|
|
""",
    4: """
x-------x
|       |
|       0
|      /|\\
|
|
""",
    5: """
x-------x
|       |
|       0
|      /|\\
|      /
|
""",
    6: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""
}

def print_hangman(num_of_tries: int) -> None:
    """
    Prints the hangman figure based on the number of incorrect guesses.

    Args:
        num_of_tries (int): The number of incorrect guesses made by the user.
    """
    if num_of_tries in HANGMAN_PHOTOS:
        print(HANGMAN_PHOTOS[num_of_tries])
    else:
        print("Invalid number of tries.")

if __name__ == "__main__":
    num_of_tries = 6
    print_hangman(num_of_tries)