

#q5_3_4
def last_early(my_str):
    last_chr = my_str.lower()[-1]
    print(last_chr)
    print( my_str.lower()[:-1])
    if (last_chr in my_str.lower()[:-1]):
        return True
    else:
        return False

#q5_3_5
def distance(num1, num2, num3):
    if(((abs(num1-num2) == 1) or (abs(num1 - num3) == 1)) and ((abs(num1-num2) > 2) or (abs(num1 - num3) > 3))):
        return True
    else:
        return False


#q5_3_6
def fix_age(age):
    if ((13 <= age <= 19) and (age not in (15, 16))):
        return 0
    else:
        return age

def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)

    return (a + b + c)


#q3_5_7
def chocolate_maker(small, big, x):
    total_length = (small + (5 * big))
    return (total_length >= x)


if __name__ == '__main__':
    """my_str = input("Enter a string: ")
    print(last_early(my_str))

    print(distance(1, 2, 10))
    print(distance(4, 5, 3))

    print(filter_teens(),
          filter_teens(1, 2, 3),
          filter_teens(2, 13, 1),
          filter_teens(2, 1, 15))"""

    print(chocolate_maker(3, 1, 8),
          chocolate_maker(3, 1, 9),
          chocolate_maker(3, 2, 10))




