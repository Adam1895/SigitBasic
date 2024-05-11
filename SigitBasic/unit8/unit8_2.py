

def sort_prices(list_of_tuples: list) -> list:
    """
    Sorts a list of tuples containing items and their prices in descending order based on the prices.

    Args:
        list_of_tuples (list): A list of tuples, where each tuple contains an item and its price as strings.

    Returns:
        list: A new list of tuples sorted in descending order based on the prices.
    """
    tuples_with_float_prices = []
    for item in list_of_tuples:
        name, price = item
        price = float(price)
        tuples_with_float_prices += [(name, price)]

    def get_price(tuple_item):
        _, price = tuple_item
        return price

    sorted_tuples = sorted(tuples_with_float_prices, key=get_price, reverse=True)

    return sorted_tuples


#q8_2_3
def mult_tuple(tuple1: tuple, tuple2: tuple) -> tuple:
    """
    Returns a tuple containing all pairs of elements from the given tuples.

    Args:
        tuple1 (tuple): The first input tuple.
        tuple2 (tuple): The second input tuple.

    Returns:
        tuple: A tuple containing all pairs of elements from the input tuples, including pairs with elements in reverse order.
    """
    result = []
    for item1 in tuple1:
        for item2 in tuple2:
            result.append((item1, item2))
            result.append((item2, item1))
    return tuple(result)


#q8_2_4
def sort_anagrams(list_of_strings: list) -> list:
    """
    Sorts a list of strings into a list of lists, where each inner list contains strings that are anagrams of each other.

    Args:
        list_of_strings (list): A list of strings, where each string is a single word (no spaces).

    Returns:
        list: A list of lists, where each inner list contains strings that are anagrams of each other.
    """
    anagram_dict = {}

    for string in list_of_strings:
        sorted_string = ''.join(sorted(string))
        anagram_dict.setdefault(sorted_string, []).append(string)

    sorted_anagrams = [sorted(anagrams) for anagrams in anagram_dict.values()]

    return sorted_anagrams


if __name__ == '__main__':
    #q8_2_1
    '''data = ("self", "py", 1.543)
    format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!" % data

    print(format_string)'''

    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))

    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))

    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))