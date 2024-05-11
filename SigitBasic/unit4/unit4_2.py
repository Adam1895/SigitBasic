
def q4_2_2():
    entr_str = input("Enter a string: ").lower().replace(" ", "")
    ans_str = bool(entr_str == entr_str[::-1])
    print(f"{entr_str}\n"
          f"{entr_str[::-1]}")
    if (ans_str == False):
        print("Is palindrom: NOT")
    else:
        print("Is palindrom: OK")

def q4_2_3():
    print("Convert temp from C to F and vise-versa")
    temp_input = input("Enter the temp you would like to convert: ").lower()
    if (temp_input.endswith('f')):
        temp_float = float(temp_input[:-1])
        converted_temp = (temp_float - 32) * (5/9)
        print(f"The conversion from {temp_float}F to C is: {converted_temp}")
    elif (temp_input.endswith('c')):
        temp_float = float(temp_input[:-1])
        converted_temp = (temp_float * (9/5)) + 32
        print(f"The conversion from {temp_float}C to F is: {converted_temp}")
    else:
        print("Invalid input. Please enter a temperature followed by 'f/F' or 'c/C'.")


import calendar
from datetime import datetime
def q4_2_4():
    WEEKDAY_NAMES = {1 : "Monday",
                     2 : "Tuesday",
                     3 : "Wednesday",
                     4 : "Thursday",
                     5 : "Friday",
                     6 : "Saturday",
                     7 : "Sunday"}

    date_str = input("Enter a date: ")
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day

    day_of_week_int = calendar.weekday(year, month, day) + 1
    day_of_week_name = WEEKDAY_NAMES[day_of_week_int]
    print(day_of_week_name)



if __name__ == '__main__':
    q4_2_4()