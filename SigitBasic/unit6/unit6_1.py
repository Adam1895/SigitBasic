

def shift_left(my_list: list) -> list:
    shifted_list = my_list[1:] + [my_list[0]]
    return shifted_list

if __name__ == '__main__':
    print(f"Og: [0,1,2] -> {shift_left([0, 1, 2])}\n"
          f"Og: ['monkey', 2.0, 1] -> {shift_left(['monkey', 2.0, 1])}")