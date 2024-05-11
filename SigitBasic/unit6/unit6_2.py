
#q6_2_3
def format_list(my_list: list) -> str:
    """
    Returns a string containing the elements at even indices of the input list,
    separated by a comma and a space, and including the last element with the
    word "and" before it.

    Args:
        my_list (list): A list of strings with an even length.

    Returns:
        str: A formatted string with the elements at even indices and the last element.
    """
    even_elements_arr = my_list[::2]
    last_element = my_list[-1]

    result = ", ".join(even_elements_arr) + f" and {last_element}"
    return result


#q6_2_4
def extend_list_x(list_x: list, list_y: list) -> list:
    """
    Extends list_x by adding list_y at the beginning, and returns the updated list_x.

    Args:
        list_x (list): The list to be extended.
        list_y (list): The list to be added at the beginning of list_x.

    Returns:
        list: The updated list_x with list_y added at the beginning.
    """
    list_x[:0] = list_y
    return list_x



if __name__ == '__main__':
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    print(format_list(my_list))

    x = [4, 5, 6]
    y = [1, 2, 3]
    print(extend_list_x(x, y))
