

def squared_numbers(start: int, stop: int) -> list:
    """
    Returns a list of squared numbers between start and stop (inclusive).

    Args:
        start (int): The starting number.
        stop (int): The ending number.

    Returns:
        list: A list of squared numbers between start and stop (inclusive).
    """
    result = []
    current = start
    while current <= stop:
        result.append(current ** 2)
        current += 1
    return result

if __name__ == '__main__':
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))