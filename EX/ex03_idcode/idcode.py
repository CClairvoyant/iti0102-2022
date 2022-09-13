"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """
    idcode = ""
    for character in text:
        if character.isdigit():
            idcode += character
        else:
            idcode += ""

    if len(idcode) < 11:
        return "Not enough numbers!"
    elif len(idcode) > 11:
        return "Too many numbers!"
    else:
        return idcode


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    idcode = ""
    for character in text:
        if character.isdigit():
            idcode += character
        else:
            idcode += ""

    if len(idcode) < 11:
        return "Incorrect ID code!"
    elif len(idcode) > 11:
        return "Incorrect ID code!"

    control_number = (int(idcode[0]) + int(idcode[1]) * 2 + int(idcode[2]) * 3 + int(idcode[3]) * 4 +
                      + int(idcode[4]) * 5 + int(idcode[5]) * 6 + int(idcode[6]) * 7 + int(idcode[7]) * 8 +
                      + int(idcode[8]) * 9 + int(idcode[9])) % 11

    if len(idcode) == 11 and control_number == int(idcode[-1]):
        return idcode
    elif control_number < 10 and control_number != int(idcode[-1]):
        return "Incorrect ID code!"
    else:
        return "Needs the second algorithm!"


if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print(the_first_control_number_algorithm(""))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("123456789123456789"))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("ID code is: 49403136526"))  # -> "49403136526"
    print(the_first_control_number_algorithm("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"
    print(the_first_control_number_algorithm("50412057633"))  # -> "50412057633"
    print(the_first_control_number_algorithm("Peeter's ID is euf50weird2fs0fsk51ef6t0s2yr7fyf4"))  # -> "Needs
    # the second algorithm!"


def is_valid_gender_number(gender_number: int) -> bool:
    """Check if given value is correct for gender number in ID code."""
    if 0 < gender_number < 7:
        return True
    else:
        return False


def get_gender(gender_number: int) -> str:
    """Check the gender of the ID code."""
    if gender_number in (1, 3, 5):
        return "male"
    elif gender_number in (2, 4, 6):
        return "female"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    if 0 <= year_number < 100:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    if month_number in range(1, 13):
        return True
    else:
        return False


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    if 0 < birth_number < 1000:
        return True
    else:
        return False


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> True

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True


def is_leap_year(year_number: int) -> bool:
    if year_number % 400 == 0:
        return True
    elif year_number % 4 == 0 and year_number % 100 != 0:
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    year = 0
    if gender_number in (1, 2):
        year = year_number + 1800
    elif gender_number in (3, 4):
        year = year_number + 1900
    elif gender_number in (5, 6):
        year = year_number + 2000
    return year


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    if birth_number in range(1, 11):
        return "Kuressaare"
    elif birth_number in range(11, 21):
        return "Tartu"
    elif birth_number in range(21, 221):
        return "Tallinn"
    elif birth_number in range(221, 271):
        return "Kohtla-Järve"
    elif birth_number in range(271, 371):
        return "Tartu"
    elif birth_number in range(371, 421):
        return "Narva"
    elif birth_number in range(421, 471):
        return "Pärnu"
    elif birth_number in range(471, 711):
        return "Tallinn"
    elif birth_number < 1:
        return "Wrong input!"
    else:
        return "undefined"


if __name__ == '__main__':
    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"
