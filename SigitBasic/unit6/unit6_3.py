
#q6_3_1
def are_lists_equal(list1: list, list2: list) -> bool:
    """
    Checks if two lists containing only integers and floats are equal.

    Args:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.

    Returns:
        bool: True if the lists contain exactly the same elements (possibly in a different order), False otherwise.
    """
    return (sorted(list1) == sorted(list2))



#q6_3_2
def longest(my_list: list) -> str:
    """
    Returns the longest string from the input list of strings.

    Args:
        my_list (list): A list of strings.

    Returns:
        str: The longest string from the input list.
    """
    return max(my_list, key=len)

if __name__ == '__main__':
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(f"{are_lists_equal(list1, list2)}\n"
          f"{are_lists_equal(list1, list3)}")

    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))