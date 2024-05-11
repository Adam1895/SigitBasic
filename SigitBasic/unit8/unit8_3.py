
#q8_3_2
maria = {
    "first_name": "Maria",
    "last_name": "Carey",
    "birth_date": "27.03.1970",
    "hobbies": ["Sing", "Compose", "Act"]
}

def main():
    global maria
    choice = int(input("Enter a number (1-7): "))

    if choice == 1:
        print(f"Maria's last name is: {maria['last_name']}")
    elif choice == 2:
        birth_month = maria["birth_date"].split(".")[1]
        print(f"Maria was born in month: {birth_month}")
    elif choice == 3:
        num_hobbies = len(maria["hobbies"])
        print(f"Maria has {num_hobbies} hobbies.")
    elif choice == 4:
        last_hobby = maria["hobbies"][-1]
        print(f"Maria's last hobby is: {last_hobby}")
    elif choice == 5:
        maria["hobbies"].append("Cooking")
        print("'Cooking' has been added to Maria's hobbies.")
        print(maria)
    elif choice == 6:
        birth_date_tuple = tuple(int(part) for part in maria["birth_date"].split("."))
        print(f"Maria's birth date as a tuple: {birth_date_tuple}")
    elif choice == 7:
        current_year = 2023
        birth_year = int(maria["birth_date"].split(".")[2])
        age = current_year - birth_year
        maria["age"] = age
        print(f"Maria's age has been added: {maria['age']}")
        print(maria)
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")


#q8_3_3
def count_chars(my_str: str) -> dict:
    """
    Returns a dictionary where the keys are the unique characters in the given string
    (excluding spaces), and the values are the count of occurrences of each character.

    Args:
        my_str (str): The input string.

    Returns:
        dict: A dictionary where the keys are unique characters and the values are their counts.
    """
    char_counts = {}

    for char in my_str:
        if char == ' ':
            continue

        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts


#q8_3_4
def inverse_dict(my_dict: dict) -> dict:
    """
    Returns a new dictionary with keys and values swapped, where the values in the
    new dictionary are represented as sorted lists.

    Args:
        my_dict (dict): The input dictionary.

    Returns:
        dict: A new dictionary with keys and values swapped, where the values are
              sorted lists.
    """
    inverse = {}

    for key, value in my_dict.items():
        if value in inverse:
            inverse[value].append(key)
        else:
            inverse[value] = [key]

    for value_list in inverse.values():
        value_list.sort()

    return inverse

if __name__ == "__main__":
    #main()

    magic_str = "abra cadabra"
    print(count_chars(magic_str))

    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))
