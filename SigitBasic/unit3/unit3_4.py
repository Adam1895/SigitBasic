
def q3_4_2():
    my_str = input("Please enter a string: ")
    first_ch = my_str[0]
    print(first_ch + my_str[1:].replace(first_ch, 'e'))

def q3_4_3():
    my_str = input("Please enter a string: ")
    size = len(my_str)
    mid = size // 2
    print(my_str[:mid].lower() + my_str[mid:].upper())

if __name__ == '__main__':
    q3_4_3()
