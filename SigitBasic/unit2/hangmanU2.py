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
    guess_str = input("Guess a letter: ")
    print(guess_str)


if __name__ == '__main__':
    print(f"{HANGMAN_ASCII_ART}\n"
          f"Max tries: {MAX_TRIES}\n")

    base_game()
