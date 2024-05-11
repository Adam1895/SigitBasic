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

def base_game():
    """
                אפשר גם ככה:

    og_str = input("Enter a string: ").lower()
    size = len(og_str)
    blank_str = "".zfill(size).replace('0', '_')
    print(blank_str)
    """

    og_str = input("Enter a string: ").lower()
    new_str = '_' * len(og_str)
    print(new_str)


if __name__ == '__main__':
    print(f"{HANGMAN_ASCII_ART}\n"
          f"Max tries: {MAX_TRIES}\n")

    base_game()
