
if __name__ == '__main__':
    guess_str = input("Enter a string: ").lower()
    length = len(guess_str)
    has_multiple_chars = (length > 1)
    has_non_alphabetic = (not(guess_str.isalpha()))

    if (has_multiple_chars and has_non_alphabetic):
        print("E3")
    elif (has_multiple_chars):
        print("E1")
    elif (has_non_alphabetic):
        print("E2")
    else:
        print(guess_str)