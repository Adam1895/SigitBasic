
#q7_2_1
def is_greater(my_list: list, n: int) -> list:
    """
      Returns a new list containing elements from the given list that are greater than n.

      Args:
          my_list (list): The input list.
          n (int or float): The number to compare against.

      Returns:
          list: A new list containing elements from the input list that are greater than n.
      """

    result = []
    for element in my_list:
        if (element > n):
            result.append(element)
    return result



#q7_2_2
def numbers_letters_count(my_str: str) -> list:
    """
    Returns a list containing the count of digits and non-digit characters in the given string.

    Args:
        my_str (str): The input string.

    Returns:
        list: A list with two elements, where the first element is the count of digits
              and the second element is the count of non-digit characters (letters,
              spaces, punctuation, etc.) in the input string.
    """

    digit_count = 0
    non_digit_count = 0

    for char in my_str:
        if (char.isdigit()):
            digit_count += 1
        else:
            non_digit_count += 1

    return [digit_count, non_digit_count]



#q7_2_4
def seven_boom(end_number: int) -> list:
    """
    Simulates the "Seven Boom" game by replacing certain numbers with the string 'BOOM'.

    Args:
        end_number (int): The ending number of the range.

    Returns:
        list: A list of numbers and 'BOOM' strings in the range 0 to end_number (inclusive),
              where numbers that are multiples of 7 or contain the digit 7 are replaced with 'BOOM'.
    """

    result = []
    for num in range(end_number + 1):
        if ((num % 7 == 0) or (str(num).find('7') != -1)):
            result.append('BOOM')
        else:
            result.append(num)
    return result


#q7_2_5
def sequence_del(my_str: str) -> str:
    """
    Removes consecutive duplicate characters from a given string.

    Args:
        my_str (str): The input string.

    Returns:
        str: A new string with only one instance of each consecutive character sequence.
    """

    result = ""
    prev_char = ""

    for char in my_str:
        if (char != prev_char):
            result += char
            prev_char = char

    return result


#q7_2_6
def get_products():
    """
    Prompts the user to enter a comma-separated list of products and returns a list of products.
    """
    products_str = input("Enter a comma-separated list of products: ")
    products_list = [product.strip() for product in products_str.split(',')]
    return products_list

def print_products(products):
    """
    Prints the list of products.
    """
    print("List of products:")
    for product in products:
        print(product)

def print_product_count(products):
    """
    Prints the number of products in the list.
    """
    count = len(products)
    print(f"Number of products: {count}")

def check_product_in_list(products):
    """
    Checks if a given product is in the list and prints the result.
    """
    product_name = input("Enter a product name: ")
    if product_name in products:
        print(f"{product_name} is in the list.")
    else:
        print(f"{product_name} is not in the list.")

def count_product_occurrences(products):
    """
    Counts the occurrences of a given product in the list and prints the result.
    """
    product_name = input("Enter a product name: ")
    count = products.count(product_name)
    print(f"{product_name} appears {count} times in the list.")

def remove_product(products):
    """
    Removes a given product from the list and prints the result.
    """
    product_name = input("Enter a product name to remove: ")
    if product_name in products:
        products.remove(product_name)
        print(f"{product_name} has been removed from the list.")
    else:
        print(f"{product_name} is not in the list.")

def add_product(products):
    """
    Adds a given product to the list and prints the result.
    """
    product_name = input("Enter a product name to add: ")
    products.append(product_name)
    print(f"{product_name} has been added to the list.")

def print_invalid_products(products):
    """
    Prints the list of invalid products (length < 3 or contains non-alphabetic characters).
    """
    invalid_products = [product for product in products if len(product) < 3 or not product.isalpha()]
    if invalid_products:
        print("Invalid products (length < 3 or contains non-alphabetic characters):")
        for product in invalid_products:
            print(product)
    else:
        print("All products are valid.")

def remove_duplicates(products):
    """
    Removes duplicate products from the list, prints a message, and returns the list with unique products.
    """
    unique_products = list(set(products))
    print("Duplicate products have been removed.")
    return unique_products

def main():
    """
    Main function that runs the program.
    """
    products = get_products()

    while True:
        choice = int(input("\nChoose an option:\n"
                           "1. Print the list of products\n"
                           "2. Print the number of products\n"
                           "3. Check if a product is in the list\n"
                           "4. Count occurrences of a product\n"
                           "5. Remove a product from the list\n"
                           "6. Add a product to the list\n"
                           "7. Print invalid products\n"
                           "8. Remove duplicate products\n"
                           "9. Exit\n"
                           "Enter your choice: "))

        if choice == 1:
            print_products(products)
        elif choice == 2:
            print_product_count(products)
        elif choice == 3:
            check_product_in_list(products)
        elif choice == 4:
            count_product_occurrences(products)
        elif choice == 5:
            remove_product(products)
        elif choice == 6:
            add_product(products)
        elif choice == 7:
            print_invalid_products(products)
        elif choice == 8:
            products = remove_duplicates(products)
        elif choice == 9:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

#q7_2_7
def arrow(my_char: str, max_length: int) -> str:
    """
    Returns a string representing an arrow shape made up of the given character.

    Args:
        my_char (str): A single character to be used for building the arrow shape.
        max_length (int): The maximum length of the center row (the longest row) of the arrow shape.

    Returns:
        str: A string representing the arrow shape.
    """

    result = []
    for i in range(max_length):
        row = my_char * (i + 1)
        result.append(row)

    result.extend(result[max_length - 2::-1])

    return "\n".join(result)


if __name__ == '__main__':
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)

    print(numbers_letters_count("Python 3.6.3"))

    print(seven_boom(17))

    print(f"{sequence_del('ppyyyyythhhhhooonnnnn')}\n"
          f"{sequence_del('SSSSsssshhhh')}\n"
          f"{sequence_del('Heeyyy   yyouuuu!!!')}")

    #main()

    print(arrow('.', 5))