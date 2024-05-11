def program(num_of_bricks: int):
    # num_of_bricks: 3 digit num, each digit indicates the amount of bricks a pig has
    sum_bricks = (num_of_bricks % 10) + ((num_of_bricks // 10) % 10) + (num_of_bricks // 100)
    avg_bricks = sum_bricks // 3
    leftover = sum_bricks % 3
    is_equal = (avg_bricks == leftover)

    print(f"Original 3 digit num: {num_of_bricks}\n"
          f"Sum of all the digits: {sum_bricks}\n"
          f"Avg without leftovers: {avg_bricks}\n"
          f"Leftovers: {leftover}\n"
          f"Are there no leftovers: {is_equal}")


if __name__ == '__main__':
    program(124)