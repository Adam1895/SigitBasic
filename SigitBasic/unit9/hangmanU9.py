import random


def choose_word(file_path: str, index: int) -> tuple:
    """
    Chooses a secret word from a text file at the specified index.

    Args:
        file_path (str): The path to the text file containing the words.
        index (int): The position of the desired word in the file (starting from 1).

    Returns:
        tuple: A tuple containing the number of unique words in the file and the secret word.
    """
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            unique_words = list(set(words))
            num_unique_words = len(unique_words)

            index = (index - 1) % len(words)
            secret_word = words[index]

            print(f"randomly picked word: {words[random.randint(0, len(words) - 1)]}")
            return (num_unique_words, secret_word)
    except FileNotFoundError:
        print(f"File {file_path} not found.")


if __name__ == '__main__':
    print(choose_word("words.txt", 3))
    print(choose_word("words.txt", 15))